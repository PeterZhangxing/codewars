# 只读方式打开文件,只能read
f = open('test.txt','r',encoding='utf-8')
content = f.read(3) # 读取文件的内容，可以指定读取几个字符
f.seek(3) # 将文件中的光标向后移动3个字节
f.seek(f.tell()-3) # 将文件中的光标向前移动3个字节
content1 = f.read()
cposition = f.tell() # 获取光标当前所在位置是第几个字节
f.close() # 关闭文件，句柄不再占用内存


# 只写模式打开文件，只能write，每次以写模式打开文件都会清空文件
f1 = open('test.txt','w',encoding='utf-8')
content3 = 'it is a test'
f1.write(content3)
f1.close()


# 以添加模式打开文件，不会清空文件原内容，但只能在文件最后添加内容，但是不能读取内容
f1 = open('test.txt','a',encoding='utf-8')
content3 = 'it is a test'
f1.write(content3)
f1.close()


# 以比特模式保存和读取文件，此时写到文件或从文件读取的内容都是二进制流
f2 = open('test.txt','rb')
content2 = f2.read().decode('utf-8')
f2.close()

f3 = open('test.txt','wb')
f3.write('附近看到类似纠纷'.encode('utf-8'))
f3.close()


# 以读写模式打开文件，必须先读取，再写入
f = open('test.txt',mode='r+',encoding='utf-8')
print(f.read())
f.write('hahahaha')
f.close()


# 以添加读模式打开文件,先写，再读
f = open('test.txt',mode='a+',encoding='utf-8')
f.write('hahahaha')
print(f.read(f.seek(f.tell()-9)))
f.close()


# 其他常用功能
f = open('test.txt',mode='r+',encoding='utf-8')
f.readable() # 判断文件是否可读
f.writable() # 判断文件是否可写
line = f.readline() # 一次读取一行文件内容
line_li = f.readlines() # 每一行当成列表中的一个元素，存储在list中

# 循环读取文件中的每一行，是一个迭代器，可以节省内存
for line in f:
    print(line)
f.close()


# 可以自动关闭文件的写法
with open('log',mode='r+',encoding='utf-8') as f,\
        open('log',mode='w+',encoding='utf-8') as f1:
    f1.write(f.read())