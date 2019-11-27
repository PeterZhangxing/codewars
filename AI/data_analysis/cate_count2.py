import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("data_source/911.csv")

tmp_li = df["title"].str.split(": ").tolist()
cate_li = list(set([i[0] for i in tmp_li]))

tmp_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_li))),columns=cate_li)

for i in cate_li:
    tmp_df[i][df["title"].str.contains(i)] = 1

cate_count = tmp_df.sum(axis=0)

plt.figure(figsize=(7, 6), dpi=80)

_x = cate_count.index
_y = cate_count.values

plt.bar(range(len(_x)),_y,width=0.5)
plt.xticks(range(len(_x)),_x)

plt.show()