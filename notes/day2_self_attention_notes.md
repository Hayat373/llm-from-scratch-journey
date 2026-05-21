# Day 2 Notes - Self-Attention & Character Level Training

**Date:** May 21, 2026

## Key Concepts

### 1. Self-Attention
- **Query (Q)**: What am I looking for?
- **Key (K)**: What do I contain?
- **Value (V)**: What information should I pass?
- **Scaled Dot-Product Attention**: `softmax( (Q @ K^T) / sqrt(d_k) ) @ V`
- Multi-head attention = running multiple attention heads in parallel.

### 2. Training Setup
- **Block Size**: Maximum context length the model can attend to (e.g., 32 characters).
- **Batch Size**: Number of examples processed at once (e.g., 64).
- **Bigram Model**: Very basic baseline — only uses the previous character.

### 3. Data Preparation
- Character-level tokenization (each character is a token).
- Created `encode()` and `decode()` functions.
- Split data into train/validation.

## Challenges Faced
- Notebook setup issues in Colab (raw JSON view).
- Understanding tensor shapes (B = batch, T = time/context, C = channels/embedding).
- Slow training without GPU.

## Major Takeaways
- Transformers are powerful because of self-attention (parallelizable + long-range dependencies).
- Even a very simple model can learn patterns when trained.
- Next goal: Build a real mini-GPT with multiple layers and attention heads.

## Todo for Day 3
- Implement multi-head attention
- Add Feed-Forward layers
- Build a deeper Transformer block