def prime_generator(number_the_end):
    def prime(number):
        if number <= 3:
            return True
        if number % 2 == 0:  # перевірка чи парне
            return False
        odd = 3   #перевірка на ділення на непарні
        while odd * odd <= number:
            if number % odd == 0:
                return False
            odd += 2
        return True

    a = 2
    while True:
        if a > number_the_end:
            return
        if prime(a):
            yield a
        a += 1

lst = list(prime_generator(500))
print(lst)