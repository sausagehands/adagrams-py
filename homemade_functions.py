import random
from random import randint
from constants import*


def convert_to_list(word):
    deconstructed_word = []
    for letter in word:
        deconstructed_word.append(letter.upper())
    return deconstructed_word


def list_length(list_to_count):
    count = 0
    for i in list_to_count:
        count += 1
    return count

def multiply_letter_pool(LETTER_POOL):
    weighted_letters =[]
    for letter, amount in LETTER_POOL.items():
        grouped_letters = letter * amount
        for letters in convert_to_list(grouped_letters):
            weighted_letters.append(letters)
    return weighted_letters


def draw_hand():
    final_letter_pool = multiply_letter_pool(LETTER_POOL)
    pool_length = list_length(final_letter_pool)
    drawn_letters = []
    purgatory_hand = {}
    drawn_letters_count = 0
    while drawn_letters_count != 10:
        random_index = random.randint(0, pool_length - 1)
        letter = final_letter_pool[random_index]
        
        letter_count = 0
        if letter in purgatory_hand:
            letter_count = purgatory_hand[letter]
        
        if letter_count < LETTER_POOL[letter]:
            drawn_letters.append(letter)
            purgatory_hand[letter] = letter_count + 1
            drawn_letters_count += 1
            
    return drawn_letters

def convert_to_dictionary(list):
    dictionary = {}
    for letter in list:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    return dictionary

def compare_word_to_hand(word_dict, hand_dict):
    for letter in word_dict:
        if letter not in hand_dict:
            return False
        elif word_dict[letter] > hand_dict[letter]:
            return False
    return True

def scoring(word):
    word_length = list_length(convert_to_list(word))
    word_played = convert_to_dictionary(convert_to_list(word))
    
    score = 0
    
    if word_length >= 7:
        score += 8
    for letter, count in word_played.items():
        for letters, points in SCORE_CHART.items():
            if letter in letters:
                score += word_played[letter] * SCORE_CHART[letters]
                break
    return score
        
    
def highest_score(word_list):
    winning_word = ''
    high_score = 0
    
    for word in word_list:
        current_score = scoring(word)
        if current_score > high_score:
            high_score = current_score
            winning_word = word
        elif current_score == high_score:
            length_current_word = list_length(convert_to_list(word))
            length_winning_word = list_length(convert_to_list(winning_word))
            
            if length_current_word == 10 and length_winning_word != 10:
                winning_word = word
            elif length_winning_word == 10 and length_current_word != 10: 
                winning_word = winning_word
            elif length_winning_word > length_current_word:
                winning_word = word
                
    return winning_word, high_score