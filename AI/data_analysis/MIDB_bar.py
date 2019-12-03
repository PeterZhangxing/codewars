import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


file_path = "data_source/IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

tmp_genre_li = df.loc[:,"Genre"].str.split(",").tolist()
genre_li = list(set([i for gens in tmp_genre_li for i in gens]))

# print(len(genre_li)) # 20

zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_li))),columns=genre_li)
# print(zeros_df.head(3))
'''
   Western  Fantasy  Romance  Music  ...  Adventure  Comedy  Mystery  Drama
0      0.0      0.0      0.0    0.0  ...        0.0     0.0      0.0    0.0
1      0.0      0.0      0.0    0.0  ...        0.0     0.0      0.0    0.0
2      0.0      0.0      0.0    0.0  ...        0.0     0.0      0.0    0.0
'''

for i in range(df.shape[0]):
    zeros_df.loc[i,tmp_genre_li[i]] = 1

genre_total_count = zeros_df.sum(axis=0)
# print(type(genre_total_count)) # <class 'pandas.core.series.Series'>

_x = list(genre_total_count.index)
_y = list(genre_total_count.values.astype(int))

# print(_x)
# print(_y)
plt.figure(figsize=(12,5),dpi=80)

plt.bar(range(len(_x)),_y,width=0.8,color="r")
plt.xticks(range(len(_x)),_x,rotation=-45)
plt.grid(axis="y",alpha=0.6)

plt.show()