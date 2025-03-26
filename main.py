from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, Body
#pandas is used to handle CSV files.
import pandas as pd
import uuid
import io
from pymongo import MongoClient
# transformers.pipeline loads the Hugging Face LLaMA model.
from sentence_transformers import SentenceTransformer  
import torch
import json
from typing import Optional

# Connecting Locally Stored database mongodb to store csv files
client = MongoClient("mongodb://localhost:27017/")
db = client["csv_database"]
collection = db["csv_files"]

#The Hugging Face pipeline is set up for text generation.
#This model is used later for generating responses based on retrieved CSV data.
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to CSV RAG API!"}

# Upload CSV File
@app.post("/upload")
async def upload_csv(
    file: Optional[UploadFile] = File(None),
    file_path: Optional[str] = Body(None)
):
    try:
        if not file and not file_path:
            raise HTTPException(status_code=400, detail="No file or file path provided")

        if file:
            if not file.filename.endswith('.csv'):
                raise HTTPException(status_code=400, detail="Only CSV files allowed")
            contents = await file.read()
            csv_data = io.StringIO(contents.decode('utf-8', errors='replace'))
        else:
            with open(file_path, "r", encoding="utf-8") as f:
                csv_data = io.StringIO(f.read())

        df = pd.read_csv(csv_data)
        if df.empty:
            raise HTTPException(status_code=400, detail="CSV file is empty")

        file_id = str(uuid.uuid4())
        json_data = df.to_dict(orient="records")
        embeddings = [embedding_model.encode(str(row), convert_to_tensor=True).tolist() for row in json_data]

        collection.insert_one({
            "file_id": file_id,
            "file_name": file.filename if file else file_path,
            "data": json_data,
            "embeddings": embeddings
        })

        return {"file_id": file_id, "message": "Upload successful"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/files")
async def get_files():
    try:
        files = collection.find({}, {"_id": 0, "file_id": 1, "file_name": 1})
        return {"files": list(files)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query")
async def query_csv(file_id: str = Body(...), query: str = Body(...)):
    try:
        file_data = collection.find_one({"file_id": file_id})
        if not file_data:
            raise HTTPException(status_code=404, detail="File not found")

        csv_data = file_data["data"]
        embeddings = torch.tensor(file_data["embeddings"])
        query_embedding = embedding_model.encode(query, convert_to_tensor=True)

        similarity_scores = torch.nn.functional.cosine_similarity(query_embedding, embeddings)
        most_relevant_index = torch.argmax(similarity_scores).item()
        response = csv_data[most_relevant_index]

        return {"response": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/file/{file_id}")
async def delete_file(file_id: str):
    result = collection.delete_one({"file_id": file_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="File not found")
    return {"message": "File deleted successfully"}