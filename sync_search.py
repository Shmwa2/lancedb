import lancedb
import pandas as pd

def sync_search():
    uri = "data/sample-lancedb"
    db = lancedb.connect(uri)
    tbl = db.open_table("my_table")

    # 検索条件を指定してクエリを実行し、データフレームを取得する
    result_df = tbl.search([100, 100]).limit(2).to_pandas()
    print(result_df)

if __name__ == "__main__":
    sync_search()

