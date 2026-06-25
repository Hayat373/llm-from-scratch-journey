# Day 23 Log

**Date:** June 25, 2026

**Focus:** LLM Agents & Tool Use

**What I Did**
- Learned the concept of LLM Agents
- Built a simple agent that can use tools (search, calculator, etc.)
- Created a ReAct-style agent
- Tested agent behavior with different tasks

**Key Learnings**
- Agents are LLMs that can use external tools to solve tasks
- Tool use allows LLMs to do things they can't do alone (math, search, API calls, etc.)
- ReAct pattern (Reason + Act) is a popular way to build agents
- Small models like TinyLlama struggle with strict tool-calling format

**Challenges**
- Small models often ignore instructions and generate normal text instead of using tools
- Complex agent frameworks (LangChain) have many import and version issues
- Reliable tool use requires bigger models or very careful prompting

**Reflection**
Agents are very powerful in theory, but in practice they need good models and careful engineering. This is an advanced topic that becomes much better with stronger models (like Llama-3 or Mixtral).

**GitHub Commit Link** [https://github.com/Hayat373/llm-from-scratch-journey.git]