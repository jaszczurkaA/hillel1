
#завдання 1 - з 3 змінними
a = input()
b = input()

buffer = a
a = b
b = buffer
print(a, b)

#завданя 2 - з 2 змінними
c = input()
d = input()

c, d= d, c
print(c, d)

#завдання 3 - з +-
e = int(input())
f = int(input())

g = e
e = e - e + f
f = f - f + g
print(e, f)









