# Day 26 Notes - Multi-Agent Systems

**Date:** June 25, 2026

## What are Multi-Agent Systems?

Instead of using **one LLM** to do everything, we use **multiple specialized agents** that work together like a team.

### Common Agent Roles
- **Researcher Agent**: Gathers information and facts
- **Writer Agent**: Turns research into clear, well-structured output
- **Critic Agent**: Reviews and improves the output
- **Planner Agent**: Breaks down complex tasks into steps
- **Executor Agent**: Performs specific actions (search, code, API calls)

## Why Multi-Agent Systems Are Powerful
- Each agent can focus on its strength
- Better reasoning and quality on complex tasks
- More modular and easier to debug
- Closer to how human teams work

## Simple Architecture I Built Today
```
User Query
↓
Researcher Agent → gathers info
↓
Writer Agent → creates final response
↓
Final Answer
```

## My Current Understanding
- Good conceptual grasp of multi-agent design
- Can implement basic two-agent workflows
- Still need practice on:
  - Better coordination between agents
  - Using stronger models for agents
  - Building more complex systems (Planner → Researcher → Critic → Writer)

## Major Takeaway
**"One LLM is smart. Multiple specialized agents working together are much smarter."**

Multi-agent systems are currently one of the most exciting and effective ways to get high-quality results from LLMs.

## Next Goals
- Build a more complete multi-agent system (3+ agents)
- Add tools to agents
- Use it for real tasks (research assistant, content creator, job application helper)

**Personal Note:** Day 26 opened my eyes to how powerful agent collaboration can be. This is definitely something I want to explore more for portfolio projects.