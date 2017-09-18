def greeting(name):
    ''' (str) -> str
    The function will return a greeting based on the parameter name.

    >>> greeting('nick')
    'Hello nick how are you today?'
    '''
    return 'Hello ' + name + ' how are you today?'


def mutate_list(input_list):
    ''' (list) -> NoneType
    The function will only mutate each element in the input list
    by the following rules:
    1. all integers are multipled by 2
    2. boolean will be inverted
    3. all str has its first and last letters removed
    4. the 0th element of the list is set to the str 'Hello', regardless of
    what it was originally.

    REQ: input list has at least 1 element
    REQ: str list has at least 2 characters

    >>> l1 = ['49', '21', 'hello', 'true', False, 6]
    >>> mutate_list(l1)
    >>> l1 == ['Hello', '', 'ell', 'ru', True, 12]
    True
    '''
    # loop through each element
    index = 1
    while index < len(input_list):
        # when element is integre, then multipled by 2
        if type(input_list[index]) == int:
            input_list[index] = 2 * input_list[index]
        # when element is boolean, inverts it
        elif type(input_list[index]) == bool:
            input_list[index] = not input_list[index]
        # when element is str, then cut first and last letters
        elif type(input_list[index]) == str:
            input_list[index] = input_list[index][1:-1]
        index += 1
    # the first element should be 'Hello'
    input_list[0] = 'Hello'


def merge_dicts(dict_1, dict_2):
    ''' ({str: list of str}, {str: list of str}) -> {str: list of str}

    The function will take two dictionaries as parameters and return a new
    dictionary based on two inputs.
    The final dict should be {key: value pairs from both dictionaries}.

    >>> d1 = {'a': [1], 'b': [2], 'c': [3]}
    >>> d2 = {'a': [4], 'b': [5], 'd': [6]}
    >>> merge_dicts(d1, d2) == {'a': [1, 4], 'b': [2, 5], 'c': [3], 'd': [6]}
    True
    >>> merge_dicts(d2, d1) == {'a': [4, 1], 'b': [5, 2], 'c': [3], 'd': [6]}
    True
    '''
    # create a new dictionary as result
    result = {}
    # loop through each key in dict_1
    for key in dict_1.keys():
        # if dict_2 has the same key, then add the value together into result
        if key in dict_2:
            result[key] = dict_1[key] + dict_2[key]
        # if dict_2 does not have, then only add dict_1 value into result
        else:
            result[key] = dict_1[key]
    # loop through each key in dict_2
    for key in dict_2.keys():
        # if the key in dict_2 never appear in the result,
        # then add it with its value into result
        if key not in result:
            result[key] = dict_2[key]
    return result
