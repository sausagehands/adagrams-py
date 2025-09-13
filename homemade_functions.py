import random
from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

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
    
    


sample_list = ['d','o','g','g']
convert_to_dictionary(sample_list)