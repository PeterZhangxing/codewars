import numpy as np
from matplotlib import pyplot as plt

us_file_path = ""
uk_file_path = ""

t_uk = np.loadtxt(uk_file_path,delimiter=',',dtype='int')

t_uk = t_uk[t_uk[:,1<=500000]]
t_uk_comment = t_uk[:,-1]
t_uk_like = t_uk[:,1]

plt.figure(figsize=(12,5),dpi=80)

plt.scatter(t_uk_like,t_uk_comment)

plt.show()