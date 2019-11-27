from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="msyhbd.ttc")
a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
b = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]


x = list(range(11,31))
y1 = a
y2 = b

plt.figure(figsize=(12,5),dpi=80)

plt.plot(x,y1,color="red",label="魔人布偶")
plt.plot(x,y2,color="green",label="大教堂吗")

_xticks_label = ["%s岁"%i for i in x]
plt.xticks(x[::1],_xticks_label[::1],fontproperties=my_font)

plt.xlabel("年龄",fontproperties=my_font)
plt.ylabel("个数",fontproperties=my_font)
plt.title("女朋友个数图",fontproperties=my_font)
plt.legend(prop=my_font)

plt.show()