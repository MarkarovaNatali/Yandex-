import random

a = random.randint(1, 1000)
n = 0
while True:
    if n == 10:
        print('Не угадал')
        break
    b = int(input())
    if a > b:
        print('больше')
    if a < b:
        print('меньше')
    n += 1
    if a == b:
        print('Число отгадано')
        break
