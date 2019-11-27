import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager


my_font = font_manager.FontProperties(fname="msyhbd.ttc")

us_path = "data_source/US_video_data_numbers.csv"
gb_path = "data_source/GB_video_data_numbers.csv"

us_data = np.loadtxt(us_path,delimiter=",",dtype="int")
gb_data = np.loadtxt(gb_path,delimiter=",",dtype="int")

total_data = np.vstack((us_data,gb_data))

# print(us_data.shape)
# print(gb_data.shape)
# print(total_data.shape)
'''
(1688, 4)
(1600, 4)
(3288, 4)
'''

selected_data = total_data[total_data[:,-1]<10000]
# print(selected_data.shape)

selected_comment = selected_data[:,-1]
selected_like = selected_data[:,1]

plt.figure(figsize=(12,5),dpi=80)
plt.scatter(selected_comment,selected_like)

distance = max(selected_comment) - min(selected_comment)
x = list(range(distance+1001))
_xtick_label = ["评论数:%s"%i for i in x]
plt.xticks(x[::1000],_xtick_label[::1000],fontproperties=my_font,rotation=45)

plt.show()