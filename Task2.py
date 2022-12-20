# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def facktorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

n = int(input())
list=[]
for i in range (1,n+1):
    list.insert(i-1,facktorial(i))
print(list)
