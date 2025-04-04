"""Продолжим работу с таблицами истинности.
К сожалению, некоторые из операций Булевой алгебры не реализованы в Python.
Самые частые не стандартные операции это: импликация, строгая дизъюнкция и эквивалентность.

Обозначим их следующим образом:

импликация — ->;
строгая дизъюнкция — ^;
эквивалентность — ~.
Напишите программу, которая для введённого сложного логического высказывания строит таблицу истинности.

Формат ввода
Вводится логическое выражение от нескольких переменных.

Возможное содержание выражения:

Заглавная латинская буква — переменная;
not — отрицание;
and — конъюнкция;
or — дизъюнкция;
^ — строгая дизъюнкция;
-> — импликация;
~ — эквивалентность;
() — логические скобки.
Формат вывода
Выведите таблицу истинности данного выражения."""

from itertools import product


def func(vvod, dic):
    for key in dic.keys():
        vvod = vvod.replace(key, str(dic[key]))
    st = list(vvod.split())
    leaght = len(st) - st.count('not')
    i = 0
    while i < leaght:
        if st[i] == 'not':
            x = int(st.pop(i + 1))
            st[i] = int(not x)
        i += 1
    leaght = len(st) - st.count('and') * 2
    i = 1
    while i <= leaght:
        if len(st) > leaght:
            if st[i] == 'and':
                x = int(st.pop(i - 1))
                y = int(st.pop(i))
                st[i - 1] = x and y
                i -= 1
        i += 1
    i = 1
    leaght = len(st) - st.count('or') * 2 - st.count('^') * 2
    while i <= leaght:
        if len(st) > leaght:
            if st[i] == 'or':
                x = int(st.pop(i - 1))
                y = int(st.pop(i))
                st[i - 1] = x or y
                i -= 1
            if st[i] == '^':
                x = int(st.pop(i - 1))
                y = int(st.pop(i))
                if x != y:
                    st[i - 1] = 1
                    i -= 1
                else:
                    st[i - 1] = 0
                    i -= 1
        i += 1
    i = 1
    leaght = len(st) - st.count('->') * 2 - st.count('~') * 2
    while i <= leaght:
        if len(st) > leaght:
            if st[i] == '->':
                x = int(st.pop(i - 1))
                y = int(st.pop(i))
                if x <= y:
                    st[i - 1] = 1
                    i -= 1
                else:
                    st[i - 1] = 0
                    i -= 1
            if st[i] == '~':
                x = int(st.pop(i - 1))
                y = int(st.pop(i))
                if x == y:
                    st[i - 1] = 1
                    i -= 1
                else:
                    st[i - 1] = 0
                    i -= 1
        i += 1
    return st


if __name__ == '__main__':
    stroka = input()
    var_all = sorted(list({v for v in stroka if v.isupper()}))
    print(*var_all, 'F')
    res = {}
    for combi in product([0, 1], repeat=len(var_all)):
        for i in range(len(var_all)):
            res[var_all[i]] = combi[i]
        stroka_2 = stroka
        while '(' in stroka_2:
            in_breakets = stroka_2
            while '(' in in_breakets:
                br_1 = in_breakets.find('(')
                in_breakets = in_breakets[br_1 + 1::]
            br_2 = in_breakets.find(')')
            in_breakets = in_breakets[:br_2:]
            if len(in_breakets) > 0:
                rep = func(in_breakets, res)
                in_br = '(' + in_breakets + ')'
                stroka_2 = stroka_2.replace(in_br, str(*rep))
        print(*combi, *func(stroka_2, res))
