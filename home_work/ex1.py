from random import randint

n = int(input('Enter the len of set_1: '))
m = int(input('Enter the len of set_2: '))

set_1 = set(int(input('Enter the value if set_1: ')) for _ in range(n))
set_2 = set(int(input('Enter the value if set_2: ')) for _ in range(m))

print(set_1)
print(set_2)
print(sorted(set_1.intersection(set_2)))

