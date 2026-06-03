# Day 5 Notes - Causal Masking & Training Improvements

**Date:** jun 3, 2026

## Key Concepts Learned

### 1. Causal Masking (Most Important Today)
- Prevents the model from looking into the future during training.
- Creates a lower triangular matrix using `torch.tril()`.
- Uses `masked_fill()` to set future positions to `-inf` before softmax.
- This is what makes GPT a **decoder-only** autoregressive model.

### 2. Model Improvements
- Added `block_size` parameter to attention layer
- Used `register_buffer` to store the mask (saved with model)
- Increased model capacity slightly (`n_embd=96`, `n_layer=4`, `n_head=6`)

### 3. Training Best Practices
- Using proper causal masking
- AdamW optimizer (better than regular Adam)
- Consistent batching and context length

## Code Understanding Level
- I now understand why masking is necessary.
- I can follow the `MultiHeadAttention` forward pass better.
- Still need practice to write the masking part from memory.

## Major Takeaway
Even though the model is small, adding proper causal masking makes it behave more like real GPT models.



## Plan for Next Days
- Learn model saving/loading
- Add evaluation (perplexity)
- Start building real applications (RAG, Fine-tuning)

**Goal:** By Day 10, be comfortable modifying the full MiniGPT code myself.