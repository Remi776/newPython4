
flag = True
max_number = 0
while flag:
    n = int(input())
    if max_number < n:
        max_number = n
    if n == 0:
        flag = False
print(max_number)