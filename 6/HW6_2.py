dct= {}
lst = input()

for el in lst:
    count = dct.get(el)
    if count:
        dct[el]+=1
    else:
        dct[el] = 1
print(dct)







