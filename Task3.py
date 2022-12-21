# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#
# Пример:
#
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
print("Введите число")
n = int(input())
d = {}
for i in range(1, n + 1):
    d[i] = round((1 + (1 / i)) ** i, 2)
print(d)
sum=0
for i in range(0, n):
    sum+=d[i+1]
print(sum)
