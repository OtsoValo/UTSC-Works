def percent_to_gpv(mark: int):
    ''' (int) -> float
    This is function is to get the Grade Point Value based on your percentage
    mark.
    The function will return the Great Point Value, a float.
    REQ: mark >= 0 and mark <= 100
    >>> percent_to_gpv(97)
    4.0
    >>> percent_to_gpv(81)
    3.7
    >>> percent_to_gpv(71)
    2.7
    >>> percent_to_gpv(68)
    2.3
    >>> percent_to_gpv(72)
    2.7
    >>> percent_to_gpv(62)
    1.7
    >>> percent_to_gpv(65)
    2.0
    >>> percent_to_gpv(39)
    0.0
    >>> percent_to_gpv(57)
    1.3
    >>> percent_to_gpv(53)
    1.0
    '''
    # the percentage mark is between 0 and 49
    if (0 <= mark and mark <= 49):
        gpv = 0.0
    # the percentae mark is between 50 and 52
    elif (50 <= mark <= 52):
        gpv = 0.7
    # the percentage mark is between 53 and 56
    elif (53 <= mark and mark <= 56):
        gpv = 1.0
    # the percentage mark is between 57 and 59
    elif (57 <= mark and mark <= 59):
        gpv = 1.3
    # the percentage mark is between 60 and 62
    elif (60 <= mark and mark <= 62):
        gpv = 1.7
    # the percentage mark is between 63 and 66
    elif (63 <= mark and mark <= 66):
        gpv = 2.0
    # the percentage mark is between 67 and 69
    elif (67 <= mark and mark <= 69):
        gpv = 2.3
    # the percentage mark is between 70 and 72
    elif (70 <= mark and mark <= 72):
        gpv = 2.7
    # the percentage mark is between 73 and 76
    elif (73 <= mark and mark <= 76):
        gpv = 3.0
    # the percentage mark is between 77 and 79
    elif (77 <= mark and mark <= 79):
        gpv = 3.3
    # the percentage mark is between 80 and 84
    elif (80 <= mark and mark <= 84):
        gpv = 3.7
    # the percentage mark is between 85 and 89
    elif (85 <= mark and mark <= 89):
        gpv = 4.0
    # the percentage mark is between 90 and 100
    elif (90 <= mark and mark <= 100):
        gpv = 4.0
    # return gpv
    return gpv


def card_namer(value_input: str, suit_input: str):
    ''' (str, str) -> str
    The function takes two string from two different list which are called
    value and suit.
    One capital letter represents one characteristic from each list.
    If the suit input is not one of the recognized inputs, then, the inout
    is trying to cheat and will return 'CHESTER'.
    This function will return a string which is the full name of recognized
    inputs.
    >>> card_namer('Q', 'D')
    'Queen of Diamonds'
    >>> card_namer('9', 'S')
    '9 of Spades'
    >>> card_namer('8', 'T')
    'CHEATER!'
    >>> card_namer('2', '3')
    'CHEATER!'
    >>> card_namer('2', 'H')
    '2 of Hearts'
    >>> card_namer('7', 'C')
    '7 of Clubs'
    >>> card_namer('A', 'C')
    'Ace of Clubs'
    >>> card_namer('T', '9')
    'CHEATER!'
    >>> card_namer('J', 'D')
    'Jack of Diamonds'
    '''
    # name a str called result
    result = ''
    # if the value input is A
    if (value_input == 'A'):
        result += 'Ace'
    # if the value input is 2
    elif (value_input in '23456789'):
        result += value_input
    # if the value input is T
    elif (value_input == 'T'):
        result += '10'
    # if the value input is J
    elif (value_input == 'J'):
        result += 'Jack'
    # if the value input is Q
    elif (value_input == 'Q'):
        result += 'Queen'
    # if the value input is K
    elif (value_input == 'K'):
        result += 'King'
    # add the string ' of '
    result += ' of '
    # add another characteristic from suit list
    # if the suit input is D
    if (suit_input == 'D'):
        result += 'Diamonds'
    # if the suit input is C
    elif (suit_input == 'C'):
        result += 'Clubs'
    # if the suit input is H
    elif (suit_input == 'H'):
        result += 'Hearts'
    # if the suit input is S
    elif (suit_input == 'S'):
        result += 'Spades'
    # if the suit input can not match the suit list
    # it returns 'CHEATER!'
    else:
        result = 'CHEATER!'
    return result


def my_str(your_input):
    '''(obj) -> str
    The function will get your input whatever your input type is, and finally
    return a string.
    There are four sections, if the input is string, the output will be the
    same.
    If the input is int, the output would be 'Small Number', 'Medium Number',
    or 'Large Number'.
    If the input is a boolean, the output will be 'Yes', or 'No'.
    If the input is a foalt, the output will keep two numbers after the decimal
    mark
    Other types' input will return 'I dunno'
    The function will return a string as the final result
    >>> my_str("Hello")
    'Hello'
    >>> my_str(False)
    'NO'
    >>> my_str(42)
    'Medium Number'
    >>> my_str(42.0)
    '42.0'
    >>> my_str(3.1415926)
    '3.14'
    >>> my_str([1, 2, 3])
    'I dunno'
    >>> my_str('42')
    '42'
    >>> my_str(3248)
    'Large Number'
    '''
    # name a result, and it will be returned at the end of the function
    result = ''
    # if the input is a string
    # it will return itself
    if isinstance(your_input, str):
        result = your_input
    # if the input is a boolean, then return 'YES' or 'NO'
    elif isinstance(your_input, bool):
        your_input = str(your_input)
        if (your_input == 'True'):
            result = 'YES'
        else:
            result = 'NO'
    # if the the input is an integer
    # then return 'Small Number', 'Medium Number', or 'Large Number'
    elif isinstance(your_input, int):
        if your_input <= 10:
            result = 'Small Number'
        elif 11 <= your_input <= 99:
            result = 'Medium Number'
        else:
            result = 'Large Number'
    # if the input is a float
    # then return it as a string and keep two numbers after decimal mark
    elif isinstance(your_input, float):
        your_input = round(your_input, 2)
        result = str(your_input)
    # if the input is other types
    # it will return 'I dunno'
    else:
        result = 'I dunno'
    return result
