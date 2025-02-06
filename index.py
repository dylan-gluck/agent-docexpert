import asyncio
import argparse
from crawl4ai import AsyncWebCrawler

async def main(url, external):
    links = []
    print(f"Starting run! Crawling {url}...")
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url)
        if result.success:
            internal_links = result.links.get("internal", [])
            external_links = result.links.get("external", [])

            print(f"Found {len(internal_links)} internal links.")
            print(f"Found {len(external_links)} external links.")

            if internal_links:
                links.extend(internal_links)
                print(f"Added {len(internal_links)} links to the list.")

            if external_links and external:
                links.extend(external_links)
                print(f"Added {len(external_links)} external links to the list.")
        else:
            print("Crawl failed:", result.error_message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, required=True, help="URL to crawl")
    parser.add_argument("--external", help="Include external links", action="store_true")
    args = parser.parse_args()
    asyncio.run(main(args.url, args.external))
