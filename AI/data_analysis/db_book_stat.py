import pandas as pd

csv_file_path = "data_source/books.csv"
df = pd.read_csv(csv_file_path)
df = df.loc[:,["authors","title","ratings_count"]]

# print(df.head(3))
# print(df.info())
# print(df.describe())

author_li = df.loc[:,"authors"].str.split(" ").tolist()
author_set = set([i for authors in author_li for i in authors])
author_total_num = len(author_set)
print(author_total_num)