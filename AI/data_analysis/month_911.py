import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("data_source/911.csv")
df["timeStamp"] = pd.to_datetime(df["timeStamp"])
df.set_index("timeStamp",inplace=True)

count_by_month = df.resample("M").count()["title"]

plt.figure(figsize=(14, 6), dpi=80)

_x = count_by_month.index
_y = count_by_month.values

plt.plot(range(len(_x)),_y,color="green")

_xticks = [i.strftime("%Y-%m") for i in _x]
plt.xticks(range(len(_x)),_xticks,rotation=45)

plt.show()