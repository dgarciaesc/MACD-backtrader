import glob
import pandas as pd
from os import path
BASE_URL = "https://s3-eu-west-1.amazonaws.com/public.bitmex.com/data/trade/%s"
output_folder = "data"

date_from = "2020-01-13"
date_to = "2020-01-15"
dates = pd.date_range(date_from, date_to).astype(str).str.replace("-", "")
filepaths = glob.glob(path.join(output_folder, "*.csv.gz"))
filepaths = sorted(filepaths)
filepaths

df_list = []

for filepath in filepaths:
    print(f"Reading {filepath}")
    df_ = pd.read_csv(filepath)
    df_ = df_[df_.symbol == "XBTUSD"]
    print(f"Read {df_.shape[0]} rows")
    df_list.append(df_)
df = pd.concat(df_list)
df_list = None

df.loc[:, "Datetime"] = pd.to_datetime(df.timestamp.str.replace("D", "T"))
df.drop("timestamp", axis=1, inplace=True)

df = df.groupby(pd.Grouper(key="Datetime", freq="1Min")).agg(
    {"price": ["first", "max", "min", "last"], "foreignNotional": "sum"}
)
df.columns = ["Open", "High", "Low", "Close", "Volume"]
df.loc[:, "OpenInterest"] = 0.0 # required by backtrader
df = df[df.Close.notnull()]
#df.reset_index(inplace=True)

dataset_filename = path.join(output_folder, f"XBT_USD_{date_from}_{date_to}.csv")
df.to_csv(dataset_filename)