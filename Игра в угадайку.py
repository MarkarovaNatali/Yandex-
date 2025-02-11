start, end = 0, 1001
number = (start + end) // 2
print(number)
while (answer := input()) != 'Угадал!':
    if answer == 'Больше':
        start = (start + end) // 2
    elif answer == 'Меньше':
        end = (start + end) // 2
    number = (start + end) // 2
    print(number)
