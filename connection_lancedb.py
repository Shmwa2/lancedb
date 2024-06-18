import lancedb
import pandas as pd
import pyarrow as pa
import asyncio  

# LanceDb offers both a synchronous and an asynchronous client.  There are still a
# few operations that are only supported by the synchronous client (e.g. embedding
# functions, full text search) but both APIs should soon be equivalent

# In this guide we will give examples of both clients.  In other guides we will
# typically only provide examples with one client or the other.

async def main():
    uri = "data/sample-lancedb"
    async_db = await lancedb.connect_async(uri)

# main() を非同期で実行するための処理
if __name__ == "__main__":
    asyncio.run(main())