# Day 22 Notes - Advanced RAG Techniques

**Date:** June 24, 2026

## What is Advanced RAG?

**Basic RAG**: Split documents into chunks → Embed → Retrieve top-k → Send to LLM

**Advanced RAG**: Adds multiple improvements to make retrieval much smarter and more accurate.

## Key Advanced Techniques Learned

### 1. Better Chunking Strategies
- **RecursiveCharacterTextSplitter**: Splits text intelligently (first by paragraphs, then sentences, then words)
- **Chunk Size & Overlap**: 
  - Too small chunks → lose context
  - Too large chunks → lose precision
  - Overlap helps maintain continuity between chunks
- **Semantic Chunking** (Future topic): Split based on meaning instead of fixed size

### 2. Improved Retrieval
- **Metadata Filtering**: Add source, date, topic to chunks and filter them
- **Multi-Query Retrieval**: Generate multiple versions of the question to retrieve better results
- **Reranking**: After initial retrieval, use a reranker model to reorder results by relevance (very powerful)
- **HyDE (Hypothetical Document Embeddings)**: Generate a hypothetical answer first, then retrieve based on it

### 3. Better Prompt Engineering for RAG
- Clear instructions to the model ("Answer only using the context")
- Include source references
- Structured output format

### 4. Evaluation of RAG
- Faithfulness (Does the answer match the context?)
- Relevance (Is the answer useful for the question?)
- Answer Relevancy

## Why Advanced RAG Matters
- Significantly reduces hallucinations
- Handles complex and multi-hop questions better
- More reliable for real-world applications (customer support, knowledge bases, research assistants)

## My Current Understanding
- I now understand why simple RAG is often not enough
- I can implement better chunking and improved prompts
- Still need to learn reranking and advanced evaluation methods

## Major Takeaway
**"Retrieval quality is more important than model size."**  
Even a small model can give excellent answers if it receives the right context.

This is why companies invest heavily in good RAG pipelines.

## Next Goals
- Implement reranking
- Add conversation memory to RAG
- Build evaluation system for RAG
- Create a production-ready RAG application

