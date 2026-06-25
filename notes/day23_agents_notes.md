# Day 23 Notes - LLM Agents & Tool Use

**Date:** June 25, 2026

## What are LLM Agents?

An **Agent** is an LLM that can:
- Reason about a task
- Decide when to use external tools
- Call tools (Calculator, Search, API, Database, etc.)
- Use the tool results to give better answers

## Popular Agent Patterns

1. **ReAct** (Reason + Act) — Most common
   - Think → Decide tool → Use tool → Observe result → Think again → Final Answer

2. **Tool Calling** — Modern models (Llama-3, GPT-4, etc.) can call tools natively

## Tools Used Today
- **Calculator Tool**: Allows the model to do accurate math

## Why Agents Are Important
- Overcomes LLM limitations (no real-time knowledge, bad at math, can't browse web)
- Enables building autonomous AI systems
- Very useful for real applications (research assistant, personal AI, automation)

## My Current Understanding
- Good conceptual understanding of what agents are
- Can create simple tools
- Still difficult to make reliable agents with small models like TinyLlama
- Need bigger models or better prompting techniques for good performance

## Challenges Faced
- Model not following tool format properly
- Frequent import errors due to LangChain version changes
- Small models have weak instruction following ability

## Major Takeaway
**Agents = LLM + Tools + Reasoning Loop**

This combination is one of the most exciting areas in current LLM development. Even though small models struggle, the architecture is very powerful when using stronger models.

## Next Goals
- Learn better prompting for agents
- Try bigger models for agent behavior
- Build a useful agent (e.g., Research Agent, Job Application Helper)

**Personal Note:** Day 23 showed me both the potential and current limitations of agents. This is an advanced topic that becomes much better with stronger models.