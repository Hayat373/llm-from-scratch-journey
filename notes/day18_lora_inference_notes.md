# Day 18 Notes - Loading & Using Fine-tuned LoRA Model

**Date:** JUne 21, 2026

## What We Did Today
- Loaded a base model in 4-bit quantization
- Applied the LoRA adapter trained on Day 17
- Built a clean `generate_response()` function
- Tested the fine-tuned Ethiopian AI Assistant

## Key Technical Points

### 1. Loading Process
- Load base model with `BitsAndBytesConfig`
- Load adapter with `PeftModel.from_pretrained(base_model, adapter_path)`
- The adapter only adds a small number of trained weights

### 2. Advantages of This Approach
- Very memory efficient
- Easy to switch between different adapters (e.g., one for culture, one for coding, etc.)
- Fast to save and load compared to full fine-tuning

### 3. Limitations Observed
- With very small dataset, improvement is modest
- Model can still hallucinate or be repetitive
- Inference speed depends heavily on quantization and hardware

## My Current Skill Level
- Can now fine-tune small models with LoRA
- Can load and use the fine-tuned model
- Understand the full workflow from data → training → inference

## Major Takeaway
**Customization > Training from scratch.**

With LoRA, we can take a strong base model and adapt it to our specific needs (Ethiopian context, company data, personal style, etc.) efficiently.

This workflow (Quantization + LoRA + Inference) is one of the most used patterns in real LLM applications today.

## Next Goals
- Build a full RAG + Fine-tuned model application
- Learn model merging
- Deploy the fine-tuned assistant

**Personal Note:** I now have a working customized AI assistant. This feels like real progress.