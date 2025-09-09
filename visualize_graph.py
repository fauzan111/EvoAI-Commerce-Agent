#!/usr/bin/env python3
"""
Simple ASCII visualization of the LangGraph structure.
"""

def print_graph():
    """Print ASCII representation of the agent graph."""
    graph = """
EvoAI Commerce Agent - Graph Structure
=====================================

    [User Input]
         |
         v
    ┌─────────┐
    │ Router  │ ──── Classifies intent: product_assist | order_help | other
    └─────────┘
         |
         v
    ┌─────────────┐
    │ Tool        │ ──── Selects and executes tools based on intent
    │ Selector    │      • product_search, size_recommender, eta
    └─────────────┘      • order_lookup, order_cancel
         |
         v
    ┌─────────────┐
    │ Policy      │ ──── Enforces 60-minute cancellation rule
    │ Guard       │      Handles guardrails and refusals
    └─────────────┘
         |
         v
    ┌─────────────┐
    │ Responder   │ ──── Generates final response + JSON trace
    └─────────────┘
         |
         v
    [JSON Trace + Final Message]

Node Details:
=============

Router:
  - Input: User message
  - Output: Intent classification (product_assist/order_help/other)
  - Logic: LLM-based classification

Tool Selector:
  - Input: Intent + user message
  - Output: Tool results and evidence
  - Tools Available:
    * product_search(query, price_max, tags)
    * size_recommender(user_inputs)
    * eta(zip_code)
    * order_lookup(order_id, email)
    * order_cancel(order_id, timestamp)

Policy Guard:
  - Input: Intent + evidence
  - Output: Policy decisions
  - Rules:
    * 60-minute cancellation window
    * Discount code refusals
    * Alternative suggestions

Responder:
  - Input: All previous state
  - Output: Structured JSON trace + user-friendly message
  - Format: {intent, tools_called, evidence, policy_decision, final_message}

Flow Examples:
==============

Product Assist Flow:
User → Router → Tool Selector → Policy Guard → Responder
       (product_assist) → (search+size+eta) → (no policy) → (recommendations)

Order Help Flow:
User → Router → Tool Selector → Policy Guard → Responder  
       (order_help) → (lookup+cancel) → (60min check) → (success/blocked)

Guardrail Flow:
User → Router → Tool Selector → Policy Guard → Responder
       (other) → (no tools) → (refuse+alternatives) → (helpful response)
"""
    
    print(graph)

if __name__ == "__main__":
    print_graph()