# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле
# file.txt в одной строке одно число.
import random

n = int(input())
array = [random.randint(-n, n) for i in range(n)]
print(f"Наш массив {array}")

data = open('file.txt', 'r')
list = []
for line in data:
    list.append(line)
data.close

list = [i.rstrip() for i in list]

max_in_file = list[0]
for i in range(1, len(list)):
    if list[i] > max_in_file:
        max_in_file = list[i]
# print(max_in_file)
if int(max_in_file) <= (n + 1):
    print(f" числа из файла: {list}")
    result = 1
    for i in range(0, len(list)):
        if array[int(list[i])] != 0:
            result = result * array[int(list[i])]
        else:
            result = 0
    print(f" Результат: {result}")
else:
    print(f" числа из файла: {list}")
    print(f" Вы ввели оч. маленькое число, попробуйте ещё")
