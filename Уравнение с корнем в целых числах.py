def main():
    a, b, c = int(input()), int(input()), int(input())

    if a == 0 and b >= 0 and c >= 0 and b == c ** 2:
        print("MANY SOLUTIONS")
    elif c < 0 or a == 0:
        print("NO SOLUTION")
    else:
        if a != 0 and ((c ** 2 - b) / a) == (c ** 2 - b) // a:
            print((c ** 2 - b) // a)
        else:
            print("NO SOLUTION")

if __name__ == '__main__':
    main()