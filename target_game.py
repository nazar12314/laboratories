from typing import List
import string
import random

LETTERS = string.ascii_lowercase
ITEMS = [random.choice(LETTERS) for _ in range(9)]


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    counter = 0
    game_field = []
    for i in range(3):
        game_field.append([])
        while len(game_field[i]) < 3:
            game_field[i].append(ITEMS[counter].upper())
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
                words.append(line.lower())
    for word in words:
        if center_letter in word:
            word_letters = []
            for i in word:
                item = (i, word.count(i))
                if item not in word_letters:
                    word_letters.append(item)
            for i in range(len(word_letters)):
                if word_letters[i][0] in letters and\
                        word_letters[i][1] <= letters.count(word_letters[i][0]):
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


def get_pure_user_words(user_words: List[str], letters: List[str],
words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    center_letter = letters[4]
    pure_words = []
    for word in user_words:
        if len(word) >= 4 and center_letter in word \
                and word not in words_from_dict:
            used_letters = []
            for i in word:
                item = (i, word.count(i))
                if item not in used_letters:
                    used_letters.append(item)
            for i in range(len(used_letters)):
                if used_letters[i][0] in letters and used_letters[i][1] <= letters.count(used_letters[i][0]):
                    used_letters[i] = True
                else:
                    used_letters[i] = False
            if False not in used_letters:
                pure_words.append(word)

    return pure_words


def results(*args):
    """
    Write results into result.txt
    """
    with open('result.txt', 'w') as file:
        file.write('All words: \n')
        for i in args[1]:
            file.write(f'- {i} \n')
        file.write('Pure words:\n')
        for i in args[0]:
            file.write(f'- {i} \n')
        file.write('Your input:\n')
        for i in args[2]:
            file.write(f'- {i} \n')


# def main():
#     """
#     main function. Executes all code
#     """
#     words = get_words('en.txt', ITEMS)
#     print(generate_grid())
#     user_input = get_user_words()
#     a = get_pure_user_words(user_input, ITEMS, words)
#     results(a, words, user_input)
#     print(user_input)
#     print(a)


print(get_words('en.txt', [el for el in 'vhtdsrael']))

# if __name__ == '__main__':
#     main()
