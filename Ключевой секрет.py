"""Вася любит секреты и шифрование. Он часто пользуется шифром на основе замен и просит разработать вас функцию,
которая позволит ему быстро шифровать сообщения.
Напишите функцию secret_replace(text, **replaces), которая принимает:
текст требующий шифрования;
именованные аргументы — правила замен, представляющие собой кортежи из одного или нескольких значений.
Функция должна вернуть зашифрованный текст."""

def secret_replace(text, **replaces):
    list_text = list(text)
    new_text = list_text.copy()
    for i in replaces.keys():
        count = 1
        for index, j in enumerate(list_text):
            if j == i:
                new_text[index] = replaces[i][count - 1]
                count = count % len(replaces[i]) + 1
    return ''.join(new_text)

result = secret_replace(
    "ABRA-KADABRA",
    A=("Z", "1", "!"),
    B=("3",),
    R=("X", "7"),
    K=("G", "H"),
    D=("0", "2"),
)
print(result)