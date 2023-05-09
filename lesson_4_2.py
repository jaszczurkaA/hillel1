list = input()

length = len(list)

middle_index = length//2
centr = length %2
if centr == 0:
    first_half = list[:middle_index]
    second_half = list[middle_index:]
    print(first_half)
    print(second_half)
elif centr ==1 :
    first_half = list[:middle_index+1]
    second_half = list[middle_index+1:]
elif length == 0:
    print([], [])
else:
    print()






