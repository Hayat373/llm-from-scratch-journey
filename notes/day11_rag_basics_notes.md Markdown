# Day 11 Notes - RAG (Retrieval Augmented Generation)

**Date:** June 15, 2026

## Key Concepts Learned

### What is RAG?
- **Retrieval Augmented Generation**
- Instead of only relying on what the model learned during training, we retrieve relevant information from external data and give it to the model at inference time.

### Main Components
1. **Knowledge Base** — Your custom data/documents
2. **Embeddings** — Convert text into numerical vectors (`SentenceTransformer`)
3. **Vector Database** — FAISS (fast similarity search)
4. **Retriever** — Finds most relevant chunks for a query
5. **Generator** — LLM that uses the retrieved context to answer

### Why RAG is Important
- Reduces hallucinations
- Allows model to work with up-to-date or private information
- Very popular in production applications

## Tools Used Today
- `sentence-transformers` → Embeddings
- `faiss` → Vector search
- Hugging Face models → Generation

## My Current Understanding
- Good grasp of the basic RAG pipeline
- Still need to fully integrate retrieval with model generation
- Need to learn advanced RAG (chunking, better embeddings, reranking, etc.)

## Next Goals
- Build a complete RAG chatbot
- Use LangChain or LlamaIndex for easier RAG
- Add RAG to my Ethiopian AI Assistant

**Major Takeaway:**  
RAG is the bridge between powerful pre-trained models and real useful applications.