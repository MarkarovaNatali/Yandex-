N, M = int(input()), int(input())
z = str(N * M)
for i in range(N):
    if i % 2 == 0:
        x = 1 + i * M
        for j in range(M):
            print(str(x).rjust(len(z)), end=' ')
            x += 1
    else:
        x = (i + 1) * M
        for j in range(M):
            print(str(x).rjust(len(z)), end=' ')
            x -= 1
    print('')