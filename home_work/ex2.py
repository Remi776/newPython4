from random import randint

n = int(input('Enter the num of bushes: '))
list_1 = [randint(1, 10) for _ in range(n)]
new_list = list()
j = 0

for i in range(len(list_1)):
    if j != len(list_1) - 1:
        new_list.append(list_1[i] + list_1[i - 1] + list_1[j + 1])
        j += 1
    else:
        new_list.append(list_1[i] + list_1[i - 1] + list_1[0])

print(list_1)
print(max(new_list))