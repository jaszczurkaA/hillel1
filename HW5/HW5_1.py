input_list = input()

import string
letter1 = input_list[0]
letter2 = input_list[2]

lst = list(string.ascii_letters)
a= lst.index(letter1)
b = lst.index(letter2)
c = b+1
print(lst[a:c])
