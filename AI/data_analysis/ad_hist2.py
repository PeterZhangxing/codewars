import pandas as pd
from matplotlib import pyplot as plt

file_path = "data_source/IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

# print(df.head(3))
# print(df.info())

rate_data = df["Rating"].values
# print(rate_data)

max_rate = rate_data.max()
min_rate = rate_data.min()
# print(max_rate,min_rate)

# 构建直方图的x坐标的值列表
num_bin_list = [1.9,3.5]
i = 3.5
while i<=max_rate:
    i += 0.5
    num_bin_list.append(i)

plt.figure(figsize=(12,5),dpi=80)
plt.hist(rate_data,num_bin_list)
plt.xticks(num_bin_list)

plt.show()