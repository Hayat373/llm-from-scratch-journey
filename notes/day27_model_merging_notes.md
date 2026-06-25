# Day 27 Notes - Model Merging

**Date:** June, 2026

## What is Model Merging?

Combining the weights of multiple models (or adapters) into a single stronger model.

### Why Model Merging is Powerful
- Combine strengths of different fine-tunes (e.g., one good at culture, another at coding)
- Create specialized models without expensive full training
- Often outperforms individual models
- Very popular in open-source LLM community

## Popular Merging Methods

1. **SLERP** (Spherical Linear Interpolation) — Smooth blending
2. **Task Arithmetic** — Simple weighted average of weights
3. **DARE** (Drop And REscale) — Drops some parameters and rescales
4. **Model Soup** — Average of multiple fine-tuned models

## My Current Understanding
- Good conceptual knowledge of why merging works
- Understand basic idea of combining adapters
- Still need hands-on practice with tools like `mergekit`

## Major Takeaway
**"Don't always train new models. Sometimes merging existing ones is smarter and cheaper."**

This technique is especially useful for creating domain-specific models (e.g., Ethiopian legal AI, medical AI, education AI, etc.).

## Next Phase Plan
- Finish core learning by Day 30
- Start building clean portfolio projects from Day 31


**Personal Reflection (End of Week 4)**
I have covered:
- Transformers from scratch
- Hugging Face & practical usage
- RAG, Agents, LoRA, Quantization, Evaluation, Deployment
- Multi-agent systems

I now have a solid foundation. Time to shift more focus toward building impressive portfolio projects.

