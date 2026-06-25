# Day 25 Log

**Date:** June 25, 2026

**Focus:** LLM as a Judge + Advanced Evaluation Techniques

**What I Did**
- Learned how to use a stronger LLM to evaluate other models/outputs
- Implemented LLM-as-a-Judge for faithfulness, relevance, and helpfulness
- Compared self-evaluation vs external judge
- Evaluated my RAG chatbot outputs

**Key Learnings**
- LLM-as-a-Judge is a powerful and scalable way to evaluate outputs automatically
- Good judge prompts are critical for reliable scoring
- Small models (like TinyLlama) are weak judges — they tend to repeat or give inconsistent scores
- Stronger models work much better as judges

**Challenges**
- Small models struggle with strict evaluation instructions
- Judge outputs can be noisy or repetitive
- Need careful prompt engineering for consistent results

**Reflection**
LLM-as-a-Judge is very useful for fast iteration during development, but it still needs human oversight for important decisions. This is a key technique used in real LLM projects.

**GitHub Commit Link** [https://github.com/Hayat373/llm-from-scratch-journey.git]