import asyncio
import argparse
import chromadb

async def main(args):
    # Parse the arguments
    c = args.collection
    limit = args.limit

    # Initialize the database
    client = chromadb.PersistentClient()
    collection = client.get_or_create_collection(name=c)

    print(f"Querying the {c} collection for {limit} results...")

    # Query the database
    res: chromadb.GetResult = collection.get(limit=limit)

    documents = res.get("documents", []) or []

    print(f"Found {len(documents)} documents.")

    print("Done, exiting...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--collection", type=str, help="chromadb collection id", default="docexpert")
    parser.add_argument("--limit", type=int, help="limit results", default=5)
    args = parser.parse_args()
    asyncio.run(main(args))
