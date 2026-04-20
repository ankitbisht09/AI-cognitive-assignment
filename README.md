# AI Cognitive Routing & RAG Prototype

# Overview

This project simulates a simplified cognitive loop where AI agents (personas) react to incoming content based on relevance, generate opinions, and handle arguments using contextual understanding.

Instead of broadcasting every post to all agents, I focused on selective routing using semantic similarity.

# Phase 1: Persona-Based Routing

I used vector embeddings to match incoming content with relevant personas.

Each persona is embedded once and stored in an in-memory FAISS index.  
Incoming posts are embedded and compared using distance-based similarity.

Rather than relying on exact keyword matching, this approach tries to capture semantic intent.

# Key points: 
- Lightweight embedding model (MiniLM)
- FAISS used as in-memory vector store
- Similarity score derived from L2 distance
- Threshold tuned manually after testing different inputs

# Phase 2: Content Generation Flow

Instead of directly generating posts, I simulated a simple decision pipeline:

1. Persona decides a topic (based on its traits)
2. System fetches relevant context (mocked search)
3. Bot generates an opinionated post

This loosely follows the idea behind LangGraph-style orchestration, but implemented in a simplified form.

The output is structured as JSON:
- bot_id
- topic
- post_content

# Phase 3: Context-Aware Replies (RAG Simulation)

To handle deeper conversations, I constructed replies using full thread context:
- original post
- previous comments
- latest user reply

This prevents shallow responses and helps maintain continuity.

# Prompt Injection Handling

I added a simple safeguard against malicious instructions.

If the user tries to override system behavior (e.g., "ignore instructions"),  
the bot ignores such patterns and continues responding within its persona.

This is implemented using basic rule-based filtering.


# Observations

- Semantic matching is sensitive to phrasing, not just keywords  
- Lower similarity thresholds improved recall but required balance  
- Multiple personas can match depending on tone and framing  
- Simple rule-based defenses can handle basic prompt injection attempts  

# How to Run

Install dependencies:

pip install -r requirements.txt

Run the project:

python main.py

#  Notes

This is a simplified prototype focused on demonstrating core ideas:
- semantic routing
- structured generation
- contextual reasoning

It can be extended with:
- real LLM APIs
- persistent vector databases
- advanced orchestration (LangGraph)
