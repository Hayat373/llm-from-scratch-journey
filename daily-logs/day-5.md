# Day 5 Log

**Date:** jun 3, 2026

**Focus:** Causal Masking, Better Model Architecture & Training Practices

**What I Did**
- Added causal masking (triangular mask) so the model cannot see future tokens
- Improved the MultiHeadAttention class with proper masking
- Trained a better version of MiniGPT
- Generated text using the improved model

**Key Learnings**
- Causal Masking is extremely important in decoder-only models like GPT. It ensures the model only uses past tokens to predict the next one (autoregressive property).
- Without masking, the model would "cheat" by seeing future tokens during training.
- `register_buffer` is used to save the mask as part of the model.
- LayerNorm + Residual Connections help stabilize training of deeper models.
- Training loss is decreasing more smoothly now.

**Challenges**
- Understanding tensor shapes in multi-head attention with masking
- Training still takes time even on GPU
- Generated text is better but still not very coherent (normal for small model trained from scratch)

**Next Steps**
- Start working on evaluation metrics (Perplexity)
- Save and load model weights
- Move towards practical applications

**GitHub Commit Link** [https://github.com/Hayat373/llm-from-scratch-journey.git]