def result_accumulator(func):
    summ = []

    def decorated(*args, method="accumulate"):
        nonlocal summ
        summ.append(func(*args))
        if method == "drop":
            exit_value = summ.copy()
            summ.clear()
            return exit_value

    return decorated


@result_accumulator
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
print(get_letters('Ехали медведи на велосипеде', method='drop'))
