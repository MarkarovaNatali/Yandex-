N, M = int(input()), int(input())
z = str(N * M)
x = 1
for i in range(N):
    for j in range(M):
        if j % 2 == 0:
            x = (i + 1) + j * N
            print(str(x).rjust(len(z)), end=' ')
        else:
            x = (j + 1) * N - i
            print(str(x).rjust(len(z)), end=' ')
    x = i + 1
    print('')