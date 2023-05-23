
def find_unique_value(numbers):
    if not numbers:
        return None
    unique = numbers[0]
    for element in numbers:
        if element in numbers:
            continue
        else:
            clear(unique)
            append.unique(element)
    return unique

#a = find_unique_value([1, 2, 1, 1])
#print(a)






