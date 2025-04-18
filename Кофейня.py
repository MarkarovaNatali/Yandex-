"""Руководство местной кофейни для программистов под названием Java-0x00 решило модернизировать систему заказа кофе.

Для этого им требуется реализовать функцию order, которая принимает список предпочтений посетителя в порядке «убывания желания».

Согласно положению, каждый напиток в кофейне строго определён рецептом:

Эспрессо готовится из: 1 порции кофейных зерен.
Капучино готовится из: 1 порции кофейных зерен и 3 порций молока.
Макиато готовится из: 2 порций кофейных зерен и 1 порции молока.
Кофе по-венски готовится из: 1 порции кофейных зерен и 2 порций взбитых сливок.
Латте Макиато готовится из: 1 порции кофейных зерен, 2 порций молока и 1 порции взбитых сливок.
Кон Панна готовится из: 1 порции кофейных зерен и 1 порции взбитых сливок.
В глобальной переменной in_stock содержится словарь, описывающий ингредиенты в наличии. Ключи словаря: coffee, cream, milk.

Функция должна вернуть:

название напитка, который будет приготовлен;
сообщение «К сожалению, не можем предложить Вам напиток», если ни одно из предпочтений не может быть приготовлено.
Если заказ, может быть совершён, количество доступных ингредиентов должно соответствующим образом уменьшиться."""

import json

in_stock = input()
rem = json.loads(in_stock)


def order(*list_of_coffee):
    coffee = {"Эспрессо": {"coffee": 1}, "Капучино": {"coffee": 1, "milk": 3}, "Макиато": {"coffee": 2, "milk": 1},
              "Кофе по-венски": {"coffee": 1, "cream": 2}, "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
              "Кон Панна": {"coffee": 1, "cream": 1}}
    for kind in list_of_coffee:
        if all(coffee[kind][key] <= rem[key] for key in coffee[kind].keys()):
            for key in coffee[kind].keys():
                new = rem[key] - coffee[kind][key]
                rem[key] = new
            return kind
    return "К сожалению, не можем предложить Вам напиток"


print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
print(order("Капучино", "Макиато", "Эспрессо"))
