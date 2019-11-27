#/usr/bin/python3.5

# mydic = {10000:0.1,100000:0.075}
#
# print(mydic[10000])

while True:
    t_income = input("pure bonus: ")

    if t_income == 'exit' or t_income == 'quit':
        exit('Already exited this programme!')
    else:
        t_income = int(t_income)

    b_level = [1000000,600000,400000,200000,100000,0]
    r_level = [0.01,0.015,0.03,0.05,0.075,0.1]
    bonus = 0

    for i in range(0,6):
        if t_income > b_level[i]:
            bonus += (t_income - b_level[i]) * r_level[i]
            # 计算每次在固定的区间内多出来的那部分获取的提成

            t_income = b_level[i]
            # 除去本区间多出来的收入后，下个区间剩下的值

    print(bonus)

