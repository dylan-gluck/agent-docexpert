import asyncio
import argparse
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, MemoryAdaptiveDispatcher, CrawlerMonitor, DisplayMode

async def crawl_batch(urls):
    browser_config = BrowserConfig(headless=True, verbose=False)

    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        stream=True  # Enable streaming mode
    )

    dispatcher = MemoryAdaptiveDispatcher(
        memory_threshold_percent=70.0,
        check_interval=1.0,
        max_session_permit=10,
        monitor=CrawlerMonitor(
            display_mode=DisplayMode.DETAILED
        )
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        # Process results as they become available
        async for result in await crawler.arun_many(
            urls=urls,
            config=run_config,
            dispatcher=dispatcher
        ):
            if result.success:
                # Process each result immediately
                print(f"Successfully crawled {result.url}")
            else:
                print(f"Failed to crawl {result.url}: {result.error_message}")


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
                for link in internal_links:
                    href = link.get("href")
                    if href not in links:
                        links.append(href)
                print(f"Added {len(internal_links)} links to the list.")

            if external_links and external:
                for link in external_links:
                    href = link.get("href")
                    if href not in links:
                        links.append(href)
                print(f"Added {len(external_links)} external links to the list.")

            await crawl_batch([links[0], links[1]])

        else:
            print("Crawl failed:", result.error_message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, required=True, help="URL to crawl")
    parser.add_argument("--external", help="Include external links", action="store_true")
    args = parser.parse_args()
    asyncio.run(main(args.url, args.external))
