# Day 7 Log

**Date:** jun 10, 2026

**Focus:** Final MiniGPT Improvements (Dropout, Scheduler, Bigger Model) + Reflection

**What I Did**
- Combined all previous concepts into a final stronger MiniGPT
- Added Dropout for regularization
- Added Learning Rate Scheduler
- Trained with bigger context and model size
- Generated text with improved settings

**Key Learnings**
- Dropout helps prevent overfitting
- Learning Rate Scheduler improves training stability
- Bigger models + longer context = noticeably better text quality
- From-scratch training is educational but computationally expensive

**Challenges**
- Training time is long on limited GPU
- Still need more practice writing full model code independently
- Model still generates somewhat repetitive text (limitation of small data + small model)

**Overall Reflection**
I now understand the full GPT-like architecture quite well: Embeddings → Positional Encoding → Multiple Transformer Blocks (with Masked Multi-Head Attention + FeedForward) → Output.

**GitHub Commit Link** [https://github.com/Hayat373/llm-from-scratch-journey.git]