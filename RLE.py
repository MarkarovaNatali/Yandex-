n = input()
i = 0
while i < (len(n) - 1):
    a = n[i]
    b = 1
    while n[i] == n[i + 1]:
        b += 1
        i += 1
        if i == len(n) - 1:
            break
    print(a, b)
    i += 1
if n[-2] != n[-1]:
    print(n[-1], 1)


