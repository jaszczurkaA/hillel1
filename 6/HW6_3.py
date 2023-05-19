list_input= [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

dct = {}
for item in list_input:
    if item[0] not in dct:
        dct[item[0]] = [item[1]]
    else:
        dct[item[0]].append(item[1])
print(dct)







