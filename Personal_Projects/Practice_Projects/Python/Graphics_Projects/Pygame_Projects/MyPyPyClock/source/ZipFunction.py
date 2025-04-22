

def test():
    dict1 = {'k1':44, 'k2':44}
    dict2 = {'d1': 14, 'd2':33}
    dictR = tuple(zip(dict2, dict1))
    print(dictR)

def test2():
    clock12 = dict(zip(range(12), range(0, 360, 30)))   ##  Hour hand
    clock60 = dict(zip(range(60), range(0, 260, 6)))
    print(clock12)
    print(clock60)

def test3():
    print(9 % 3)

if __name__ == '__main__':
    test3()