# Day 4 Notes - Improving MiniGPT & Hyperparameters

**Date:** May 30, 2026

## Main Improvements Made

1. **Bigger Model**
   - `n_embd`: 64 → 128 (bigger embedding vectors)
   - `n_head`: 4 → 8
   - `n_layer`: 3 → 6 (more transformer blocks)
   - `block_size`: 32 → 64 (longer context)

2. **Better Training**
   - Used AdamW optimizer
   - Trained for more steps

## What Each Hyperparameter Does

- **n_embd**: Size of the vector representing each token. Bigger = more capacity to learn patterns.
- **n_head**: Number of parallel attention mechanisms. Helps model learn different relationships.
- **n_layer**: Number of Transformer blocks stacked. Deeper model = more complex reasoning (but harder to train).
- **block_size**: How many previous tokens the model can attend to.

## Key Takeaways

- Scaling up the model improves output quality noticeably compared to Day 3.
- Even small models can learn basic Shakespeare-style language.
- The architecture (Multi-Head Attention + FeedForward + Residuals) is the real power.
- Training from scratch on a small dataset has limits — this is why real LLMs use massive data + pre-training.

## My Current Weakness
- I understand the concepts quite well now.
- But I am still weak at writing the full code myself (mostly copy-pasting and modifying).
- I need to practice rewriting classes like `MultiHeadAttention` and `TransformerBlock` from memory.

## Plan Moving Forward
- Spend more time typing code manually instead of pasting
- Try to break and fix the code intentionally to learn
- Start combining this knowledge with practical tools (Hugging Face, RAG, etc.)

## Goal for Next Week
Be able to build a basic Transformer model with minimal guidance.