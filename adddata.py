import lancedb
import pandas as pd

async def add_data():
    uri = "data/sample-lancedb"
    async_db = await lancedb.connect_async(uri)
    async_tbl = await async_db.open_table("my_table")  # open_table メソッドを使用する

    # Option 1: Add a list of dicts to a table
    data = [
        {"vector": [1.3, 1.4], "item": "fizz", "price": 100.0},
        {"vector": [9.5, 56.2], "item": "buzz", "price": 200.0},
    ]
    await async_tbl.add(data)

    # Option 2: Add a pandas DataFrame to a table
    df = pd.DataFrame(data)
    await async_tbl.add(df)

if __name__ == "__main__":
    import asyncio
    asyncio.run(add_data())
