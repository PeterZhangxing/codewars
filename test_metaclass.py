####################### 使用元类实现修改类属性的示例 #######################

class MyMeta(type):

    def __new__(cls,class_name,class_parents,class_attr):
        print(class_name)
        print(class_parents)

        new_attr = {}
        for k,v in class_attr.items():
            if not k.startswith('__'):
                new_attr[k.upper()] = v
            else:
                new_attr[k] = v

        return type.__new__(cls,class_name,class_parents,new_attr)

# 元类是用来生成其他类的类，生成某个类之前，
# 都调用了元类的__new__方法，返回的就是一个指向新类的引用
class MyBasic(object,metaclass=MyMeta):
    bar = 100

print(MyBasic.__dict__)
print(MyBasic.BAR)


####################### 使用元类实现orm的向数据表插入一条数据的功能 #######################

class MyMeta(type):

    def __new__(cls, class_name,class_parents,class_attr):

        col_mapping_dict = {}
        for k,v in class_attr.items():
            if isinstance(v,tuple):
                col_mapping_dict[k] = v

        for k in col_mapping_dict:
            class_attr.pop(k)

        class_attr["__mappings__"] = col_mapping_dict
        class_attr["__table_name__"] = class_name

        return type.__new__(cls,class_name,class_parents,class_attr)


class DbMeta(object,metaclass=MyMeta):

    def __init__(self,**kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)

    def save(self):
        table_name = self.__table_name__
        col_name_li = []
        val_li = []
        for k,v in self.__mappings__.items():
            col_name_li.append(v[0])
            val_li.append(getattr(self,k))

        new_val_li = []
        for item in val_li:
            if isinstance(item,int):
                new_val_li.append('%s'%item)
            elif isinstance(item,str):
                new_val_li.append("""'%s'"""%item)

        col_names = ','.join(col_name_li)
        vals = ','.join(new_val_li)

        sql_temp = """insert into %s (%s) values (%s)"""%(table_name,col_names,vals)
        return sql_temp


class User(DbMeta):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")


if __name__ == '__main__':
    obj = User(uid=1,name='zx',email='123@qq.com',password='redhat')
    sql = obj.save()
    print(sql)