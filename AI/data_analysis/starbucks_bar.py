import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager


my_font = font_manager.FontProperties(fname="msyhbd.ttc")

csv_file_path = "data_source/starbucks_store_worldwide.csv"
df = pd.read_csv(csv_file_path)

df_country = df.groupby(by="Country").count()["Brand"].sort_values(ascending=False)[:10]
# print(df_country)

df_china_city = df[df["Country"]=="CN"].groupby(by="City").count()["Brand"].sort_values(ascending=False)[:25]

# _x = df_country.index
# _y = df_country.values

_x = df_china_city.index
_y = df_china_city.values

plt.figure(figsize=(12,5),dpi=80)

plt.bar(_x,_y,color="r",width=0.5)
plt.xticks(_x,rotation=-45,fontproperties=my_font)
plt.grid(axis="y",alpha=0.5)

plt.show()