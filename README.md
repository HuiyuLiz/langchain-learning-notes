# LangChain Learning Notes

A repository containing learning notes, examples, and experiments with LangChain - a framework for building applications with Large Language Models (LLMs). This is learning notes from YouTube LangChain tutorials.

## Overview

This repository serves as a personal learning space for exploring LangChain capabilities, including:
- Building LLM-powered applications
- Working with vector stores (ChromaDB)
- Integrating with various LLM providers (DeepSeek, Ollama)
- Creating chains and agents
- Document processing and retrieval

## Requirements

- Python >= 3.11

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd langchain-learning-notes
```

2. Install dependencies using `uv`:
```bash
uv sync
```

The `uv sync` command will automatically:
- Create a virtual environment (if it doesn't exist)
- Install all dependencies listed in `pyproject.toml`
- Lock the dependencies in `uv.lock`

Alternatively, using pip:
```bash
pip install -e .
```

## Dependencies

- `langchain` - Core LangChain framework
- `chromadb` - Vector database for embeddings
- `langchain-chroma` - LangChain integration for ChromaDB
- `langchain-deepseek` - LangChain integration for DeepSeek models
- `langchain-ollama` - LangChain integration for Ollama

## Usage

Run the main script:
```bash
python main.py
```

## Project Structure

```
.
├── README.md          # This file
├── main.py            # Main entry point
├── pyproject.toml     # Project configuration and dependencies
└── uv.lock           # Dependency lock file
```

## Learning Resources

This repository contains practical examples and notes from learning LangChain. Feel free to explore the code and experiment with different LangChain features.

## License

This is a personal learning repository.
