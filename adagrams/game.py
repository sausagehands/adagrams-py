from random import randint
from homemade_functions import*

def draw_letters():
    chosen_letters = draw_hand()
    return chosen_letters

def uses_available_letters(word, letter_bank):
    word_list = convert_to_list(word)
    word_dict = convert_to_dictionary(word_list)
    hand_dict = convert_to_dictionary(letter_bank)
    return compare_word_to_hand(word_dict, hand_dict)
    

def score_word(word):
    return scoring(word)

def get_highest_word_score(word_list):
    return highest_score(word_list)