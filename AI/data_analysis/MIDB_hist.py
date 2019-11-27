import pandas as pd
from matplotlib import pyplot as plt

file_path = "data_source/IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

# print(df.info())
# print(df.head(1))

rating = df.loc[:,"Rating"].values

distance = 0.5
num_bin = int((rating.max() - rating.min())//0.5)

# print(rating.max())
# print(rating.min())

plt.figure(figsize=(12,5),dpi=80)

x_list = [1.9,2.5,]
i = 2.5
while i <= rating.max():
    i += 0.5
    x_list.append(i)

plt.hist(rating,x_list)
plt.xticks(x_list)

plt.grid(alpha=0.7,axis="x")

plt.show()