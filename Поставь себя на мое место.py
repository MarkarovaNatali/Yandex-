from sys import stdin
import json

with open('scoring.json', 'r', encoding='UTF-8') as file_in:
    data = json.load(file_in)
summ_point = 0
answ = [str(result).strip() for result in stdin]
n_test = 0
for group in data:
    for test in group['tests']:
        if test['pattern'] == answ[n_test]:
            summ_point += int(group['points'] / len(group['tests']))
        n_test += 1
print(summ_point)
