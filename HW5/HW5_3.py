

lst = list(map(int, input()))

list_num = []
list_zero = []
for i in lst:
    if i == 0:
        list_zero.append(i)
    else:
        list_num.append(i)

print(list_num + list_zero)