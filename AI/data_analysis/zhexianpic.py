from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="msyhbd.ttc")

# 设置纵坐标的值
y1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2 = [1,3,5,1,6,4,3,2,3,3,4,2,1,1,1,1,1,1,1,1]

# 设置横坐标的值
x = range(11,31)

# 设置图片的大小
plt.figure(figsize=(12,5),dpi=80)

# 根据横纵坐标生成图像
plt.plot(x,y1,label='自己',color='red',linestyle='--',linewidth=5,marker='o', markersize=12)
plt.plot(x,y2,label='徐冉',color='green',linestyle=':',linewidth=5)

# 设置横纵坐标显示的样式
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels,fontproperties=my_font,rotation=45)
plt.yticks(range(0,8))

# 设置网格
plt.grid(alpha=0.7,linestyle=':',axis="y")

# 设置图例的字体和位置
plt.legend(prop=my_font,loc="upper right")

# 设置图的名字,横纵轴的名字
plt.title(label="你猜猜",fontproperties=my_font)
plt.xlabel(xlabel="年龄",fontproperties=my_font)
plt.ylabel(ylabel="个数",fontproperties=my_font)

# 显示图片
plt.show()