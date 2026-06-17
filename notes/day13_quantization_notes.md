# Day 13 Notes - Model Quantization & Optimization

**Date:** June 17, 2026

## Key Concepts Learned

### What is Quantization?
- Reducing the precision of model weights (from 16-bit to 4-bit or 8-bit)
- Goal: Lower memory usage + faster inference with minimal quality loss

### Popular Techniques
- **4-bit Quantization** (NF4 + Double Quant) → Best balance right now
- **8-bit Quantization** → Better quality than 4-bit
- `bitsandbytes` library makes this very easy in Hugging Face

### Benefits
- Run larger models on smaller GPUs
- Faster loading and generation
- Lower VRAM usage
- Possible to run on free Colab GPU

### Trade-offs
- Slight drop in response quality
- Sometimes needs careful configuration (`bnb_4bit_compute_dtype=torch.float16`)

## Tools Used
- `BitsAndBytesConfig`
- `load_in_4bit=True`
- `device_map="auto"`

## My Current Understanding
- Good grasp of why quantization is needed
- Can now load and run models more efficiently
- Still need to learn advanced optimization (vLLM, llama.cpp, AWQ, GPTQ)

## Major Takeaway
**"Bigger model ≠ better experience if it's too slow."**  
Quantization allows us to get the best performance out of limited hardware.

## Next Goals
- Use quantized models in my RAG chatbot
- Learn deployment on Hugging Face Spaces
- Build more complete portfolio projects

**Personal Note:** This was a very practical and useful day.