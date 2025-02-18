prev = 0  # для хранения предыдущего хеша
bad = -1  # для хранения номера "плохого" блока
for index in range(int(input())):
    block = int(input())
    hn = block % 256
    rn = (block // 256) % 256
    mn = block // 256 ** 2
    hn_calc = (37 * (mn + rn + prev)) % 256
    if hn != hn_calc or hn >= 100:
        bad = index
        break
    prev = hn
print(bad)



