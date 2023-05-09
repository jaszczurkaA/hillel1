snake = input()

camel = snake.split('_')
camel1 = camel[0].capitalize()
camel2 = camel[1].capitalize()
camel3 = camel[2].capitalize()
camel = (camel1 + camel2+ camel3)
camel = ''.join(camel)
print(camel)




