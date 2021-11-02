import random


def generate_grid():
    letters = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    grid = []
    while len(grid) < 5:
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
        if i[0] and i[0][0] in letters and len(i[0]) <= 5 and \
                'intj' not in i[1] and 'noninfl' not in i[1] and 'onomat' not in i[1]:
            for j in language_form:
                if j in i[1]:
                    i[1] = language_form[j]
            result.append(tuple(i))
    return result


def check_user_words(user_words, language_part, letters, dict_of_words):
    correct_words = []
    pure_words = []
    words = [i[0] for i in list(filter(lambda x: x[1] == language_part, dict_of_words))]
    for i in user_words:
        if i in words and i[0] in letters:
            correct_words.append(i)
    for i in words:
        if i not in correct_words:
            pure_words.append(i)
    return correct_words, pure_words


def main():
    language_form = random.choice(('verb', 'adverb', 'adjective', 'noun'))
    generated_letters = generate_grid()
    print(generated_letters)
    print(f'Language part: {language_form}')
    user_input = input('>>> ').split(' ')
    words = get_words('base.txt', generated_letters)
    print(check_user_words(user_input, language_form, generated_letters, words))


if __name__ == '__main__':
    main()