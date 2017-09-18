# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:


def clean_message(message):
    ''' (str) -> str

    The function will return a copy of the input message which only includes
    alphabetical characters, and all the characters will convert to uppercase.

    REQ: type(message) == str

    >>> clean_message('aA,bB,cC,dD')
    'AABBCCDD'
    >>> clean_message('Python Type "help","copyright","credits"')
    'PYTHONTYPEHELPCOPYRIGHTCREDITS'
    '''
    # initialize the result string
    result = ''
    # determine each character in the input str
    for element in message:
        # only add letters into result, and letters are uppercase
        if element.isalpha():
            result += element.upper()
    return result


def encrypt_letter(letter, keystream_value):
    ''' (str, int) -> str

    The function will receive two parameters, the first parameter is a single
    letter and the second parameter is a keystream vaue.
    The function will clean the letter first, to make sure the letter
    finally is uppercase.
    The function will apply the keystream value to the character to
    encrypt the character, and return the encrypted character.
    The function will get the order of the letters and matching them
    from 0-25

    REQ: letter only can contain one alphabet

    >>> encrypt_letter('a', 9)
    'J'
    >>> encrypt_letter('z', 1)
    'A'
    >>> encrypt_letter('X', 6)
    'D'
    >>> encrypt_letter('L', 12)
    'X'
    >>> encrypt_letter('A', 8)
    'I'
    >>> encrypt_letter('K', 17)
    'B'
    >>> encrypt_letter('E', 25)
    'D'
    >>> encrypt_letter('H', 1)
    'I'
    >>> encrypt_letter('Y', 14)
    'M'
    >>> encrypt_letter('L', 15)
    'A'
    >>> encrypt_letter('I', 13)
    'V'
    >>> encrypt_letter('A', 20)
    'U'
    '''
    # clean the letter by calling the function clean_message
    letter = clean_message(letter)
    # get the matching value using the order of letters
    letter_value = ord(letter) - 65
    # apply keystream_value to the letter, and get encrypted_value
    encrypted_value = (letter_value + keystream_value) % 26
    # get the matching letter using the matching order of the letters
    encrypted_letter = chr(encrypted_value+65)
    return encrypted_letter


def decrypt_letter(letter, keystream_value):
    ''' (str, int) -> str

    The function will receive two parameters, the first parameter is a single
    character and the second parameter representes a keystream vaue.
    The function will apply the keystream value to the character to
    decrypt the character, and return the decrypted character.
    The function will get the order of the letters and matching them
    from 0-25.

    REQ: letter only can contain one alphabet

    >>> decrypt_letter('X', 12)
    'L'
    >>> decrypt_letter('I', 8)
    'A'
    >>> decrypt_letter('B', 17)
    'K'
    >>> decrypt_letter('D', 25)
    'E'
    >>> decrypt_letter('I', 1)
    'H'
    >>> decrypt_letter('M', 14)
    'Y'
    >>> decrypt_letter('A', 15)
    'L'
    >>> decrypt_letter('V', 13)
    'I'
    >>> decrypt_letter('U', 20)
    'A'
    '''
    # clean the letter by calling the function clean_message
    letter = clean_message(letter)
    # get the matching value using the order of letters
    letter_value = ord(letter) - 65
    # apply keystream_value to the letter, and get decrypted_value
    decrypted_value = (letter_value + 26 - keystream_value) % 26
    # get the matching letter using the matching order of the letters
    decrypted_letter = chr(decrypted_value+65)
    return decrypted_letter


def swap_cards(deck_of_cards, index):
    ''' (list of int, int) -> NoneType

    The first parameter represents a deck of cards and the second represents
    an index into the deck.
    The function will swap the card at the index with the card
    that follos it, and it treats the deck as circular.
    The function will only mutate the deck and return nothing.

    REQ: type of deck_of_cards is a list of int
    REQ: len(deck_of_cards) == 28
    REQ: int in dec_of_cards from 1-28 can only appear once
    REQ: index >= 0 and index < 28

    >>> cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> swap_cards(cards, 7)
    >>> cards == [1, 2, 3, 4, 5, 6, 7, 9, 8, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    True

    >>> cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> swap_cards(cards, 27)
    >>> cards == [28, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 1]
    True
    '''
    # get the index value
    tem = deck_of_cards[index]
    # determine if the index is pointing to the end of the list
    if tem == deck_of_cards[-1]:
        # swap the card with the first card
        deck_of_cards[index] = deck_of_cards[0]
        deck_of_cards[0] = tem
    # when it is not the first value
    else:
        # swap the card with the following one
        deck_of_cards[index] = deck_of_cards[index+1]
        deck_of_cards[index+1] = tem
    return None


def move_joker_1(deck_of_cards):
    ''' (list of int) -> NoneType

    This function is the first step of the algorithm.
    The function will find the JOKER1, and swap it with the next card.
    It treats cards as circular.
    The function will only mutate deck_of_cards and return nothing.

    REQ: type of deck_of_cards is a list of int
    REQ: len(deck_of_cards) == 28
    REQ: int in dec_of_cards from 1-28 can only appear once
    REQ: the value of JOKER1 has to be in the deck_of_cards

    >>> cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    >>> move_joker_1(cards)
    >>> cards == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 27]
    True

    >>> cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 27]
    >>> move_joker_1(cards)
    >>> cards == [27, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 1]
    True
    '''
    # find the index of JOKER1 and call swap_cards
    index_JOKER1 = deck_of_cards.index(JOKER1)
    swap_cards(deck_of_cards, index_JOKER1)
    return None


def move_joker_2(deck_of_cards):
    ''' (list of int) -> NoneType

    This function is the second step of the algorithm.
    The function will find the JOKER2, and move it two cards down by
    calling the swap_cards twice.
    It states cards as circular.
    The function will only mutate deck_of_cards and return nothing.
    The function will get the result by calling the function swap_cards
    twice.

    REQ: type of deck_of_cards is a list of int
    REQ: len(deck_of_cards) == 28
    REQ: int in dec_of_cards from 1-28 can only appear once
    REQ: the value of JOKER2 has to be in the deck_of_cards

    >>> cards = [27, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 28, 24, 26, 25, 1]
    >>> move_joker_2(cards)
    >>> cards == [27, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 26, 28, 25, 1]
    True

    >>> cards = [27, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 26, 25, 28, 1]
    >>> move_joker_2(cards)
    >>> cards == [28, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 26, 25, 1, 27]
    True

    >>> cards = [27, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 26, 25, 1, 28]
    >>> move_joker_2(cards)
    >>> cards == [2, 28, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
    18, 19, 20, 21, 22, 23, 24, 26, 25, 1, 27]
    True
    '''
    # find the index of JOKER2 and call swap_cards
    index_JOKER2 = deck_of_cards.index(JOKER2)
    swap_cards(deck_of_cards, index_JOKER2)
    # find new index of JOKER1 and call swap_cards again
    index_JOKER2 = deck_of_cards.index(JOKER2)
    swap_cards(deck_of_cards, index_JOKER2)
    return None


def triple_cut(deck_of_cards):
    ''' (list of int) -> NoneType

    This function is the third step of the algorithm.
    The function will find two jokers, JOKER1 and JOKER2 and do a triple cut.
    The function will swaps the cards above the first joker with the cards
    below thesecond joker by slicing.
    The function will only mutate deck_of_cards and return nothing.

    REQ: type of deck_of_cards is a list of int
    REQ: len(deck_of_cards) == 28
    REQ: int in dec_of_cards from 1-28 can only appear once
    REQ: the value of JOKER1 and JOKER2 has to be in the deck_of_cards

    >>> cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,\
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> triple_cut(cards)
    >>> cards == [2, 5, 8, 11, 14, 17, 20, 23, 26, 28, 3, 6, 9, 12, 15, 18,\
    21, 24, 27, 1, 4, 7, 10, 13, 16, 19, 22, 25]
    True

    >>> cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 27, 3, 6, 9, 12, 15, 18,\
    21, 24, 28, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> triple_cut(cards)
    >>> cards == [2, 5, 8, 11, 14, 17, 20, 23, 26, 27, 3, 6, 9, 12, 15, 18,\
    21, 24, 28, 1, 4, 7, 10, 13, 16, 19, 22, 25]
    True

    >>> cards = [28, 1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 9, 12, 15, 18,\
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> triple_cut(cards)
    >>> cards == [2, 5, 8, 11, 14, 17, 20, 23, 26, 28, 1, 4, 7, 10, 13, 16,\
    19, 22, 25, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    True

    >>> cards = [27, 1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 9, 12, 15, 18,\
    21, 24, 28, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> triple_cut(cards)
    >>> cards == [2, 5, 8, 11, 14, 17, 20, 23, 26, 27, 1, 4, 7, 10, 13, 16,\
    19, 22, 25, 3, 6, 9, 12, 15, 18, 21, 24, 28]
    True

    >>> cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,\
    21, 24, 26, 2, 5, 8, 11, 14, 17, 20, 23, 27]
    >>> triple_cut(cards)
    >>> cards == [28, 3, 6, 9, 12, 15, 18, 21, 24, 26, 2, 5, 8, 11, 14, 17,\
    20, 23, 27, 1, 4, 7, 10, 13, 16, 19, 22, 25]
    True

    >>> cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 27, 3, 6, 9, 12, 15, 18,\
    21, 24, 26, 2, 5, 8, 11, 14, 17, 20, 23, 28]
    >>> triple_cut(cards)
    >>> cards == [27, 3, 6, 9, 12, 15, 18, 21, 24, 26, 2, 5, 8, 11, 14, 17,\
    20, 23, 28, 1, 4, 7, 10, 13, 16, 19, 22, 25]
    True

    >>> cards = [27, 4, 7, 10, 13, 16, 19, 22, 25, 26, 3, 6, 9, 12, 15, 18,\
    21, 24, 1, 2, 5, 8, 11, 14, 17, 20, 23, 28]
    >>> triple_cut(cards)
    >>> cards == [27, 4, 7, 10, 13, 16, 19, 22, 25, 26, 3, 6, 9, 12, 15, 18,\
    21, 24, 1, 2, 5, 8, 11, 14, 17, 20, 23, 28]
    True

    >>> cards = [28, 4, 7, 10, 13, 16, 19, 22, 25, 26, 3, 6, 9, 12, 15, 18,\
    21, 24, 1, 2, 5, 8, 11, 14, 17, 20, 23, 27]
    >>> triple_cut(cards)
    >>> cards == [28, 4, 7, 10, 13, 16, 19, 22, 25, 26, 3, 6, 9, 12, 15, 18,\
    21, 24, 1, 2, 5, 8, 11, 14, 17, 20, 23, 27]
    True

    >>> cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 12, 3, 6, 9, 28, 27, 18,\
    21, 24, 15, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> triple_cut(cards)
    >>> cards == [18, 21, 24, 15, 2, 5, 8, 11, 14, 17, 20, 23, 26, 28, 27,\
    1, 4, 7, 10, 13, 16, 19, 22, 25, 12, 3, 6, 9]
    True

    >>> cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 12, 3, 6, 9, 27, 28, 18,\
    21, 24, 15, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> triple_cut(cards)
    >>> cards == [18, 21, 24, 15, 2, 5, 8, 11, 14, 17, 20, 23, 26, 27, 28,\
    1, 4, 7, 10, 13, 16, 19, 22, 25, 12, 3, 6, 9]
    True
    '''
    # get the index of two jokers
    index_JOKER1 = deck_of_cards.index(JOKER1)
    index_JOKER2 = deck_of_cards.index(JOKER2)
    # when JOKER1 appears before JOKER2
    if index_JOKER1 < index_JOKER2:
        # swap top cards with bottom cards
        deck_of_cards[:] = deck_of_cards[index_JOKER2+1:] + deck_of_cards[
            index_JOKER1:index_JOKER2+1] + deck_of_cards[:index_JOKER1]
    # when JOKER2 appears before JOKER1
    else:
        # swap top cards with bottom cards
        deck_of_cards[:] = deck_of_cards[index_JOKER1+1:] + deck_of_cards[
            index_JOKER2:index_JOKER1+1] + deck_of_cards[:index_JOKER2]
    return None


def insert_top_to_bottom(deck_of_cards):
    ''' (list of int) -> NoneType

    This function is the forth step of the algorithm.
    The function will look at the end of the cards from the deck, and
    take that value as num_cards, and then take the value of num_card cards
    from the begining of deck,
    and put them at the end of the deck but before the last element.
    Special case: if the last card is JOKER2, the we treat num_cards as JOKER1.
    The function will only mutate deck_of_cards and return nothing.

    REQ: type of deck_of_cards is a list of int
    REQ: len(deck_of_cards) == 28
    REQ: int in dec_of_cards from 1-28 can only appear once

    >>> cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,\
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> insert_top_to_bottom(cards)
    >>> cards == [23, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,\
    18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 26]
    True

    >>> cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,\
    21, 24, 26, 2, 5, 8, 11, 14, 17, 20, 23, 27]
    >>> insert_top_to_bottom(cards)
    >>> cards == [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,\
    21, 24, 26, 2, 5, 8, 11, 14, 17, 20, 23, 27]
    True

    >>> cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 9, 12, 15, 18,\
    21, 24, 26, 2, 5, 8, 11, 14, 17, 20, 23, 27, 28]
    >>> insert_top_to_bottom(cards)
    >>> cards == [1, 4, 7, 10, 13, 16, 19, 22, 25, 3, 6, 9, 12, 15, 18,\
    21, 24, 26, 2, 5, 8, 11, 14, 17, 20, 23, 27, 28]
    True
    '''
    # get the value of the last card
    num_cards = deck_of_cards[-1]
    # when the last card is JOKER2, the we treat num_cards as JOKER1
    if num_cards == JOKER2:
        num_cards = JOKER1
    # move top cards to the bottom but before last value
    deck_of_cards[:] = deck_of_cards[num_cards:-1] + deck_of_cards[:num_cards]\
        + deck_of_cards[-1:]
    return None


def get_card_at_top_index(deck_of_cards):
    ''' (list of int) -> int

    This function is the fifth step of the algorithm.
    The function will look at the top card from the deck, and
    use the first card value as an index, and return the value of card that
    matches that index.
    Special case: if the top card is JOKER2, it wil use JOKER1.
    The function will return a card value

    REQ: type of deck_of_cards is a list of int
    REQ: len(deck_of_cards) == 28
    REQ: int in dec_of_cards from 1-28 can only appear once

    >>> get_card_at_top_index([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6,\
    9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    4

    >>> cards = [JOKER2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,\
    16, 17, 18, 19, 20, 21, 22, 23, 24, JOKER1, 25, 26]
    >>> get_card_at_top_index(cards)
    26

    >>> cards = [JOKER2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,\
    16, 17, 18, 19, 20, 21, 22, 23, 24, JOKER1, 25, 26]
    >>> get_card_at_top_index(cards)
    26

    >>> get_card_at_top_index([23, 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3,\
    6, 9, 12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 26])
    11
    '''
    # get the value of the first cards as index
    index = deck_of_cards[0]
    # if index is JOKER2, then we treat it as JOKER1
    if index == JOKER2:
        index = JOKER1
    # get the specific card
    result = deck_of_cards[index]
    return result


def get_next_value(deck_of_cards):
    ''' (list of int) -> int

    This is the function that contains all five steps of the algorithm, so
    it is a whole algorithm.
    The function will return the next potential keystream value, but this
    value may not be valid.

    REQ: type of deck_of_cards is a list of int
    REQ: len(deck_of_cards) == 28
    REQ: int in dec_of_cards from 1-28 can only appear once

    >>> cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,\
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> get_next_value(cards)
    11
    >>> get_next_value(cards)
    9
    >>> get_next_value(cards)
    23
    >>> get_next_value(cards)
    7
    >>> get_next_value(cards)
    10
    >>> get_next_value(cards)
    25
    >>> get_next_value(cards)
    11
    >>> get_next_value(cards)
    11
    >>> get_next_value(cards)
    7
    >>> get_next_value(cards)
    27
    >>> get_next_value(cards)
    8
    '''
    # repeat four steps
    move_joker_1(deck_of_cards)
    move_joker_2(deck_of_cards)
    triple_cut(deck_of_cards)
    insert_top_to_bottom(deck_of_cards)
    # let result equals to next keysteam value
    result = get_card_at_top_index(deck_of_cards)
    return result


def get_next_keystream_value(deck_of_cards):
    ''' (list of int) -> int

    This function will repeat all five steps by calling the function
    get_next_value until a valid keystream value is prodeced,
    which means that keystream value is in the range 1-

    REQ: type of deck_of_cards is a list of int
    REQ: len(deck_of_cards) == 28
    REQ: int in dec_of_cards from 1-28 can only appear once

    >>> cards = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18,\
    21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> get_next_keystream_value(cards)
    11
    >>> get_next_keystream_value(cards)
    9
    >>> get_next_keystream_value(cards)
    23
    >>> get_next_keystream_value(cards)
    7
    >>> get_next_keystream_value(cards)
    10
    >>> get_next_keystream_value(cards)
    25
    >>> get_next_keystream_value(cards)
    11
    >>> get_next_keystream_value(cards)
    11
    >>> get_next_keystream_value(cards)
    7
    >>> get_next_keystream_value(cards)
    8
    >>> get_next_keystream_value(cards)
    9
    '''
    # initializa result
    result = 0
    # call get_next_value until get a valid keystream value
    while not (result in range(1, 27)):
        result = get_next_value(deck_of_cards)
    return result


def process_message(deck_of_cards, message, order):
    ''' (list of int, str, str) -> str

    The function receive three parameters.
    The first one is a deck of cards which is used to get the keystream value.
    The second is the massage which is used to encrypt or decrypt
    the last one is order, to encrypt or decrypt is based on this parameter,
    and if order is 'e', then it is encrypt.
    If order is 'd', then do the decrypt.

    REQ: type of deck_of_cards is a list of int
    REQ: len(deck_of_cards) == 28
    REQ: int in deck_of_cards from 1-28 can only appear once
    REQ: order must be 'e' or 'd'

    >>> process_message([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,\
    18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26], 'did you get up?', 'e')
    'ORAFYTRPACY'

    >>> process_message([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,\
    18,21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26], 'ORAFYTRPACY', 'd')
    'DIDYOUGETUP'

    >>> process_message([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,\
    18,21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26], 'RXLKVTNV', 'd')
    'GOODLUCK'
    '''
    # clean the message first
    message = clean_message(message)
    # initialize the keystream value and the result
    keystream_value = []
    result = ''
    # for how many letters we have in message, get how many keystream value
    while len(keystream_value) < len(message):
        next_keystream_value = get_next_keystream_value(deck_of_cards)
        keystream_value.append(next_keystream_value)
    # initialize i for encryption and decryption in while loop
    i = 0
    # when order is 'e', do the encrypt
    if order == 'e':
        while i < len(message):
            result += encrypt_letter(message[i], keystream_value[i])
            i += 1
    # when order is 'd', do the decrypt
    elif order == 'd':
        while i < len(message):
            result += decrypt_letter(message[i], keystream_value[i])
            i += 1
    return result


def process_messages(deck_of_cards, messages, order):
    ''' (list of int, list of str, str) -> list of str

    The function will encrypt or decrypt a list of message by calling
    previous function that is process_message.
    Rather than encrypt or decrypt a str, this function will do a list
    of str, so the second parameter should be a list of str.
    If order is 'd', then do the decrypt.

    REQ: type of deck_of_cards is a list of int
    REQ: len(deck_of_cards) == 28
    REQ: int in deck_of_cards from 1-28 can only appear once
    REQ: order must be 'e' or 'd'

    >>> process_messages([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,\
    15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26], ['did', 'you',\
    'get', 'up?'], 'e')
    ['ORA', 'FYT', 'RPA', 'CY']

    >>> process_messages([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,\
    15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26], ['ORA', 'FYT',\
    'RPA', 'CY'], 'd')
    ['DID', 'YOU', 'GET', 'UP']

    process_messages([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15,\
    18,21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26], ['RXLK', 'VTNV'], 'd')
    ['GOOD', 'LUCK']
    '''
    # initialize result as a list
    result = []
    # for each message in messages to encrypt or decrypt and add into result
    for message in messages:
        result.append(process_message(deck_of_cards, message, order))
    return result


def read_messages(open_file):
    ''' (file open for reading) -> list of str

    The function will receive a opened file which contains infomation
    about messages.
    The function will strip newline and take it line by line and add into
    a list called result.
    The function will return a list of str that contains all the information
    in the opened file.
    '''
    # read opened file
    lines = open_file.readlines()
    # initialize the result as a list
    result = []
    # strip newline add all the infomation into the result
    for line in lines:
        line = line.strip('\n')
        result.append(line)
    return result


def read_deck(open_file):
    ''' (file open for reading) -> list of int

    The function will receive a opened file which contains a deck of cards.
    The function will strip newline and space, and take it as an int, and
    then add into a list called result.
    The function will return a list of int that contains a deck of cards.
    '''
    # read opened file
    lines = open_file.readlines()
    # initialize the result as a list
    result = []
    # strip newline add all cards into the result
    for line in lines:
        line = line.strip('\n').split()
        # add each number speratelly as an int
        for num in line:
            result.append(int(num))
    return result


def test():
    ''' () -> NoneType
    This function is only for test.
    '''
    print(process_messages([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,
                           15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23,
                           26], ['did', 'you', 'get', 'up?'], 'e'))
    print(process_message([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12,
                           15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23,
                           26], 'ORAFYTRPACY', 'd'))
    deck1 = read_deck(open('deck1.txt'))
    deck2 = read_deck(open('deck2.txt'))
    print(deck1)
    print(deck2)
    print(deck1 == deck2)
    message1 = read_messages(open('secret4.txt'))
    print(message1)
    d_m1 = process_messages(deck1, message1, 'd')
    print(d_m1)


if __name__ == '__main__':
    test()
