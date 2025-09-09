# EvoAI Commerce Agent

A LangGraph-based agent that handles product assistance and order management with strict policy enforcement.

## Features

- **Product Assist**: Search products, size recommendations, ETA calculations
- **Order Help**: Secure order lookup and cancellation with 60-minute policy
- **Policy Guard**: Enforces strict cancellation rules and provides alternatives
- **Trace Logging**: Complete JSON traces for all interactions

## Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Set up environment:**
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key:
# OPENAI_API_KEY=your_key_here
```

3. **Run the main tests:**
```bash
# Mock version (no API key required)
python tests/run_tests_mock.py

# Full version (requires OpenAI API key in .env)
python -m tests.run_tests
```

4. **Run additional tests:**
```bash
# Policy unit tests
python tests/test_policy.py

# Schema validation tests  
python tests/test_schema.py
```

5. **Run all tests at once:**
```bash
python run_all_tests.py
```

6. **Try the interactive demo:**
```bash
python demo.py  # Requires OpenAI API key
```

## Project Structure

```
/src                  # agent graph + tools
  graph.py
  tools.py
/data                 # mock data
  products.json
  orders.json
/prompts              # system prompts
  system.md
/tests                # test suite
  run_tests.py
```

## Usage

The agent handles three main intents:
- `product_assist`: Product search and recommendations
- `order_help`: Order lookup and cancellation
- `other`: Guardrails and general queries

All responses include internal JSON traces with intent classification, tools called, evidence, and policy decisions.
