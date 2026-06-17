import gradio as gr
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# ====================== SETUP ======================
device = "cuda" if torch.cuda.is_available() else "cpu"

# 1. Embedding Model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Knowledge Base (Expand this!)
knowledge_base = [
    "Addis Ababa is the capital and largest city of Ethiopia.",
    "Ethiopia is one of the oldest countries in the world.",
    "Injera is the national dish of Ethiopia.",
    "The Ethiopian calendar is 7 to 8 years behind the Gregorian calendar.",
    "Ethiopia has incredible coffee culture - it is the birthplace of coffee.",
    "AI and tech startups are growing fast in Addis Ababa, especially in Bole area.",
    "Lalibela is famous for its rock-cut churches.",
]

embeddings = embedder.encode(knowledge_base)
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# 3. LLM
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16 if device == "cuda" else torch.float32)
model = model.to(device)

print("✅ RAG Chatbot Ready!")

# Retrieval Function
def retrieve(query, top_k=3):
    query_emb = embedder.encode([query])
    D, I = index.search(query_emb, top_k)
    return [knowledge_base[i] for i in I[0]]

# Generation Function
def generate_response(query, history):
    context = retrieve(query)
    context_text = "\n".join(context)
    
    system_prompt = f"""You are a helpful and friendly Ethiopian AI assistant. 
    Use the provided context to answer accurately.

    Context:
    {context_text}"""
    
    full_prompt = f"<|system|>\n{system_prompt}</s>\n<|user|>\n{query}</s>\n<|assistant|>"
    
    inputs = tokenizer(full_prompt, return_tensors="pt").to(device)
    outputs = model.generate(
        inputs.input_ids,
        max_new_tokens=300,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = response.split("<|assistant|>")[-1].strip()
    return response

# Gradio Chat Interface
def chatbot(message, history):
    response = generate_response(message, history)
    return response

# Launch the app
with gr.Blocks(title="Ethiopian AI Assistant") as demo:
    gr.Markdown("# 🇪🇹 Ethiopian AI Assistant (RAG Powered)")
    gr.Markdown("Ask anything about Ethiopia, culture, food, history, or technology!")
    
    chatbot_interface = gr.ChatInterface(
        fn=chatbot,
        title="Chat with Ethiopian AI",
        description="Powered by RAG + TinyLlama"
    )

demo.launch(share=True)   # share=True gives you a public link