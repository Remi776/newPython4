# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.


text = input().split()
result = dict()

def CountingChar():
    for i in text:
        if i in result:
            print(f'{i}_{result[i]}', end=' ')
        else:
            print(i, end=' ')
        result[i] = result.get(i, 0) + 1

CountingChar()
