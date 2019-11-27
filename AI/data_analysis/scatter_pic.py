from matplotlib import pyplot as plt
from matplotlib import font_manager
import random
my_font = font_manager.FontProperties(fname="msyhbd.ttc")

y3 = [12,23,32,12,43,21,33,43,12,34,12,32,32,44,12,12,33,11,12,23,32,12,43,21,33,43,12,34,12,32,32]
y10 = [12,23,32,12,43,21,33,43,12,34,12,32,32,44,12,12,33,11,12,23,32,12,43,21,33,43,12,34,12,32,19]
random.shuffle(y3)
random.shuffle(y10)

x3 = range(1,32)
x10 = range(51,82)

# 设置图片的大小
plt.figure(figsize=(12,5),dpi=80)

# 绘制散点图
plt.scatter(x3,y3,label='3月')
plt.scatter(x10,y10,label='10月')

_x = list(x3) + list(x10)
_xtick_labels = ["3月{}日".format(i) for i in x3]
_xtick_labels += ["10月{}日".format(i-50) for i in x10]
plt.xticks(_x[::3],_xtick_labels[::3],fontproperties=my_font,rotation=45)

plt.title(label="温度趋势",fontproperties=my_font)
plt.xlabel(xlabel="月份",fontproperties=my_font)
plt.ylabel(ylabel="温度",fontproperties=my_font)

# 设置图例的字体和位置
plt.legend(prop=my_font,loc="upper right")

plt.show()