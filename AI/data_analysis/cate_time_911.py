import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


csv_file_path = "data_source/911.csv"
df = pd.read_csv(csv_file_path)

tmp_li = df["title"].str.split(": ").tolist()
df["cate"] = pd.DataFrame(np.array([ i[0] for i in tmp_li]).reshape((df.shape[0],1)))

df["timeStamp"] = pd.to_datetime(df["timeStamp"])
df.set_index(["timeStamp"],inplace=True)

plt.figure(figsize=(12, 5), dpi=80)

for cate_name,cate_data in df.groupby(by="cate"):
    call_by_month = cate_data.resample("m").count()["title"]

    _x = call_by_month.index
    _x = [ i.strftime("%Y-%m") for i in _x ]

    _y = call_by_month.values

    plt.plot(range(len(_x)), _y, label=cate_name)

plt.xticks(range(len(_x)), _x, rotation=-45)
plt.grid(axis="y",alpha=0.5)

plt.legend(loc="upper right")

plt.show()