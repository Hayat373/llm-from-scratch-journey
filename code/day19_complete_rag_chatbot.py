# Day 19 - Complete RAG + Memory Chatbot (Portfolio Ready)

import gradio as gr
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

print("Loading components...")

# ====================== KNOWLEDGE BASE ======================
knowledge_base = [
    "Addis Ababa is the capital and largest city of Ethiopia.",
    "Ethiopia is known as the cradle of humanity.",
    "Injera is the national dish of Ethiopia made from teff flour.",
    "Lalibela is famous for its 11 rock-hewn churches.",
    "Ethiopia is the birthplace of coffee.",
    "The Ethiopian calendar is 7-8 years behind the Gregorian calendar.",
    "AI and tech startups are growing rapidly in Addis Ababa, especially in Bole.",
    "Ethiopia has a rich history as one of the oldest countries in the world.",
]

# Embeddings + Vector DB
embedder = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = embedder.encode(knowledge_base)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# ====================== MODEL ======================
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
)

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quant_config,
    device_map="auto"
)

def retrieve(query, top_k=3):
    query_emb = embedder.encode([query])
    _, indices = index.search(query_emb, top_k)
    return [knowledge_base[i] for i in indices[0]]

def chatbot(message, history):
    # Retrieve relevant knowledge
    context = retrieve(message)
    context_text = "\n".join(context)
    
    # Build prompt with history + context
    prompt = f"""You are a helpful, friendly, and knowledgeable Ethiopian AI assistant.

Context from knowledge base:
{context_text}

Previous conversation:
{chr(10).join([f"User: {h[0]}\nAssistant: {h[1]}" for h in history[-3:]] if history else [])}

User: {message}
Assistant:"""

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        inputs.input_ids,
        max_new_tokens=300,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    if "Assistant:" in response:
        response = response.split("Assistant:")[-1].strip()
    return response

# ====================== GRADIO UI ======================
demo = gr.ChatInterface(
    fn=chatbot,
    title="🇪🇹 Ethiopian AI Assistant",
    description="RAG + Memory Powered • Ask anything about Ethiopia, culture, history, food, or technology!",
    theme=gr.themes.Soft(),
    examples=[
        "What is the capital of Ethiopia?",
        "Tell me about Ethiopian food",
        "What should I know before visiting Addis Ababa?",
        "Tell me about the history of coffee"
    ]
)

demo.launch(share=True)