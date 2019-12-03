import pandas as pd
import numpy as np

df = pd.read_csv("data_source/dogNames2.csv")

# print(df.info())
# print(list(df.index))
# print(list(df.columns))
# print(df.ndim)
# print(df.dtypes)
# print(df.describe())
# print(df.sort_values(by="Count_AnimalName",ascending=False))
df_ordered = df.sort_values(by="Count_AnimalName",ascending=False)
print(df_ordered.head(3).loc[:,"Row_Labels"].str.len())
# df = df.fillna(df.mean)
# df.fillna(df.median,inplace=True)
# print(df.info())
# print(df.loc[:,"Count_AnimalName"])
# df_mean = df.loc[:,"Count_AnimalName"].mean()
# # print(df_mean)
# df_nonan = df.loc[:,"Count_AnimalName"].fillna(df_mean)
# print(df_nonan[df_nonan.isna()])
# print(df[df.isna()])
