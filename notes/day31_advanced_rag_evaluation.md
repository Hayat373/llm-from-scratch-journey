# Day 31 Notes - Advanced RAG + Evaluation

**Date:** May 21, 2026

## Advanced RAG Techniques

### 1. Smart Chunking
- `RecursiveCharacterTextSplitter`: Splits intelligently by paragraphs, sentences, then words
- Chunk size (300-500) and overlap (50-100) are important
- Better than fixed-size splitting for maintaining context

### 2. Improved Retrieval
- More chunks retrieved (top-k = 4-6)
- Metadata filtering (source, date, importance)
- Reranking results for better relevance

### 3. LLM-as-a-Judge
- Use another LLM to score answers on faithfulness, relevance, and helpfulness
- Very useful for fast iteration
- Small models are inconsistent judges

## Evaluation Metrics
- **Faithfulness**: Does the answer stick to the context?
- **Relevance**: Does it answer the question?
- **Perplexity**: How natural is the generated text?
- **Human Evaluation**: Gold standard

## Major Takeaway
**"Good retrieval is more important than a bigger model."**

Advanced RAG + proper evaluation turns a basic chatbot into a reliable system.

## My Current Understanding
- Can implement advanced RAG with better chunking and prompting
- Can use LLM-as-a-Judge for basic evaluation
- Still need practice with reranking and larger-scale evaluation

## Next Goals
- Build a production-ready RAG system
- Add memory to RAG
- Create evaluation pipeline for portfolio projects

**Personal Note:** Day 31 was more technical but very important for making real, useful applications.