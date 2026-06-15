# Day 11 Log

**Date:** june 15, 2026

**Focus:** Introduction to RAG (Retrieval Augmented Generation)

**What I Did**
- Learned the concept of RAG
- Implemented a simple RAG system using embeddings + vector database
- Built a knowledge-based AI assistant (on custom data)
- Compared normal prompting vs RAG

**Key Learnings**
- RAG = Retrieval + Generation
- Embeddings convert text into vectors so we can find similar content
- FAISS is a fast vector database for similarity search
- Providing relevant context to the model greatly reduces hallucinations and improves accuracy
- RAG is one of the most practical and widely used techniques in real LLM applications

**Challenges**
- Setting up FAISS and understanding embeddings
- Combining retrieval with generation (still need to fully connect with model generation)
- Knowledge base quality directly affects answer quality

**Reflection**
RAG feels like a big step toward building useful real-world applications. This is much more powerful than plain prompting.

**GitHub Commit Link** [https://github.com/Hayat373/llm-from-scratch-journey.git]