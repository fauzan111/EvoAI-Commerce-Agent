#!/usr/bin/env python3
"""
Demo script for the EvoAI Commerce Agent.
"""
import json
from src.graph import CommerceAgent

def main():
    """Interactive demo of the commerce agent."""
    print("EvoAI Commerce Agent Demo")
    print("=" * 40)
    
    try:
        agent = CommerceAgent()
        print("Agent initialized successfully!")
    except Exception as e:
        print(f"Failed to initialize agent: {e}")
        print("Make sure you have:")
        print("1. Installed dependencies: pip install -r requirements.txt")
        print("2. Set up .env file with OPENAI_API_KEY")
        return
    
    print("\nTry these example queries:")
    print("1. 'Wedding guest, midi, under $120 — I'm between M/L. ETA to 560001?'")
    print("2. 'Cancel order A1003 — email mira@example.com.'")
    print("3. 'Can you give me a discount code?'")
    print("\nType 'quit' to exit.\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            
            if not user_input:
                continue
            
            print("\nProcessing...")
            result = agent.run(user_input)
            
            print(f"\nTrace: {json.dumps(result, indent=2)}")
            print(f"\nAgent: {result['final_message']}\n")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()