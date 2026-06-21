# Day 18 Log

**Date:** JUne 21, 2026

**Focus:** Merging LoRA Adapter + Inference with Fine-tuned Model

**What I Did**
- Loaded the LoRA adapter from Day 17
- Merged adapter with base model
- Tested the fine-tuned model
- Built an improved Ethiopian AI Assistant using the fine-tuned model

**Key Learnings**
- LoRA adapters can be easily loaded on top of the base model using `PeftModel.from_pretrained()`
- Fine-tuned models respond better on domain-specific topics (e.g., Ethiopian culture, history, food)
- 4-bit quantization + LoRA is a very practical combination for limited hardware
- Saving and loading adapters is much faster than saving the full model

**Challenges**
- Adapter folder sometimes disappears after Colab session resets
- Fine-tuning still takes time even with LoRA
- Small fine-tuning dataset gives limited improvement

**Reflection**
Today I completed the full cycle: understanding → building from scratch → fine-tuning → using the customized model. This is a solid foundation for real projects.

**GitHub Commit Link** [https://github.com/Hayat373/llm-from-scratch-journey.git]