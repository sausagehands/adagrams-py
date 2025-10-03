import random
from random import randint
from adagrams.constants import*

def multiply_letter_pool(LETTER_POOL):
    weighted_letters =[]
    for letter, amount in LETTER_POOL.items():
        grouped_letters = [letter] * amount
        weighted_letters.extend(grouped_letters)
    return weighted_letters


def convert_to_dictionary(list):
    dictionary = {}
    for letter in list:
        dictionary[letter] = dictionary.get(letter, 0) + 1
    return dictionary


def tie_breaker(current_word, winning_word):
    length_current = len(current_word)
    length_winning = len(winning_word)
    
    if length_current == 10 and length_winning != 10:
        return current_word
    elif length_winning == 10 and length_current != 10: 
        return winning_word
    #if neither word is 10 characters, shorter word wins
    elif length_winning > length_current:
        return current_word
    #if length_current == length_highest
    else:
        return winning_word