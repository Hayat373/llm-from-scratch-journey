# Day 13 Log

**Date:** June 17, 2026

**Focus:** Model Quantization & Optimization (Making LLMs Faster)

**What I Did**
- Learned about 4-bit and 8-bit quantization
- Used bitsandbytes to run larger models efficiently
- Compared speed and quality before and after quantization
- Optimized my RAG chatbot

**Key Learnings**
- Quantization reduces model size and memory usage dramatically (4-bit is very popular)
- `BitsAndBytesConfig` with `load_in_4bit=True` makes it possible to run larger models on limited GPU
- There is a small trade-off in quality but huge gain in speed and memory
- This technique is essential for running good models on consumer hardware

**Challenges**
- Installing `bitsandbytes` sometimes needs extra setup
- Slight degradation in response quality (but often acceptable)
- Understanding when to use 4-bit vs 8-bit vs full precision

**Reflection**
Quantization is a game-changer for practical LLM usage. Now I can run better models without needing very powerful hardware.

**GitHub Commit Link** [https://github.com/Hayat373/llm-from-scratch-journey.git]