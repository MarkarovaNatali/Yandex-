"""Весьма часто, данные, которые мы получаем из различных источников, не удовлетворяют нашим пожеланиям.
Одна из частых проблем – излишняя вложенность списков.

Напишите функцию make_linear, которая принимает список списков и возвращает его "выпрямленное" представление."""


def make_linear(args, straight=None):
    if straight is None:
        straight = []
    if not args:
        return straight
    first, *rest = args
    if isinstance(first, list):
        return make_linear(first + rest, straight)
    else:
        straight.append(first)
        return make_linear(rest, straight)


print(make_linear([1, [2, [3, 4]], 5, 6]))
