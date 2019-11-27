import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager


my_font = font_manager.FontProperties(fname="msyhbd.ttc")

csv_file_path = "data_source/books.csv"
df = pd.read_csv(csv_file_path)

# print(df.info())
# print(df.head(3))

df_books = df[df["original_publication_year"].notnull()]
# print(df_books.info())

grouped_book_rating = df_books.groupby(by="original_publication_year")["average_rating"].mean()
# print(grouped_book_rating)
'''
original_publication_year
-1750.0    3.630000
-762.0     4.030000
-750.0     4.005000
-720.0     3.730000
... ...
'''

_x = grouped_book_rating.index.astype(int)
_y = grouped_book_rating.values

plt.figure(figsize=(12,5),dpi=80)

plt.plot(list(range(len(_x))),_y)
plt.xticks(list(range(len(_x)))[::10],_x[::10],rotation=-45)

plt.show()