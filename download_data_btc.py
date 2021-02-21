import pandas as pd
import requests
from os import path
BASE_URL = "https://s3-eu-west-1.amazonaws.com/public.bitmex.com/data/trade/%s"
output_folder = "data"

date_from = "2020-01-10"
date_to = "2020-01-15"
dates = pd.date_range(date_from, date_to).astype(str).str.replace("-", "")

def download_trade_file(filename, output_folder):
    print(f"Downloading {filename} file")
    url = BASE_URL % filename
    resp = requests.get(url)
    if resp.status_code != 200:
        print(f"Cannot download the {filename} file. Status code: {resp.status_code}")
        return
    with open(path.join(output_folder, filename), "wb") as f:
        f.write(resp.content)
    print(f"{filename} downloaded")

def download_trade_files(date_start,date_end):
    dates = pd.date_range(date_start, date_end).astype(str).str.replace("-", "")
    for date in dates:
        filename = date + ".csv.gz"
        download_trade_file(filename, output_folder)
    return
