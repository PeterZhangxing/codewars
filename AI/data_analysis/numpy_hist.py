import numpy as np
from matplotlib import pyplot as plt

us_file_path = ""
uk_file_path = ""

# 从文件中获取数据，存在二位数组中
t_us = np.loadtxt(us_file_path,delimiter=",",dtype="int")

# 取得样本的最后一列数据
t_us_comments = t_us[:,-1]
t_us_comments = t_us_comments[t_us_comments<=5000]

d = 50

bin_nums = (t_us_comments.max()-t_us_comments.min()) // d

plt.figure(figsize=(12,5),dpi=80)

plt.hist(t_us_comments,bin_nums)

plt.show()