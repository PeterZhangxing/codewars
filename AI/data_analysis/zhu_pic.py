from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="msyhbd.ttc")

a = ['dajiji','dabibi','dadidi','xiaomeimei']
b16 = [12323,321,4321,321]
b15 = [23312,123,4312,432]
b14 = [3213,321,1234,123]

# 设置每个柱体的宽度
bar_width = 0.2

x14 = list(range(len(a)))
x15 = [i+bar_width for i in x14]
x16 = [i+bar_width*2 for i in x14]

plt.figure(figsize=(12,5),dpi=80)

# 绘制柱形图
plt.bar(x14,b14,width=bar_width,label="9月")
plt.bar(x15,b15,width=bar_width,label="10月")
plt.bar(x16,b16,width=bar_width,label="11月")

# 设置x轴显示的内容
plt.xticks(x15,a,fontproperties=my_font)

plt.legend(prop=my_font,loc="upper right")

plt.show()