#/usr/bin/python3.5

while True:

    num = input("Enter an integer: ").strip()

    if num == 'exit' or num == 'quit':
        exit('Has exited this programme!')

    if num.isdigit():
        str_num_len = len(num)
        num = int(num)
    else:
        print('invalid input number!')
        continue

    num_li = list()
    for i in range(1,str_num_len+1):
        j = num // (10 ** (str_num_len - i)) # 获取商
        num = num % (10 ** (str_num_len - i)) # 获取余数
        num_li.append(j)

    rev_num_li = reversed(num_li)

    print(num_li)
    print(list(rev_num_li))