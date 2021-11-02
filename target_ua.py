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
    result = []
    language_form = {'/n': 'noun', 'noun': 'noun', '/adj': 'adjective', 'adv': 'adverb', '/v': 'verb', 'verb': 'verb'}
    with open(f, 'r') as file:
        for line in file:
            line = line.lower().replace('\n', '')
            items.append(line.split(' ')[:2])
    for i in items:
        if i[0] and i[0][0] in letters and len(i[0]) <= 5 and\
                'intj' not in i[1] and 'noninfl' not in i[1] and 'onomat' not in i[1]:
            for j in language_form:
                if j in i[1]:
                    i[1] = language_form[j]
            result.append(tuple(i))
    return result


def check_user_words(user_words, language_part, letters, dict_of_words):
    pass


def main():
    pass


print(get_words('base.txt', generate_grid()))