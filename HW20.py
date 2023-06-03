def generate_cube_numbers(last_number):
    numbers = list(range(2, last_number+1))
    cube = []
    for i in range(len(numbers)):
        a = i**3
        if a > 2 and a < last_number:
            cube.append(a)
        if a > last_number:
            break
    return(cube)

cube_numbers = generate_cube_numbers(28)
print(cube_numbers)




