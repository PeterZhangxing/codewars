import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# 把时间字符串列转换为时间类型
df = pd.read_csv("data_source/911.csv")
df["timeStamp"] = pd.to_datetime(df["timeStamp"])

tmp_li = df["title"].str.split(": ").tolist()
cat_li = [i[0] for i in tmp_li]
df["cate"] = pd.DataFrame(np.array(cat_li).reshape((df.shape[0],1)))

df.set_index("timeStamp",inplace=True)

plt.figure(figsize=(14, 6), dpi=80)

for group_name,group_data in df.groupby(by="cate"):
    # 把按分类分组后的每组数据,再按照月份聚合,计算每个月有多少个条目
    count_by_month = group_data.resample("M").count()["title"]
    # print(count_by_month.head())

    # 为每个分类,画每个月的数据统计图
    _x = count_by_month.index
    _y = count_by_month.values

    plt.plot(range(len(_x)),_y,label=group_name)
    _xticks = [i.strftime("%Y-%m") for i in _x]
    plt.xticks(range(len(_x)),_xticks,rotation=45)

plt.legend(loc="upper right")
plt.show()