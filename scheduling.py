import schedule
import time
from database import get_conn_pg, get_conn_sqlite
from pandas import json_normalize
import pandas as pd
import requests
import requests_cache 
import json


requests_cache.install_cache(expire_after = requests_cache.expiration.NEVER_EXPIRE)


def flatten_df(df):
    """
    Flattens a dataframe with nested columns.
    """
    i = 0
    while i < 100:
        columns_with_dicts = [col for col in df.columns if isinstance(df[col].iloc[0], dict)]
        columns_with_lists = [col for col in df.columns if isinstance(df[col].iloc[0], list)]
        if columns_with_dicts == [] and columns_with_lists == []:
            break
        
        # Flatten the columns with dictionaries
        for col in columns_with_dicts:
            print(col, df[col].iloc[0])
            df_col = json_normalize(df[col])
            df_col.columns = [col + '_' + str(sub_col) for sub_col in df_col.columns]
            df = pd.concat([df, df_col], axis=1)
            # df.drop(col, axis=1, inplace=True)

        # Join columns with lists
        for col in columns_with_lists:
            print(col, df[col].iloc[0])
            # df.
            df_col = df[col].apply(list_to_str)
            df = pd.concat([df, df_col], axis=1)
            # df.drop(col, axis=1, inplace=True)
        i+=1
    return df

def format_json(df):
    for col in df.columns:
        df[col] = df[col].apply(json.dumps)

    return df

def list_to_str(x):
    if len(x) == 0:
        return ""
    elif isinstance(x[0], dict):
        return x[0]
    else:
        return ", ".join(x)

def ingest_new_finn_re_ads():
    conn = get_conn_pg().connect()
    page = 1
    max_page = 1
    
    while True:
        URL = f"https://www.finn.no/api/search-qf?searchkey=SEARCH_ID_REALESTATE_HOMES&published=1&vertical=realestate&page={page}"
        print("getting data from finn")
        resp = requests.get(URL)
        if resp.ok:
            j = resp.json()
            max_page = j["metadata"]["paging"]["last"]
            df = pd.DataFrame(j["docs"])

            df = format_json(df)
  
            print("inserting data into database")
            print(df.to_sql("finn_real_estate", conn, if_exists="append", index=False))
            conn.commit()
        
        if page >= max_page:
            break

        page+=1



# def ingest_new_finn_lease_ads():
#     conn = get_conn()
#     URL = ""
#     resp = requests.get(URL)
    

#     if resp.ok:
#         df = pd.DataFrame(resp.json())
#         df.to_sql("finn_lease", conn)

if __name__ == "__main__":

    schedule.every(5).seconds.do(ingest_new_finn_re_ads)

    while True:
        schedule.run_pending()
        time.sleep(1)



    def print_hello():
        """
        Prints 'hello' to the console.
        """
        print("hello")

