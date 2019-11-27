import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


csv_file_path = "data_source/BeijingPM20100101_20151231.csv"
df =  pd.read_csv(csv_file_path)

# print(df.info())
# print(df.head(3))

df["datetime"] = pd.PeriodIndex(year=df["year"],month=df["month"],day=df["day"],hour=df["hour"],freq="H")
# print(df.info())
df.set_index("datetime",inplace=True)

df = df.resample("7D").mean()

data_usa = df["PM_US Post"]
data_cn = df["PM_Nongzhanguan"]

plt.figure(figsize=(15, 8), dpi=80)

_x = data_usa.index
_x_ticks = [ i.strftime("%Y:%m:%d") for i in _x ]

_y_usa = data_usa.values
_y_cn = data_cn.values

plt.plot(range(len(_x)),_y_usa,label="USA_DATA")
plt.plot(range(len(_x)),_y_cn,label="CN_DATA")

plt.xticks(range(len(_x))[::10],_x_ticks[::10],rotation=-45)

plt.legend(loc="upper right")

plt.grid(axis='y',alpha=0.3)

plt.show()