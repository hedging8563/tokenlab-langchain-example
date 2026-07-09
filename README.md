# TokenLab LangChain Example

[![CI](https://github.com/hedging8563/tokenlab-langchain-example/actions/workflows/ci.yml/badge.svg)](https://github.com/hedging8563/tokenlab-langchain-example/actions/workflows/ci.yml)

Minimal LangChain Python example using TokenLab as an OpenAI-compatible endpoint.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
export TOKENLAB_API_KEY=sk-your-tokenlab-key
python main.py
```

## Links

- TokenLab docs: https://docs.tokenlab.sh
- LangChain integration docs: https://docs.tokenlab.sh/integrations/langchain
- Model catalog: https://api.tokenlab.sh/v1/models
