import asyncio
import lancedb
import pandas as pd
import pyarrow as pa

async def main():
    uri = "data/sample-lancedb"
    async_db = await lancedb.connect_async(uri)

    data = [
        {"vector": [3.1, 4.1], "item": "foo", "price": 10.0},
        {"vector": [5.9, 26.5], "item": "bar", "price": 20.0},
    ]

    # Asynchronous client: create table
    async_tbl = await async_db.create_table("my_table", data=data)
    print("Table created asynchronously:", async_tbl)

if __name__ == "__main__":
    asyncio.run(main())