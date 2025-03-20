from itertools import product, combinations

cards = [str(i) for i in range(2, 11)] + ['валет', 'дама', 'король', 'туз']
cards_suit = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
cards.sort()
suit = input()
cards.remove(input())
s = product(cards, sorted(cards_suit.values()))
index = 1
for combi in combinations(s, r=3):
    for i in range(3):
        if combi[i][1] == cards_suit[suit] and index <= 10:
            print(', '.join([f'{x} {y}' for x, y in combi]))
            index += 1
            break
