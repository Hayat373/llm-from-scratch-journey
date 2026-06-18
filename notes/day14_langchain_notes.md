# Day 14 Notes - LangChain Framework Deep Dive

**Date:** june 18, 2026

## Why LangChain Matters
- It is the most popular framework for building LLM-powered applications
- Saves hundreds of lines of code
- Has excellent integrations (Vector DBs, Agents, Memory, Tools, etc.)

## Core LangChain Concepts Learned

### 1. Document Loading & Splitting
- `TextLoader` → Loads files
- `CharacterTextSplitter` → Splits long text into smaller chunks (very important for RAG)

### 2. Embeddings + Vector Store
- `HuggingFaceEmbeddings` → Converts text to vectors
- `FAISS` → Fast similarity search

### 3. Retriever
- Turns VectorStore into a tool that can find relevant documents for a query

### 4. Chains
- `LLMChain` + `PromptTemplate` → Connects prompt + LLM
- `RetrievalQA` → Combines retriever + LLM (higher level)

## Key Takeaways

- **Modular Design**: LangChain breaks complex systems into reusable components
- **Prompt Engineering** becomes more organized with `PromptTemplate`
- RAG with LangChain is cleaner and easier to maintain than pure PyTorch code
- This is the kind of code companies actually use in production

## My Current Level
- Can now build basic RAG applications using LangChain
- Understand the high-level architecture of LLM apps
- Still need to learn:
  - Memory (conversation history)
  - Agents (tool calling)
  - Advanced RAG (Parent-Document, HyDE, etc.)

## Comparison: Manual RAG vs LangChain
| Aspect               | Manual Code         | LangChain              |
|----------------------|---------------------|------------------------|
| Code Length          | Long                | Much shorter           |
| Maintainability      | Hard                | Easy                   |
| Features             | Basic               | Rich ecosystem         |
| Learning Curve       | Steep               | Moderate               |

**Major Realization**:  
Understanding the fundamentals (from Days 1-13) helps me use frameworks like LangChain much better. Now I know **what** is happening behind the abstractions.

