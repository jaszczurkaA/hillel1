#lst1= input()
#lst= list(map(int, input(lst1)))

#for i in range(len(lst)):
 #   if lst[i]==0:
      #  lst = lst.pop(i)
      #  print(lst)
      #  lst.append(int(input(i)))
#print(lst)

lst = list(map(int, input()))

list_num = []
list_zero = []
for i in lst:
    if i == 0:
        list_zero.append(i)
    else:
        list_num.append(i)

print(list_num + list_zero)