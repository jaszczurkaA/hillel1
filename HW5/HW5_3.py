lst1= input()
lst= list(map(int, input(lst1)))

for i in range(len(lst)):
    if lst[i]==0:
        lst = lst.pop(i)
        print(lst)
        lst.append(int(input(i)))
print(lst)