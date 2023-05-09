a = input(str())

parts =a.split('*')
print('Name:' + parts[0])
born = parts[1]
deth = parts[2]
b = int(born[0:4])
c = int(deth[0:4])

print('Age:', (c- b),'years')


























