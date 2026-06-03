# Day 4 Log

**Date:** May 30, 2026

**Focus:** Improving MiniGPT + Running Experiments

**What I Did**
- Improved the MiniGPT model with bigger embedding size, more heads, and more layers
- Increased context length (block_size)
- Trained the model and generated longer text
- Compared results with Day 3 model

**Key Learnings**
- Increasing model size (n_embd, n_layer, n_head) generally improves text quality
- Larger block_size allows the model to remember longer context
- Training deeper models is slower and needs more compute (GPU helps a lot)
- Residual connections and LayerNorm are crucial for training deeper models
- Even with improvements, the model still generates somewhat repetitive or imperfect text because it's small and trained on limited data

**Challenges**
- Training takes longer with bigger models
- Still mostly copy-pasting code, not writing it from scratch
- Understanding how changing each hyperparameter affects the output
- Model still not very coherent (expected at this stage)

**Next Steps**
- Focus more on understanding and modifying code myself
- Move towards RAG and practical applications
- Try fine-tuning a real small LLM (like Phi-3 or Gemma)

**GitHub Commit Link** [https://github.com/Hayat373/llm-from-scratch-journey.git]