import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("data_source/BeijingPM20100101_20151231.csv")
# print(df.head(3))
# print(df.info())

df["datetime"] = pd.PeriodIndex(
    year=df["year"],
    month=df["month"],
    day=df["day"],
    hour=df["hour"],
    freq="H")

df.set_index("datetime",inplace=True)
df = df.resample("7D").mean()
# print(df.head(3))

data_usa = df["PM_US Post"]
data_cn = df["PM_Nongzhanguan"]

plt.figure(figsize=(15, 6), dpi=80)

_x = data_usa.index
_xticks = [i.strftime("%Y-%m-%d") for i in _x]

_y_usa = data_usa.values
_y_cn = data_cn.values

plt.plot(range(len(_x)),_y_usa,label="US_POST")
plt.plot(range(len(_x)),_y_cn,label="CN_POST")

plt.xticks(range(0,len(_x),10),_xticks[::10],rotation=45)

plt.legend(loc="upper right")
plt.grid(axis='y')
plt.show()