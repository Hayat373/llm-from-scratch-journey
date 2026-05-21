# Day 2 Log

**Date:** May 21, 2026

**Focus:** Self-Attention implementation + Training a small GPT-like model

**What I Did**
- [ ] Studied and implemented scaled dot-product attention
- [ ] Trained character-level model with bigger context
- [ ] Compared different block sizes

**Key Learnings**
- Self-Attention allows every token to look at all previous tokens and weigh their importance using Query, Key, and Value matrices.
- Scaled dot-product attention prevents vanishing gradients (dividing by sqrt(head_size)).
- Character-level modeling is simple but limited (vocab size is small).
- Block size = how much previous context the model can see at once.
- Training loss decreasing means the model is learning to predict the next character better.

**Challenges**
- Setting up and running notebooks smoothly in Colab (file format issues)
- Understanding the full code at first (especially shapes: B, T, C)
- Training on CPU was slow, so switched to Colab GPU
- The generated text from Bigram model is still quite random/repetitive

**Next Steps**
- Move from Bigram to a real Transformer with multiple attention heads
- Improve model architecture


**GitHub Commit Link:** [https://github.com/Hayat373/llm-from-scratch-journey.git]