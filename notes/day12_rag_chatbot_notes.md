# Day 12 Notes - Building RAG Chatbot with Gradio

**Date:** June 16, 2026

## What We Built Today
- A complete RAG system (Retrieval + Generation)
- Gradio Chat Interface
- Ethiopian knowledge base
- Deployable web app (local + public link)

## Technical Stack
- **Embeddings**: SentenceTransformer (`all-MiniLM-L6-v2`)
- **Vector DB**: FAISS
- **LLM**: TinyLlama-1.1B
- **UI**: Gradio

## Performance Issues I Faced
- Running 1.1B model on CPU is slow
- Long response time (common problem)
- High memory usage

## Solutions I Should Learn Next
- Model Quantization (4-bit, 8-bit)
- Using faster inference engines (llama.cpp, vLLM)
- Smaller models or distilled versions
- Running on better GPU / Google Colab

## Major Takeaway
Even with slow performance, building a full-stack RAG app with UI is **excellent for portfolio**. This kind of project is what recruiters and hackathon judges like to see.

## Next Goals
- Optimize the app for speed
- Improve RAG (better chunking, metadata, etc.)
- Deploy on Hugging Face Spaces or Streamlit

**Personal Note:** Slow performance is normal at this stage. The important thing is that I built a working end-to-end application.