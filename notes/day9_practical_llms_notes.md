# Day 9 Notes - Practical Modern LLMs with Hugging Face

**Date:**June 10, 2026

## Key Concepts Learned

### 1. Hugging Face Ecosystem
- `pipeline()` → Easiest way for quick tasks
- `AutoTokenizer` + `AutoModelForCausalLM` → More control
- Chat templates for structured conversations

### 2. Modern Small Models
- TinyLlama-1.1B → Good balance of speed and quality
=

### 3. Important Techniques
- Proper chat formatting using `apply_chat_template()`
- Generation parameters: `temperature`, `top_p`, `top_k`, `max_new_tokens`
- Running models on GPU with `torch_dtype=torch.float16`

## Mini Project: AI Assistant
- Built a reusable function for chatting
- Tested with different types of prompts (stories, career advice, recipes)

## My Current Level
- Can now load and use real LLMs comfortably
- Understand the practical workflow
- Still need to learn:
  - Model quantization (to run bigger models)
  - Fine-tuning
  - RAG (Retrieval Augmented Generation)

## Major Takeaway
**"Don't reinvent the wheel."**  
Understanding from scratch is good for foundation, but for real impact (jobs/hackathons), mastering pre-trained models + building applications on top is much more valuable.

**Fun Moment**: Seeing the AI Assistant actually respond meaningfully felt very satisfying.

## Next Goals
- Build more useful mini-projects
- Learn RAG
- Start fine-tuning small models