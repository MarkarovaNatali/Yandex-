# Математик Виталий Евгеньевич задумался над вопросом выгоды систем счисления.
# Он решил, что выгодной системой счисления будет являться та, в которой число имеет наибольшую сумму цифр.
# Напишите программу, которая по введённому числу определяет основание системы счисления с максимальной выгодой.
#
# Формат ввода
# Одно натурально число.
#
# Формат вывода
# Одно натуральное число из диапазона [2;10] — основание системы счисления с максимальной выгодой.
# Если таких оснований несколько, выбирается наименьшее.


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

