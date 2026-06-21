# Day 17 Log

**Date:** June 20, 2026

**Focus:** Fine-tuning with LoRA (PEFT)

**What I Did**
- Learned LoRA (Low-Rank Adaptation)
- Set up 4-bit quantization + LoRA fine-tuning on TinyLlama
- Created a small custom dataset and fine-tuned the model
- Saved the LoRA adapter

**Key Learnings**
- LoRA allows us to fine-tune large models by training only a small number of parameters (very efficient)
- `bitsandbytes` + `peft` makes fine-tuning possible even on limited hardware
- Only a tiny percentage of parameters (~0.1-1%) are trained with LoRA
- Fine-tuning on domain-specific data (e.g., Ethiopian knowledge) improves the model's responses on that topic

**Challenges**
- Debugging dataset formatting and padding issues
- Training is still slow even with LoRA
- Need to learn proper evaluation of fine-tuned models

**Reflection**
This was a very important day. I now understand one of the most valuable real-world skills in the LLM field — efficient fine-tuning.


**GitHub Commit Link** [https://github.com/Hayat373/llm-from-scratch-journey.git]