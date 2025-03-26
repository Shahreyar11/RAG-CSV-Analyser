<h1>RAG-CSV-AI Project - README</h1>

<h2>Overview</h2>
<p>This project is an AI-based application using the <strong>MiniLM-L6-v2</strong> model. It is designed to handle text generation tasks efficiently. The goal is to provide meaningful AI-generated responses from any CSV based file while integrating an intuitive UI.</p>

<h2>Images</h2>

![Screenshot 2025-03-26 214527](https://github.com/user-attachments/assets/415253f5-2454-4895-b916-dea18a274828)

![Screenshot 2025-03-26 214534](https://github.com/user-attachments/assets/d9f9fe98-d6e7-47c0-af25-07bb2c77ca16)



<h2>Key Features</h2>
<ul>
    <li>Uses <strong>Hugging Face</strong> for AI model integration</li>
    <li>Supports <strong>text generation</strong> with a well-optimized pipeline</li>
    <li>Allows authentication using Hugging Face API tokens</li>
    <li>Can be fine-tuned for better response quality</li>
</ul>

<h2>Installation</h2>
<pre>
Install all the necessary libraries given in the Requirements.txt file. 
    Clone the repository to your local computer and run "uvicorn main:app --reload" in one terminal and in another terminal run "streamlit run streamlit_app.py" for the UI from Streamlit part.
</pre>

<h2>Usage</h2>
<pre>
from transformers import pipeline
llm_pipeline = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")
result = llm_pipeline("Your input text here")
print(result)
</pre>

<h2>My Points</h2>
<ul>
    <li>It helps in Generating important data or specific data from any CSv files.</li>
    <li>Optimize model for better performance</li>
    <li>Good Streamlit UI makes good approach and better workflow</li>
    <li>Test different models for better accuracy</li>
</ul>

<h3> My Points: </h3>
<p> Hi, So I am Shahreyar I got this Project as an assignment by the Simplify Money, and I read the pdf file which contains 3 projects to choose from. No doubt all three projects seemed to be the best approach to newer project and new learning. Since I had developed apps in Android and not in React Native I chose this Python backend Projects as backend always fascinates me and though I was new to RAG, LLM, FASTAPI it seemed good option to explore this backend project to learn more.\n Moreover I genuinely didn't know how to proceed and have never created this big project though I have created in other aspects but not for the backend so I directly went to AI tools to get the overview of the project, I learned something new and finding out different things on stackoverflow on youtube on chat gpt from learning what is FASTAPI to watching videos of how to upload csv files using FASTAPI and honestly taking helps from AI tools I came up finally with this. Yes I know the LLM didn't worked well as I never used that and honestly I tried from finding it it was little bit harder for me to implement in such short time but still I managaed to use this mini LLM to generate answers based on CSV files. The project was really good, I learned a lot as I was having some issues on how to proceed learning backend development but Now I found out learning by doing is a great thing and this project taught me on where do I lag in concepts and which concepts do I have to make more stronger in order to become more efficient and good programmer.\n So Yes that was all and I hope this you will find this project well.</p>
