import random
from random import randint
from constants import*

def convert_to_list(word):
    deconstructed_word = []
    for letter in word:
        deconstructed_word.append(letter.upper())
    return deconstructed_word

# def count_same_letters(list_to_count):
#     count = 0
#     index = 0
    
#     while index < list_length(list_to_count):
#         current_letter = list_to_count[index]
#         if list_to_count[index] == current_letter:
#             count += 1
#         index += 1
#     return count

def get_sum ():
    pass

def list_length(list_to_count):
    count = 0
    for i in list_to_count:
        count += 1
    return count

def multiply_letter_bank(letter_bank):
    weighted_letters =[]
    for letter, amount in letter_bank.items():
        grouped_letters = letter * amount
        for letters in convert_to_list(grouped_letters):
            weighted_letters.append(letters)
    return weighted_letters


def draw_hand():
    final_letter_list = multiply_letter_bank(LETTER_POOL)
    drawn_letters = []
    for i in range(10):
        random_index = [random.randint(0, list_length(multiply_letter_bank(LETTER_POOL)) + 1)]
        for i in random_index:
            drawn_letters.append(final_letter_list[i])
    return drawn_letters
    
#need to finish this for draw letters-- right direction?
# def letter_frequency(letter_bank):
#     for letter, amount in letter_bank.items():
#         if letter in draw_hand():
#             list_length(draw_hand())
            
# def check_letter_overlap(word):
#     word_submission = convert_to_list(word)
#     #get count of each letter in word submission
#     #& count of each letter in hand & subtract hand - submission >= 0
    
#     for letter in word_submission:
#         if letter not in draw_hand():
#             return False
#         else: 
#             pass
            
            
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
            
                
            
        
        

scoring('dog')