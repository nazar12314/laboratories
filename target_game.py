from typing import List
import string
import random


def random_words():
    letters = string.ascii_lowercase
    items = []
    while len(items) < 9:
        items.append(random.choice(letters))
    return items


def generate_grid():
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters = random_words()
    counter = 0
    game_field = []
    for i in range(3):
        game_field.append([])
        while len(game_field[i]) < 3:
            game_field[i].append(letters[counter].upper())
            counter += 1
    words = get_words('en.txt', letters)


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
    pass


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass


print(generate_grid())