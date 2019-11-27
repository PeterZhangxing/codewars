from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,UniqueConstraint,Index,CHAR,VARCHAR
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine


################################ 创建表格类 ################################

# 创建给自定义表类继承的基类
myBase = declarative_base()

class UserType(myBase):
    '''
    通过类的方式，在数据库中自定义表结构
    '''
    # 定义数据库中表的名字
    __tablename__ = 'usertype'

    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(64),nullable=True,index=True)


class Users(myBase):

    __tablename__ = 'users'

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(VARCHAR(16),nullable=True,index=True)
    email = Column(CHAR(32),unique=True)

    # 定义外键约束
    user_type_id = Column(Integer,ForeignKey('usertype.id'))

    # 定义正向及反向关联，定义在有外键的类中
    user_type = relationship('UserType',backref='usersobj')

    # 定义联合索引和联合唯一等，多个字段共同组成的属性
    # __table_args__ = (
    #     UniqueConstraint('id', 'name', name='uix_id_name'),
    #     Index('ix_n_ex','name', 'email',),
    # )


def create_db():
    '''
    连接数据库，创建表
    :return:
    '''
    engine = create_engine("mysql+pymysql://alchemy:redhat@10.1.1.128:3306/test_sqlalchemy?charset=utf8", max_overflow=5)
    # 格式为：用户名:密码@数据库地址:数据库端口/数据库名称？数据库选项
    myBase.metadata.create_all(engine)
    return engine


def drop_db():
    '''
    连接数据库，删除所有的表
    :return:
    '''
    engine = create_engine("mysql+pymysql://alchemy:redhat@10.1.1.128:3306/test_sqlalchemy?charset=utf8", max_overflow=5)
    myBase.metadata.drop_all(engine)


################################ 创建操作表中数据的连接 ################################

engine = create_db()
Session = sessionmaker(bind=engine)
session = Session()


################################ 在表中添加一行或者多行数据 ################################

# 在表中添加一行或者多行数据
# obj1 = UserType(title='normal_user')
# session.add(obj1)
#
# obj_li = [
#     UserType(title='DIAMOND_user'),
#     UserType(title='GOLD_user'),
#     UserType(title='SILVER_user')
# ]
# session.add_all(obj_li)

# obj1 = UserType(title='NORMAL_user')
# session.add(obj1)


################################ 实现普通的数据查询 ################################

# select * from user,usertype 语句的实现
# ret = session.query(Users, UserType)

# print(session.query(UserType))
# user_type_list = session.query(UserType).all()
# for row in user_type_list:
#     print(row.id,row.title)

# select xxx  UserType where 语句实现
# user_type_list = session.query(UserType.id,UserType.title).filter(UserType.id > 2)
# for row in user_type_list:
#     print(row.id,row.title)


################################ 实现运行原生的SQL语句 ################################

session.execute(r"insert into users (name,email,user_type_id) values ('zx4','ewrdasd1232','4');")


################################ 实现连表操作 ################################

# 手动连表
# select * from user,usertype whre user.usertype_id = usertype.id
# ret = session.query(Users, UserType).filter(Users.usertype_id==UserType.id)

# 实现表的内连接
# result = session.query(Users).join(UserType)
# print(result)

# 实现表的左外连接
# result = session.query(Users).join(UserType,isouter=True)
# print(result)


################################ 实现删除数据 ################################

# 删除数据
# session.query(UserType).filter(UserType.title=='normal_user').delete()


################################ 实现修改数据 ################################

# 修改数据
# session.query(UserType).filter(UserType.id==2).update({"title":"BLACK_user"})
# 在原数据基础上修改数据
# session.query(UserType).filter(UserType.id > 3).update({UserType.title: UserType.title + "x"}, synchronize_session=False)
# session.query(UserType.id,UserType.title).filter(UserType.id > 0).update({"num": Users.num + 1}, synchronize_session="evaluate")


################################ 条件语句中的子查询 ################################

# 1、select * from b where id in (select id from tb2);
# q1 = session.query(UserType.id).filter(UserType.id > 3).all()
# q1_li = []
# for i in q1:
#     q1_li.append(i[0])
# q2 = session.query(Users.name).filter(Users.user_type_id.in_(q1_li)).all()
# print(q2)
# # 第二种实现
# q2 = session.query(Users.name).filter(Users.user_type_id.in_(session.query(UserType.id).filter(UserType.id > 3))).all()
# for i in q2:
#     print(q2[0])

# 2、select * from (select * from tb) as B;
# 查询结果是一个子表，可以作为另一个查询的基表
# q1 = session.query(UserType).filter(UserType.id > 5).subquery()
# result = session.query(q1).all()
# print(result)

# 3、select id,(select * from users where users.user_type_id=usertype.id) from usertype;
# # 实现select后面的子查询语句，as_scalar返回的是一个字段值，不是一个表对象的集合
# result = session.query(UserType.id,session.query(Users.name).filter(Users.user_type_id==UserType.id).as_scalar()).all()
# print(result)
# # 输出结果：[(2, 'zx2'), (3, 'zx'), (4, None), (6, 'zx1')]


################################ 使用relationship完成连表操作 ################################

# 问题1. 获取用户信息以及与其关联的用户类型名称(FK,Relationship=>正向操作)
# user_list = session.query(Users,UserType).join(UserType,isouter=True)
# print(user_list)
# for row in user_list:
#     print(row[0].id,row[0].name,row[0].email,row[0].user_type_id,row[1].title)

# 手动连表操作
# user_list = session.query(Users.name,UserType.title).join(UserType,isouter=True).all()
# for row in user_list:
#     print(row[0],row[1],row.name,row.title)

# 正向连表操作
user_list = session.query(Users)
for row in user_list:
    print(row.name,row.id,row.user_type)

# 问题2. 获取用户类型
# 手动连表操作
# type_list = session.query(UserType)
# for row in type_list:
#     print(row.id,row.title,session.query(Users).filter(Users.user_type_id == row.id).all())

# 反向连表操作
type_list = session.query(UserType)
for row in type_list:
    print(row.id,row.title,row.usersobj)


################################ 提交程序对数据库的操作后关闭连接 ################################

session.commit()
session.close()