from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="msyhbd.ttc")

interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2727,3723,3925,3535,1438,3273,643,987,613,215,47]

plt.figure(figsize=(12,5),dpi=80)

plt.bar(range(len(interval)),quantity,width=1)

_x = [i-0.5 for i in range(len(interval)+1)]
interval+=[150]
plt.xticks(_x,interval)

plt.grid()

plt.show()