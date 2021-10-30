from typing import List
import string
import random


def random_words():
    letters = string.ascii_lowercase
    items = []
    while len(items) < 9:
        letter = random.choice(letters)
        if letter not in items:
            items.append(letter)
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
    return game_field


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(f, 'r') as file:
        for


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
