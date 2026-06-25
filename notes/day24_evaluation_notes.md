# Day 24 Notes - Model Evaluation & Benchmarking

**Date:** June 25, 2026

## Why Evaluation Matters
Without good evaluation, we cannot know if our changes (better prompts, RAG, fine-tuning, etc.) are actually improvements.

## Main Evaluation Methods

### 1. Perplexity (Intrinsic)
- Measures how "surprised" the model is by a piece of text.
- Calculated using cross-entropy loss.
- **Lower perplexity = better** language modeling ability.
- Best used for comparing language models on the same dataset.

### 2. Faithfulness (RAG specific)
- Checks whether the generated answer is supported by the retrieved context.
- Very important to reduce hallucinations in RAG systems.
- Can be measured automatically (using another LLM as judge) or manually.

### 3. Relevance / Usefulness
- Does the answer actually solve the user's question?
- Can be measured by similarity between question and answer embeddings.

### 4. Human Evaluation (Gold Standard)
- Still the most reliable method.
- Usually scored on:
  - Relevance (1-10)
  - Factual Accuracy
  - Helpfulness
  - Naturalness / Fluency

## Key Takeaways from Today
- Automatic metrics are useful for fast iteration
- No single metric is perfect — we need a combination
- For RAG systems, **Faithfulness** is one of the most important metrics
- Small models like TinyLlama have high perplexity and weaker reasoning

## My Current Understanding
- Good conceptual understanding of different evaluation types
- Can implement basic perplexity and faithfulness checks
- Still need to learn:
  - LLM-as-a-Judge techniques
  - Standard benchmarks (MMLU, TruthfulQA, etc.)
  - RAG-specific evaluation frameworks (Ragas, ARES, etc.)

## Major Takeaway
**"If you can't measure it, you can't improve it."**

Strong evaluation skills separate hobby projects from production-grade and job-worthy applications.

## Next Goals
- Implement LLM-as-a-Judge for automatic evaluation
- Add evaluation to my RAG chatbot
- Learn popular benchmarks

**Personal Note:** Day 24 was more theoretical but very important for building high-quality systems.