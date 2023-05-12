age = int(input('How old are you? '))

if age > 0 and age < 2:
    print('baby')
elif age >=2 and age < 4:
    print('kid')
elif age >=4 and age < 13:
    print('child')
elif age >=13 and age < 20:
    print('teenager')
elif age >=20 and age < 65:
    print('grow-up')
elif age > 65:
    print('senior')
else:
    print('mistake')