# Day 15 Log

**Date:** June 20, 2026

**Focus:** Adding Conversation Memory + Building Better Chatbot

**What I Did**
- Learned how to add memory to LangChain chains
- Built a chatbot that remembers previous conversation
- Improved the Ethiopian AI Assistant with memory
- Tested multi-turn conversations

*Key Learnings**
- Conversation memory allows the LLM to remember previous messages in the chat
- `ConversationBufferMemory` stores the full conversation history
- `ConversationChain` makes it easy to maintain context across multiple turns
- Memory is essential for building real chat applications (otherwise each message is independent)

**Challenges**
- Memory can make prompts very long (context window limit)
- Responses can become slower as history grows
- Combining RAG + Memory is powerful but needs careful design

**Reflection**
Adding memory made the chatbot feel much more natural and intelligent. This is a key feature that separates basic demos from real applications.

**GitHub Commit Link** [https://github.com/Hayat373/llm-from-scratch-journey.git]