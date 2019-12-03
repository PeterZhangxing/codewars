import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("data_source/911.csv")
# df["zip"].dropna(inplace=True)
# df["zip"].fillna(df["zip"].mean(),inplace=True)
# df.dropna(inplace=True)
# print(df.info())
# print(df["twp"])
# print(df["zip"].isna())
# tmp_li = df["title"].str.split(": ").tolist()
# cate_li = [i[0] for i in tmp_li]
# df["cate"] = pd.DataFrame(np.array(cate_li).reshape((df.shape[0],1)))
#
# cate_num = df.groupby(by="cate").count()["title"]
# # print(cate_num)
#
# plt.figure(figsize=(7, 6), dpi=80)
#
# _x = cate_num.index
# _y = cate_num.values
#
# plt.bar(range(len(_x)),_y,width=0.5)
# plt.xticks(range(len(_x)),_x)
#
# plt.show()