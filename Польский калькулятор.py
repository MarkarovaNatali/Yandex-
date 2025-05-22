n = list(input().split())
plus = '+'
minus = '-'
multiply = '*'
while len(n) >= 3:
    i = 0
    while n[i] not in (plus, minus, multiply):
        i += 1
        a = n[i - 2]
        b = n[i - 1]
    if n[i] == plus:
        x = int(a) + int(b)
    elif n[i] == minus:
        x = int(a) - int(b)
    elif n[i] == multiply:
        x = int(a) * int(b)
    n[i] = x
    n.pop(i - 1)
    n.pop(i - 2)
    print(n)