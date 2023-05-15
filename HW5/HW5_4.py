
# 4 задачка 5 урок

import random

old_list = []

for i in range(random.randint(3, 10)):
    old_list.append(random.randint(0, 100))
new_list = [old_list[0], old_list[2], old_list[-2]]

print(f"{old_list} == {new_list}")







