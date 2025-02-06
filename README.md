# DocExpert

DocExpert is a collection of AI agent workflows designed to process, index and search technical documentation. It leverages [Crawl4AI](https://github.com/unclecode/crawl4ai) for web crawling, [ChromaDB](https://github.com/chroma-core/chroma) for local vector storage, and [Langchain](https://github.com/langchain-ai/langchain) for semantic search capabilities.

## Overview

The project aims to make technical documentation more accessible by:
1. Crawling documentation sites to extract content
2. Creating and storing embeddings locally
3. Enabling semantic search across the indexed documentation

## Features

### Completed
- [x] Project setup using uv
- [x] CLI argument parsing
- [x] Scrape initial `links[]`

### Todo (Indexer)
- [ ] Set up ChromaDB integration for local vector storage
- [ ] Batch-crawl `links[]`
- [ ] Extract/chunk/embed text from HTML

### Todo (Search)
- [ ] Add Langchain integration for semantic search
- [ ] Create search API endpoints

---

## Usage

Pull latest:

```bash
git clone https://github.com/dylan-gluck/agent-docexpert.git
cd agent-docexpert
```

Run the indexer with:

```bash
# Basic usage
uv run index.py --url https://docs.example.com

# Include external links in crawl
uv run index.py --url https://docs.example.com --external
```

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU GPLv3 License - see the LICENSE file for details.
