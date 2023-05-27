
def find_unique_value(numbers):
    if not numbers:
        return None
    unique = []
    for x in range(len(numbers)):
        count_x = 0
        for y in range(x+1, len(numbers)):
            count_y  = 0

            if numbers[x] == numbers[y]:
                count_x += 1
                continue
            else:
                count_y +=1
            if count_y >count_x:
               unique = numbers[x]
            else:
                unique = numbers[y]

    return unique
print(find_unique_value([3, 2, 3, 3, 3]))





    # for element in numbers:
    #     if element in unique:








