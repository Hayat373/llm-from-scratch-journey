# Day 17 Notes - LoRA Fine-Tuning (PEFT)

**Date:** June 20, 2026

## What is LoRA?
- **Low-Rank Adaptation**
- A technique to fine-tune large models without updating all parameters
- Instead of training billions of parameters, we train small "adapter" matrices

## Why LoRA is Popular
- Much lower memory usage
- Faster training
- Easy to merge / switch adapters
- Can fine-tune on consumer GPUs

## Key Components Used Today

1. **4-bit Quantization** (`BitsAndBytesConfig`)
   - Reduces model size dramatically

2. **LoRA Config**
   - `r` = rank (how much new information to learn)
   - `target_modules` = which layers to adapt (usually attention layers)
   - `lora_alpha`, `lora_dropout`

3. **PEFT Library**
   - `get_peft_model()` adds the adapters

## Training Setup
- Small custom dataset (Question-Answer pairs)
- `DataCollatorForLanguageModeling`
- `TrainingArguments` with `adamw_8bit`

## My Current Understanding
- Good conceptual understanding of why and how LoRA works
- Can set up basic fine-tuning pipeline
- Still need more practice on:
  - Creating high-quality datasets
  - Hyperparameter tuning
  - Merging adapters
  - Proper evaluation

## Major Takeaway
**You don’t need to train the whole model.**  
With LoRA + Quantization, you can adapt powerful models to your own domain (Ethiopian culture, local laws, your company data, etc.) very efficiently.

This skill is highly valued for jobs and hackathons.

## Next Goals
- Merge LoRA adapter with base model
- Inference with fine-tuned model
- Build a RAG + Fine-tuned model application

**Personal Note:** After Day 17, I feel much closer to being able to build real customized AI applications.