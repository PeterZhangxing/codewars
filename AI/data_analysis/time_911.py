import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


csv_file_path = "data_source/911.csv"
df = pd.read_csv(csv_file_path)

df["timeStamp"] = pd.to_datetime(df["timeStamp"])
df.set_index("timeStamp",inplace=True)

call_by_month = df.resample("m").count()["title"]
# print(call_by_month)

_x = call_by_month.index
_y = call_by_month.values
_x = [ i.strftime("%Y-%m") for i in _x ]

plt.figure(figsize=(12,5),dpi=80)

plt.plot(range(len(_x)),_y,color="r")
plt.xticks(range(len(_x)),_x,rotation=-45)
# plt.grid(axis="y",alpha=0.5)

plt.show()