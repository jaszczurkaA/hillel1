a= float(input('Введіть перше число: '))
b = input('Введіть оператор *, /, + чи -: ')
c = float(input('Введіть друге число: '))

if b == '*':
    print(float(a * c))
elif b == '+':
    print(float(a + c))
elif b == '-':
    print(float(a - c))
elif b == '/':
    if c == 0:
        print('на нуль ділити не можна')
    else:
        print(float(a / c))
else:
    print()





