# DocExpert

DocExpert is a collection of AI agent workflows designed to process, index and search technical documentation. It leverages [Crawl4AI](https://github.com/unclecode/crawl4ai) for web crawling, [ChromaDB](https://github.com/chroma-core/chroma) for local vector storage, and [Langchain](https://github.com/langchain-ai/langchain) for semantic search capabilities.

## Overview

The project aims to make technical documentation more accessible by:
1. Crawling documentation sites to extract content
2. Creating and storing embeddings locally
3. Enabling semantic search across the indexed documentation

<details>
    <summary>🧜‍♀️ Workflow Diagram</summary>

    ```mermaid
        flowchart TD
            A[Start] --> B[CLI Input]
            B -->|--url parameter| C[Initial URL Scraping]
            C --> D[Extract Initial Links]
            D --> E{External Links?}
            E -->|--external flag| F[Include External URLs]
            E -->|no flag| G[Filter Internal URLs]
            F --> H[Batch Crawling]
            G --> H
            H --> I[HTML Processing]
            I --> J[Text Extraction]
            J --> K[Text Chunking]
            K --> L[Generate Embeddings]
            L --> M[(ChromaDB Vector Storage)]
            M --> N{Search Request}
            N -->|Planned| O[Langchain RAG]
            O --> P[Search Results]
            P --> Q[End]

            style O stroke-dasharray: 5 5
            style P stroke-dasharray: 5 5
    ```
</details>

## Features

### Completed
- [x] Project setup using uv
- [x] CLI argument parsing
- [x] Scrape initial `links[]`
- [x] Set up ChromaDB integration for local vector storage
- [x] Batch-crawl `links[]`
- [x] Extract/chunk/embed text from HTML

### Todo (Indexer)
- [ ] Optimize metadata extraction
- [ ] Optimize URL filtering (remove #hashes, etc.)
- [ ] Add recursive crawling

### Todo (RAG)
- [ ] Add Langchain integration for RAG search
- [ ] Create search API endpoints

---

## Usage

Dependencies: [uv](https://docs.astral.sh/uv/getting-started/installation/)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

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
