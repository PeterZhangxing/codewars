#!/usr/bin/python3.5

def queue_time(customers, n):
    if not customers:
        return 0
    elif n == 1:
        return sum(customers)
    elif len(customers) <= n:
        return max(customers)
    elif len(customers) > n:
        que_list = list()
        for q in range(n):
            que_list.append(customers.pop(0))
        while customers:
            min_cus = min(que_list)
            for i,v in enumerate(que_list):
                if v == min_cus and customers:
                    que_list[i] = v + customers.pop(0)
    return max(que_list)

if __name__ == "__main__":
    print(queue_time([10,2,3,3,10,2,3,3,1,2,3,4,5], 5))
    # print(queue_time([2,3,10], 2))
    # print(queue_time([5,3,4], 1))
    # print(queue_time([], 1))
    # print(queue_time([1,2,3,4,5], 100))
    # print(queue_time([2,2,3,3,4,4], 2))
    # print(queue_time([10], 2))
