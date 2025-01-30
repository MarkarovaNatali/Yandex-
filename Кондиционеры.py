def main():
    troom, tcond = map(int, input().split())
    rezhim = input().strip()
    if rezhim == 'auto':
        troom = tcond
    elif troom < tcond:
        if rezhim == 'heat':
            troom = tcond
    elif troom > tcond:
        if rezhim == 'freeze':
            troom = tcond
    print(troom)

if __name__ == '__main__':
    main()