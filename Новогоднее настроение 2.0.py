n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(1)
    print(2)
else:
    number = 1
    ren = 1
    dlina_max = 0
    while number < n:
        row = ''
        for j in range(ren, ren + number):
            if j > n:
                break
            row += str(j)
            if j < (ren + number - 1) and j != n:
                row += ' '
        dlina = len(row)
        if dlina > dlina_max:
            dlina_max = dlina
        ren += number
        number += 1
    m = 1
    k = 1
    while k < n:
        row = ''
        for i in range(k, k + m):
            if i > n:
                break
            row += str(i)
            if i < (k + m - 1) and i != n:
                row += ' '
        print(f'{row:^{dlina_max}}')
        k += m
        m += 1