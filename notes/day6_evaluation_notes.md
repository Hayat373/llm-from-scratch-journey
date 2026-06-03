# Day 6 Notes - Model Evaluation & Generation Techniques

**Date:** Jun 3, 2026

## Key Concepts Learned

### 1. Model Saving & Loading
- Use `model.state_dict()` to save only weights (efficient)
- `torch.save()` and `model.load_state_dict()` 
- Very important for deploying and continuing training

### 2. Perplexity
- Standard evaluation metric for language models
- Formula: `Perplexity = exp(average loss)`
- Lower perplexity = better model

### 3. Advanced Text Generation
- **Temperature**: Controls randomness
  - < 1.0 → More focused/repetitive
  - > 1.0 → More creative/diverse
- **Top-k Sampling**: Only sample from top k most probable tokens
- This makes generated text much better than pure greedy sampling

## Code Understanding
- I now understand causal masking + generation loop better
- I can modify temperature and top-k parameters
- Still need more practice writing the full model from scratch

## Major Takeaways
- Training from scratch on small data has clear limitations
- Good generation techniques (temperature + top-k) significantly improve output quality
- Evaluation metrics like perplexity are important for comparing models

## My Current Level
- Concepts: Good
- Coding independently: Still developing (mostly modifying given code)
- Foundation: Getting stronger

## Plan for Next Days
- Start using Hugging Face models
- Begin building real applications (RAG, Chatbot, etc.)