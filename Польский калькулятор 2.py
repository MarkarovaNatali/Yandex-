n = input().split()
stack = []
for i in n:
    if i.isdigit():
        stack.append(int(i))
    else:
        if i == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif i == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        elif i == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b // a)
        elif i == '~':
            a = stack.pop()
            stack.append((-1) * a)
        elif i == '!':
            a = stack.pop()
            factorial = 1
            for f in range(1, a + 1):
                factorial *= f
            stack.append(factorial)
        elif i == '#':
            a = stack.pop()
            stack.append(a)
            stack.append(a)
        elif i == '@':
            a = stack.pop()
            b = stack.pop()
            c = stack.pop()
            stack.append(b)
            stack.append(a)
            stack.append(c)
print(stack[0])
