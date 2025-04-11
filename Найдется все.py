""" Давайте вновь напишем небольшой компонент поисковой системы.

Формат ввода
Сначала вводится поисковый запрос.
Затем вводятся имена файлов, среди которых следует произвести поиск.

Формат вывода
Выведите все имена файлов, в которых есть поисковая строка без учета регистра и повторяющихся пробельных символов.
Если ни в одном файле информация не была найдена, выведите "404. Not Found".

Примечание
Система поиска должна обрабатывать строки "a&nbsp;&nbsp;&nbsp;&nbsp;b", "a b" и "a\nb" как одинаковые."""

from sys import stdin

find = ' '.join(elem.strip() for elem in input().lower().split())
found = []
files = [file.strip() for file in stdin]
for file in files:
    with open(file, 'r', encoding='UTF-8') as file_in:
        text = ' '.join(elem.strip() for elem in file_in.read().lower().split())
        if find in text:
            found.append(file)
if not found:
    print('404. Not Found')
else:
    print(*found, sep='\n')