import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path = "data_source/IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)
# print(df.head(3))
# print(df.info())

# 首先取得dataframe一列的数据，然后对这一列中的每一个字符串数据做切割后，保存在数组中，
# 最后将整个这一列数据，即series类型的数据，转化为列表数据类型，结果是一个二维数组[[],[]]
tmp_li = df["Genre"].str.split(",").tolist()
# print(type(tmp_li))
# 将二维数组展开为一维
genre_list = list(set([i for j in tmp_li for i in j]))

# 构造一个全是0的dataframe，列是所有的电影分类
zero_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)
# print(zero_df)
'''
     Mystery  Animation  Crime  War  ...  Biography  Family  Fantasy  Romance
0        0.0        0.0    0.0  0.0  ...        0.0     0.0      0.0      0.0
1        0.0        0.0    0.0  0.0  ...        0.0     0.0      0.0      0.0
2        0.0        0.0    0.0  0.0  ...        0.0     0.0      0.0      0.0
3        0.0        0.0    0.0  0.0  ...        0.0     0.0      0.0      0.0
'''

# 遍历所有电影的分类，将该电影属于的分类置为1
for i in range(df.shape[0]):
    zero_df.loc[i,tmp_li[i]] = 1
# print(zero_df)
'''
     Music  Animation  Comedy  Family  ...  War  Biography  Crime  Action
0      0.0        0.0     0.0     0.0  ...  0.0        0.0    0.0     1.0
1      0.0        0.0     0.0     0.0  ...  0.0        0.0    0.0     0.0
2      0.0        0.0     0.0     0.0  ...  0.0        0.0    0.0     0.0
'''

# 计算每个电影分类，分别有多少电影
genre_count = zero_df.sum(axis=0).sort_values(ascending=False)
# print(genre_count)
'''
Music         16.0
Animation     49.0
Comedy       279.0
'''

# 构建柱形图，显示统计数据的结果
_x = genre_count.index
_y = genre_count.values

plt.figure(figsize=(12,5),dpi=80)
plt.bar(range(len(_x)),_y,width=0.4,color="orange")
plt.xticks(range(len(_x)),_x,rotation=45)

plt.show()