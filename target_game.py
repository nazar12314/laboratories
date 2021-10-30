from typing import List
import string
import random


def random_letters():
    """
    Generates random letters
    """
    letters = string.ascii_lowercase
    items = []
    while len(items) < 9:
        items.append(random.choice(letters))
    return items


def generate_grid(letters) -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    counter = 0
    game_field = []
    for i in range(3):
        game_field.append([])
        while len(game_field[i]) < 3:
            game_field[i].append(letters[counter].upper())
            counter += 1
    return game_field


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    words = []
    result = []
    center_letter = letters[4]
    with open(f, 'r') as file:
        for line in file:
            line = line.replace("\n", '')
            if len(line) >= 4:
                words.append(line)
    for word in words:
        if center_letter in word:
            word_letters = []
            for i in word:
                item = (i, word.count(i))
                if item not in word_letters:
                    word_letters.append(item)
            for i in range(len(word_letters)):
                if word_letters[i][0] in letters and word_letters[i][1] <= letters.count(word_letters[i][0]):
                    word_letters[i] = True
                else:
                    word_letters[i] = False
            if False not in word_letters:
                result.append(word.lower())

    return result


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    words = input(">>> ").split(' ')
    return words


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    wrong_words = []
    correct_words = []
    unused_words = []
    for i in user_words:
        if i not in words_from_dict:
            wrong_words.append(i)
        else:
            correct_words.append(i)
    for i in words_from_dict:
        if i not in user_words:
            unused_words.append(i)

    return wrong_words, len(correct_words), unused_words


def results(*args):
    """
    Write results into result.txt
    """
    with open('result.txt', 'w') as file:
        file.write(f'Correct words: {args[1]}\n')
        file.write('All words: \n')
        for i in args[3]:
            file.write(f'- {i} \n')
        file.write(f'Wrong words:\n')
        for i in args[0]:
            file.write(f'- {i} \n')
        file.write('Unused words:\n')
        for i in args[2]:
            file.write(f'- {i} \n')


def main():
    """
    main function. Executes all code
    """
    letters = random_letters()
    words = get_words('en.txt', letters)
    print(generate_grid(letters))
    user_input = get_user_words()
    a = get_pure_user_words(user_input, letters, words)
    results(a[0], a[1], a[2], words)


if __name__ == '__main__':
    main()
