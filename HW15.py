def pow(x):
    return x ** 2

def some_gen(begin, n, func):
    a = 0
    while a < n:
        yield begin
        begin = func(begin)
        a = a+1

gen= some_gen(5, 10, pow)
print(next(gen))
print(next(gen))
print(next(gen))

