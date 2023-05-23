str_of_numbers  = input()

def add_one():

    number = int(''.join(map(str, str_of_numbers)))
    number_plus_one = number + 1
    number_plus_one_str = str(number_plus_one)
    number_plus_one_lst = list(number_plus_one_str)

    return number_plus_one_lst

print(add_one())

add_one()






