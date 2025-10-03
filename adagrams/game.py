from random import randint
from adagrams.homemade_functions import*

def draw_letters():
    weighted_letter_pool = multiply_letter_pool(LETTER_POOL)
    pool_length = len(weighted_letter_pool)
    
    drawn_letters = []
    purgatory_hand = {}
    drawn_letters_count = 0
    
    MAX_HAND_SIZE = 10
    
    while drawn_letters_count != MAX_HAND_SIZE:
        random_index = random.randint(0, pool_length - 1)
        letter = weighted_letter_pool[random_index]
        
        letter_count = 0
        if letter in purgatory_hand:
            letter_count = purgatory_hand[letter]
        
        if letter_count < LETTER_POOL[letter]:
            drawn_letters.append(letter)
            purgatory_hand[letter] = letter_count + 1
            drawn_letters_count += 1
            
    return drawn_letters

def uses_available_letters(word, letter_bank):
    upper_word = word.upper()
    word_dict = convert_to_dictionary(upper_word)
    hand_dict = convert_to_dictionary(letter_bank)
    
    for letter in word_dict:
        if (
            letter not in hand_dict 
            or word_dict[letter] > hand_dict[letter]
            ):
            return False
    return True
    

def score_word(word):
    upper_word = word.upper()
    word_played = convert_to_dictionary(upper_word)

    running_score = 0
    
    if len(word) >= 7:
        BONUS_SCORE = 8
        running_score += BONUS_SCORE
        
    for letter, count in word_played.items():
        running_score += count * SCORE_CHART[letter]
    
    return running_score

def get_highest_word_score(word_list):
    winning_word = ''
    high_score = 0
    
    for word in word_list:
        current_score = score_word(word)
        if current_score > high_score:
            high_score = current_score
            winning_word = word
        elif current_score == high_score:
            winning_word = tie_breaker(word, winning_word)
                        
    return winning_word, high_score