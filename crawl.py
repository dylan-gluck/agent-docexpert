import asyncio
import argparse
import chromadb
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, MemoryAdaptiveDispatcher, CrawlerMonitor, DisplayMode

def check_db(collection):
    print(f"Collection has {collection.count()} documents.")

def add_to_collection(result, collection):
    print(f"Indexing {result.url}..")
    collection.add(
        documents=[result.markdown],
        ids=[result.url]
    )

async def crawl_batch(urls, collection):
    browser_config = BrowserConfig(headless=True, verbose=False)
    run_config = CrawlerRunConfig(stream=True)
    dispatcher = MemoryAdaptiveDispatcher(
        memory_threshold_percent=70.0,
        check_interval=1.0,
        max_session_permit=10,
        monitor=CrawlerMonitor(
            display_mode=DisplayMode.DETAILED
        )
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        async for result in await crawler.arun_many(
            urls=urls,
            config=run_config,
            dispatcher=dispatcher
        ):
            if result.success:
                add_to_collection(result, collection)

async def crawl(url):
    browser_config = BrowserConfig(headless=True, verbose=False)

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url)
        return result

async def get_links(result, external=False):
    urls = []

    if result.success:
        internal_links = result.links.get("internal", [])
        external_links = result.links.get("external", [])

        print(f"Found {len(internal_links)} internal links.")
        print(f"Found {len(external_links)} external links.")

        if internal_links:
            for link in internal_links:
                href = link.get("href")
                if href not in urls:
                    urls.append(href)
            print(f"Added {len(internal_links)} links to the list.")

        if external_links and external:
            for link in external_links:
                href = link.get("href")
                if href not in urls:
                    urls.append(href)
            print(f"Added {len(external_links)} external links to the list.")

        return urls
    else:
        print("Crawl failed:", result.error_message)
        return urls

async def main(args):
    # Parse the arguments
    url = args.url
    c = args.collection
    etx = args.external

    # Initialize the database
    client = chromadb.PersistentClient()
    collection = client.get_or_create_collection(name=c)
    check_db(collection)

    # Crawl the starting URL
    print(f"Starting run! Crawling {url}...")
    result = await crawl(url)
    urls = await get_links(result, etx)

    # Batch Crawl the links found on the starting URL
    await crawl_batch(urls, collection)

    # exit
    print(f"Run complete! Crawled {len(urls)} links.")
    check_db(collection)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, required=True, help="url to crawl")
    parser.add_argument("--collection", type=str, help="chromadb collection id", default="docexpert")
    parser.add_argument("--external", help="include external links", action="store_true")
    args = parser.parse_args()
    asyncio.run(main(args))
