"""Во многих задачах требуется контроль входных данных, в частности, несмотря на динамическую типизацию, их типов.

Разработайте декоратор same_type, который производит проверку переменного количества позиционных параметров.
В случае получения не одинаковых типов выводит сообщение "Обнаружены различные типы данных" и прерывает выполнение функции."""

def same_type(func):
    def decorated(*args):
        if all(isinstance(args[i - 1], type(args[i])) for i in range(1, len(args))):
            return func(*args)
        else:
            return print('Обнаружены различные типы данных')

    return decorated


@same_type
def combine_text(*words):
    return ' '.join(words)


print(combine_text('Hello,', 'world!') or 'Fail')
print(combine_text(2, '+', 2, '=', 4) or 'Fail')
print(combine_text('Список из 30', 0, 'можно получить так', [0] * 30) or 'Fail')
