# Day 16 - Deployable RAG Chatbot
import gradio as gr
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# ====================== SETUP ======================
device = "cuda" if torch.cuda.is_available() else "cpu"

# Knowledge Base (Add more content!)
knowledge_base = [
    "Addis Ababa is the capital of Ethiopia.",
    "Ethiopia is the cradle of humanity.",
    "Injera is the national dish made from teff flour.",
    "Lalibela is famous for its rock-hewn churches.",
    "Ethiopia is the birthplace of coffee.",
    "AI and tech startups are growing rapidly in Addis Ababa.",
]

# Embeddings + FAISS
embedder = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = embedder.encode(knowledge_base)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Load Quantized Model for Speed
tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
model = AutoModelForCausalLM.from_pretrained(
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    device_map="auto"
)

def retrieve(query, top_k=3):
    query_emb = embedder.encode([query])
    _, indices = index.search(query_emb, top_k)
    return [knowledge_base[i] for i in indices[0]]

def chatbot(message, history):
    context = retrieve(message)
    context_text = "\n".join(context)
    
    prompt = f"""You are a helpful Ethiopian AI assistant. Use the context to answer.

Context: {context_text}

User: {message}
Assistant:"""

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(inputs.input_ids, max_new_tokens=300, temperature=0.7, top_p=0.9, do_sample=True, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    if "Assistant:" in response:
        response = response.split("Assistant:")[-1].strip()
    return response

# Launch Gradio App
demo = gr.ChatInterface(
    fn=chatbot,
    title="🇪🇹 Ethiopian AI Assistant",
    description="RAG Powered • Ask anything about Ethiopia!",
    theme=gr.themes.Soft()
)

demo.launch(share=True)