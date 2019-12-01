#！/usr/bin/python3.5

# 新采集的网卡信息
new_set = set(["#1","#2","#3"])

# 上次存在数据库中的信息
old_set = set(["#1","#4","#7"])

# 需要添加的网卡信息
add_set = new_set.difference(old_set)
print(add_set) # {'#3', '#2'}

# 需要删除的网卡信息
del_set = old_set.difference(new_set)
print(del_set) # {'#4', '#7'}

# 原来就有的网卡信息，需要对比该网卡的每一项属性后，才能确定是不是需要更新
may_update_set = new_set.intersection(old_set)
print(may_update_set) # {'#1'}