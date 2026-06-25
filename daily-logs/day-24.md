# Day 24 Log

**Date:** June 25, 2026

**Focus:** Model Evaluation & Benchmarking

**What I Did**
- Learned different ways to evaluate LLMs
- Implemented basic evaluation metrics (Perplexity, Faithfulness, Relevance)
- Compared different models and prompting strategies
- Started thinking about how to measure quality of my RAG and fine-tuned models

**Key Learnings**
- Perplexity measures how well the model predicts text (lower = better)
- Faithfulness checks if the answer is grounded in the given context (crucial for RAG)
- Relevance checks if the answer actually helps with the user's question
- Human evaluation is still the gold standard, but automatic metrics help during development

**Challenges**
- Proper perplexity calculation requires careful loss computation
- Small models have limited evaluation reliability
- Balancing automatic metrics with real user satisfaction

**Reflection**
Evaluation is one of the most important but often neglected parts of LLM development. Good evaluation helps me understand whether my improvements (prompting, RAG, fine-tuning) are actually working.

**GitHub Commit Link** [https://github.com/Hayat373/llm-from-scratch-journey.git]