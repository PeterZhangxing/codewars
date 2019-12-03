import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


csv_file_path = "data_source/911.csv"
df = pd.read_csv(csv_file_path)

# print(df.info())
# print(df.head(3))

tmp_li = df["title"].str.split(": ").tolist()

# 构造全0矩阵求每个分类下面有几条数据
# cate_li = list(set([i[0] for i in tmp_li]))
# zero_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_li))),columns=cate_li)
#
# for cate in cate_li:
#     zero_df[cate][df["title"].str.contains(cate)] = 1

# cate_sum = zero_df.sum(axis=0)
# print(cate_sum)
'''
EMS        124844.0
Fire        37432.0
Traffic     87465.0
dtype: float64
'''

# 为每行数据添加新分类列,统计每个分类有多少条数据
df["Category"] = pd.DataFrame(np.array([ i[0] for i in tmp_li ]).reshape((df.shape[0],1)))
cate_sum = df.groupby(by="Category").count()["title"]
# print(cate_sum)

_x = cate_sum.index
_y = cate_sum.values

plt.figure(figsize=(12,5),dpi=80)

plt.bar(_x,_y,color="r",width=0.5)
plt.xticks(_x)
plt.grid(axis="y",alpha=0.5)

plt.show()