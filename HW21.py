
def is_even(n):

    int_to_string = str(n)
    string_to_list = list(int_to_string)

    last_number = string_to_list[-1]

    if last_number == '1' or last_number == '3' or last_number == '5' or last_number == '7' or last_number == '9':
        return False
    else:
        return True

result = is_even(1234554**3)


print(result)



