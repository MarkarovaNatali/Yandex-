n = int(input())
x = n
summ_max = 0
z = 2
for i in range(2, 11):
    summ = 0
    while x > 0:
        y = x % i
        summ += y
        x //= i
    if summ > summ_max:
        summ_max = summ
        z = i
    x = n
print(z)

