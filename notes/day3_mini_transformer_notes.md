# Day 3 Notes - Building a Real Transformer Block

**Date:** May 28, 2026

## What I Learned Today

### 1. Multi-Head Self-Attention
- Instead of one attention, we run **multiple attention heads** in parallel.
- Each head learns to focus on different types of relationships (syntax, meaning, etc.).
- Code breakdown:
  - `key`, `query`, `value` → Linear layers that transform input
  - Reshape to multiple heads → `(B, n_head, T, head_size)`
  - Scaled dot-product: `Q @ K^T / sqrt(head_size)`
  - Softmax to get attention weights
  - Multiply by Value

### 2. Residual Connections (`x = x + sublayer(x)`)
- Very important trick in deep networks.
- Helps gradients flow better during backpropagation.
- Prevents vanishing gradients.

### 3. LayerNorm
- Normalizes the values in each layer (mean=0, std=1).
- Makes training more stable.

### 4. FeedForward Network
- Simple MLP (Linear → ReLU → Linear) applied to each position independently.

### 5. Full Transformer Block
- Attention (for communication between tokens) + FeedForward (for thinking individually) + Residuals + LayerNorm.

## My Current Level
- I understand the high-level architecture.
- I can follow the code when explained.
- Still weak at writing it from scratch myself.

## Challenges
- Understanding tensor shape changes (especially in multi-head attention).
- Feeling overwhelmed by the full code.


## Plan to Improve
- I will explain each component in my own words.

## Next Goal
- Be able to implement a TransformerBlock with less help.