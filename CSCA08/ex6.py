def copy_me(input_list):
    '''(list) -> list
    The function will receive a list and return a coyp list which do the
    following changes.
    All string letters changed to upper-case.
    Integers and floats are going to ass one
    Boolean will be negated
    List will only return a str 'List'

    >>> copy_me(['joey', 'huang', 18, 'male', True, [1, 2, 3, 4]])
    ['JOEY', 'HUANG', 19, 'MALE', False, 'List']
    >>> copy_me([32, 4.543, '34', [2, 34.34], False])
    [33, 5.543, '34', 'List', True]
    '''
    # initialize a copy list
    copy_list = []
    # use loop and if to evaluate each element in the list
    for element in input_list:
        if type(element) == str:
            element = element.upper()
        elif type(element) == int or type(element) == float:
            element += 1
        elif type(element) == bool:
            element = element is False
        elif type(element) == list:
            element = 'List'
        # add changed elements into the copy list
        copy_list.append(element)
    return copy_list


def mutate_me(input_list):
    '''(list) -> Nonetype
    The function will mutate the list and return nothing.
    All string letters changed to upper-case.
    Integers and floats are going to ass one
    Boolean will be negated
    List will only return a str 'List'
    '''
    # initialize index 'i' equals to zore
    i = 0
    # use while loop and if to change each elements in the input list
    while i < len(input_list):
        if type(input_list[i]) == str:
            input_list[i] = input_list[i].upper()
        elif type(input_list[i]) == int or type(input_list[i]) == float:
            input_list[i] += 1
        elif type(input_list[i]) == bool:
            input_list[i] = input_list[i] is False
        elif type(input_list[i]) == list:
            input_list[i] = 'List'
        i += 1
    # return nothing
    return None
