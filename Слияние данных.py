"""Одна местная компания производит обновление данных о пользователях и заодно решили реорганизовать систему хранения.

Напишите программу, которая обновляет данные о пользователях, записанных в JSON файле.

Формат ввода
Пользователь вводит два имени файла.
В первом хранится JSON массив пользователей.
Во втором — массив новых данных.

Информация о каждом пользователе представляется JSON объектом, в котором обязательно присутствует поле name, описывающее имя пользователя. Остальные поля являются дополнительными.

Формат вывода
В первый файл запишите информацию о пользователях в виде JSON объекта, ключами которого выступают имена пользователей, а значениями — объекты с информацией о них.

Если какая-либо дополнительная информация о пользователе изменяется, то требуется сохранить лексикографически большее значение."""

import json

inter_1 = input()
inter_2 = input()
with open(inter_1, 'r', encoding='UTF-8') as file_in:
    data = json.load(file_in)
with open(inter_2, 'r', encoding='UTF-8') as file_upd:
    data_upd = json.load(file_upd)
data_res = dict()
print(data_upd)
for inform in data:
    data_res[inform.pop('name')] = inform
for dic in data_upd:
    val = dic.pop('name')
    for key in dic.keys():
        data_res[val][key] = max(dic.get(key, str()), data_res[val].get(key, str()))
print(data_res)
with open(inter_1, 'w', encoding='UTF-8') as file_out:
    json.dump(data_res, file_out, ensure_ascii=False, indent=2)

