#!/usr/bin/python3.5

def cakes(recipe, available):
    for k in recipe.keys():
        if k not in available.keys():
            return 0

    countl = []
    for k,v in recipe.items():
        tmp = int(available[k]/v)
        countl.append(tmp)

    return min(countl)


if __name__ == "__main__":
    res = cakes({'flour': 500, 'sugar': 200, 'eggs': 1,'apple':1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})
    res1 = cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})
    print(res)
    print(res1)

