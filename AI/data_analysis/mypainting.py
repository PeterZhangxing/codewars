from matplotlib import pyplot as plt

x = range(2,26,2)

y = [15,14.3,21,17,20,25,26,26,22,18,15,16]

# 设置图片大小和每英尺的像素点数
plt.figure(figsize=(9,5),dpi=80)

# 设置x轴和y轴显示的坐标值
plt.xticks([i/2 for i in range(4,49)])
plt.yticks(range(int(min(y)),int(max(y))+1,2))

# 画图
plt.plot(x,y)
# 保存图片
# plt.savefig('myfig.png')
# 显示图片
plt.show()