from pymongo import MongoClient


cli = MongoClient(host="10.1.1.128",port=27017)
collection = cli["test"]["stu"]

# collection.aggregate()

# 在集合中插入一条文档数据
res = collection.insert({"name":"dashabi","age":87,"gender":1,"school":["wucheng","K19","HGD"]})
print(res)
'''
5cf3944c89bab71c10fca582
'''

# 插入多条数据
# data_list = [{"name":"test{}".format(i)} for i in range(10)]
# collection.insert_many(data_list)

# 查找一条记录
res = collection.find_one({"name":"zx"})
print(res)
'''
{'_id': ObjectId('5cefdc007bc79b613a78d687'), 'name': 'zx', 'age': 29.0, 'gender': 1.0, 'school': 'UCLA'}
'''

# 批量查找记录,返回的是一个游标对象，类似生成器
res_cur = collection.find({"age":{"$gte":30}})
res_count = collection.find({"age":{"$gte":30}}).count()
print(res_count) # 10

for res in res_cur:
    print(res)
'''
{'_id': ObjectId('5cefdc167bc79b613a78d688'), 'name': 'honghong', 'age': 56.0, 'gender': 0.0}
{'_id': ObjectId('5cefdc3a7bc79b613a78d68a'), 'name': 'dahuzi', 'age': 42.0, 'gender': 1.0}
{'_id': ObjectId('5cefdc587bc79b613a78d68b'), 'name': 'taylor', 'age': 32.0, 'gender': 0.0}
{'_id': ObjectId('5cf3840fdb40c07621ea089d'), 'name': 'dazhujiao', 'age': 48.0, 'gender': 1.0, 'school': ['K8', 'HongQi', 'JLU', 'K19']}
{'_id': ObjectId('5cf386abdb40c07621ea089e'), 'name': 'hj', 'age': 44.0, 'gender': 0.0, 'school': ['K8', 'HongQi', 'JLU', 'K19']}
{'_id': ObjectId('5cf3937689bab71a48e01482'), 'name': 'dashabi', 'age': 87, 'gender': 1, 'school': ['wucheng', 'K19', 'HGD']}
{'_id': ObjectId('5cf393aa89bab72630f58dea'), 'name': 'dashabi', 'age': 87, 'gender': 1, 'school': ['wucheng', 'K19', 'HGD']}
{'_id': ObjectId('5cf393d289bab715f0139797'), 'name': 'dashabi', 'age': 87, 'gender': 1, 'school': ['wucheng', 'K19', 'HGD']}
{'_id': ObjectId('5cf3941d89bab72b4cc2dc79'), 'name': 'dashabi', 'age': 87, 'gender': 1, 'school': ['wucheng', 'K19', 'HGD']}
{'_id': ObjectId('5cf3944c89bab71c10fca582'), 'name': 'dashabi', 'age': 87, 'gender': 1, 'school': ['wucheng', 'K19', 'HGD']}
'''

# 因为生成器对象已经被使用完，所以此时打印内容为空
print(list(res_cur)) # []