number = input()
result = list(number)

a = int(result[0])
b = int(result[1])
c = int(result[2])
print(a+b+c)

m = input()
n = int(m)
hundreds = n//100
tenth = n % 100 // 10
ones = n% 100 % 10
print(hundreds + tenth + ones)

