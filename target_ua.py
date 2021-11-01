import random


def generate_grid():
    letters = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    grid = []
    for _ in range(5):
        letter = random.choice(letters)
        if letter not in grid:
            grid.append(letter)
    return grid


def get_words(f, letters):
    items = []
    with open(f, 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            items.append(line.split(' ')[:2])
    for i in range(len(items)):
        if ('/n' or 'noun') in items[i][1]:
            items[i][1] = 'noun'
        elif '/adj' in items[i][1]:
            items[i][1] = 'adjective'
        elif '/v' in items[i][1]:
            items[i][1] = 'verb'
        elif 'adv' in items[i][1]:
            items[i][1] = 'adverb'
    return items


def check_user_words(user_words, language_part, letters, dict_of_words):
    pass


def main():
    pass

print(get_words('base.txt', 12))