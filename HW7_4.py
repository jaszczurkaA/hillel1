import random

def common_elements():
    global a
    five_list = []
    three_list = []
    for a in range(0, 30):
        a = random.randint(0, 100)
        if a % 5 == 0:
            five_list.append(a)
    print(five_list)
    for a in range(0, 50):
        if a % 3 == 0:
            three_list.append(a)
    print(three_list)
    lst1 = five_list
    lst2 = three_list
    lst_common = []
    for i in lst1:
        if i in lst2:
            lst_common.append(i)
    print(lst_common)


common_elements()







