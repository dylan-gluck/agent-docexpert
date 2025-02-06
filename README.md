# DocExpert

DocExpert is a collection of AI agent workflows designed to process, index and search technical documentation. It leverages Crawl4AI for web crawling, ChromaDB for local vector storage, and Langchain for semantic search capabilities.

## Overview

The project aims to make technical documentation more accessible by:
1. Crawling documentation sites to extract content
2. Creating and storing embeddings locally
3. Enabling semantic search across the indexed documentation

## Features

### Completed
- [x] Web crawling functionality using Crawl4AI
- [x] Support for both internal and external link extraction
- [x] Command line interface with URL and external link options
- [x] Async crawler implementation for improved performance

### Todo
- [ ] Generate embeddings from crawled content
- [ ] Set up ChromaDB integration for local vector storage
- [ ] Implement document chunking and preprocessing
- [ ] Add Langchain components for semantic search
- [ ] Create search API endpoints

## Installation

```bash
git clone https://github.com/dylan-gluck/agent-docexpert.git
cd agent-docexpert
```

## Usage

Run the indexer with:

```bash
# Basic usage
uv run index.py --url https://docs.example.com

# Include external links in crawl
uv run index.py --url https://docs.example.com --external
```

## Requirements

- Python ≥ 3.11
- asyncio ≥ 3.4.3
- crawl4ai ≥ 0.4.248

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
