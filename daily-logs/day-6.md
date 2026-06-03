# Day 6 Log

**Date:** Jun 3, 2026

**Focus:** Model Saving/Loading, Perplexity Evaluation & Advanced Text Generation

**What I Did**
- Added model saving and loading using `torch.save()` and `state_dict`
- Implemented Perplexity as an evaluation metric
- Added advanced text generation with temperature and top-k sampling
- Trained the model with causal masking

**Key Learnings**
- `torch.save(model.state_dict(), 'model.pth')` is the standard way to save models
- Perplexity = exp(loss) → Lower is better. It tells how "surprised" the model is by the text.
- Temperature controls creativity (low = more deterministic, high = more random)
- Top-k sampling prevents the model from choosing very rare tokens
- Saving/loading models is essential for real projects

**Challenges**
- Understanding how  top-k affect output quality
- Calculating proper validation loss/perplexity
- Training time is still noticeable even on GPU

**Next Steps**
- Start building practical applications
- Move toward fine-tuning real models (Hugging Face)


**GitHub Commit Link** [https://github.com/Hayat373/llm-from-scratch-journey.git]