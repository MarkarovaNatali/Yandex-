N = int(input())
dlina = (N + 1) // 2
for i in range(N):
    x = 1
    for j in range(N):
        print(str(x).rjust(len(str(dlina))), end=' ')
        if j < i:
            x += 1
        if j >= (N - i - 1):
            x -= 1
    print('')
