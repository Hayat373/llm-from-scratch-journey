# Day 1 Notes - Transformers & nanoGPT

**Date:** May 21, 2026

## Key Concepts Learned

### 1. Tokenization
- Character-level : Every single character is a token.
- Subword (BPE - used in GPT-2): Most common method today. Balances vocabulary size and meaning.
- Word-level / Sentence-level: Less common for modern LLMs.

### 2. Language Modeling Objective
- Predict the next token given all previous tokens.
- This is called **autoregressive** modeling (GPT style).

### 3. Bigram Model (Baseline)
- Very simple: Only looks at the previous 1 token to predict the next.
- Poor at long-range dependencies.

### 4. Self-Attention (The Core of Transformers)
- Allows the model to look at **all previous tokens** at once and decide which ones are important.
- Computes attention scores (how relevant each token is to the current one).
- Scaled Dot-Product Attention + Multi-Head Attention.

### 5. Why Positional Encoding?
- Attention itself has no sense of order.
- Positional encoding adds information about the position of tokens so the model knows sequence order.

### 6. Encoder vs Decoder
- **Encoder**: Good for understanding (e.g., BERT) - bidirectional.
- **Decoder**: Good for generation (e.g., GPT) - unidirectional (only looks left to right).
- Full Transformer (Encoder + Decoder): Used in translation (T5, etc.).

## Architecture Understanding
I understand the high-level architecture:
- Embeddings → Positional Encoding → Multiple Transformer Blocks (Self-Attention + Feed Forward) → Output Layer

## Questions / Confusing Parts
- The actual code implementation of self-attention and training loop still feels overwhelming.
- Need more practice to implement it myself.

## Validation vs Test Set
- Validation set → Used during training for hyperparameter tuning and early stopping.
- Test set → Only used after final model is trained for unbiased evaluation.

## Next Goals
- Understand and implement simple self-attention from scratch.
- Train a small character-level model properly.