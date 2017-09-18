def rsum(input_list: list) -> int:
    ''' The function will get one parameter which must be
    a list of int, and the function will return the sum of
    all int in this list.

    REQ: len(input_list) >= 1

    >>> rsum([5])
    5
    >>> rsum([1, 3, 5])
    9
    >>> rsum([5, 3, 1])
    9
    >>> rsum([1, 3, 2, 4, 5])
    15
    >>> rsum([1, 1, 2, 2, 3])
    9
    '''
    # if there is only one number in list
    if len(input_list) == 1:
        result = input_list[0]
    # if list contains more than one numbers
    else:
        result = input_list[0] + rsum(input_list[1:])
    return result


def rmax(input_list: list) -> int:
    ''' The function will get one parameter which must be
    a list of int, and the function will return the max int
    in the input_list.

    REQ: len(input_list) >= 1

    >>> rmax([5])
    5
    >>> rmax([1, 3, 5])
    5
    >>> rmax([5, 3, 1])
    5
    >>> rmax([1, 3, 2, 4, 5])
    5
    >>> rmax([2, 3, 4, 2, 3, 4])
    4
    '''
    # if list contains only one number, then return it
    if len(input_list) == 1:
        result = input_list[0]
    # if list has more than two numbers, and first is greater than the second
    elif input_list[0] > input_list[1]:
        # compare other numbers without the second one
        result = rmax([input_list[0]]+input_list[2:])
    # if second number is greater than the first
    else:
        # compare other numbers without the first one
        result = rmax(input_list[1:])
    return result


def small_2(input_list: list) -> list:
    ''' The function will receive a list of int as parameter,
    and return a list of two int. The returned list contains
    two smallest int in the input_list.
    Also, in the returned list, the first element would be
    the smallest number and the second element should be
    the second smallest number.

    REQ: len(input_list) >= 2

    >>> small_2([2, 5])
    [2, 5]
    >>> small_2([1, 3, 5])
    [1, 3]
    >>> small_2([5, 3, 1])
    [1, 3]
    >>> small_2([1, 3, 2, 4, 5])
    [1, 2]
    >>> small_2([1, 2, 3, 3, 2, 1])
    [1, 1]
    '''
    # if list just has two numbers, then sort them in a new list
    if len(input_list) == 2:
        if input_list[0] > input_list[1]:
            result = [input_list[1], input_list[0]]
        else:
            result = input_list[:]
    # if list has only three numbers
    elif len(input_list) == 3:
        # when the first one is the biggest, compare the rest
        if input_list[0] >= input_list[1] and input_list[0] >= input_list[2]:
            result = small_2(input_list[1:])
        # when the last one is the biggest, compare the rest
        elif input_list[2] >= input_list[0] and input_list[2] >= input_list[1]:
            result = small_2(input_list[:2])
        # when the second one is the biggest, compare the rest
        else:
            result = small_2([input_list[0]]+[input_list[2]])
    # if list has more than three numbers
    else:
        result = small_2([input_list[0]]+small_2(input_list[1:]))
    return result


def second_smallest(input_list: list) -> int:
    ''' The function will get one parameter which must be
    a list of int, and the function will return the second
    smallest number in the input_list.

    REQ: len(input_list) >= 2

    >>> second_smallest([2, 5])
    5
    >>> second_smallest([1, 3, 5])
    3
    >>> second_smallest([5, 3, 1])
    3
    >>> second_smallest([1, 3, 2, 4, 5])
    2
    >>> second_smallest([1, 2, 3, 3, 2, 1])
    1
    '''
    return small_2(input_list)[1]


def max_min_helper(input_list: list) -> tuple:
    ''' The function is a help function for sum_max_min.
    The function must take list of int as parameter, and
    return a tuple which contains the biggest and smallest
    number in the input_list.

    REQ: len(input_list) >= 1

    >>> max_min_helper([5])
    (5, 5)
    >>> max_min_helper([1, 3, 5])
    (5, 1)
    >>> max_min_helper([5, 3, 1])
    (5, 1)
    >>> max_min_helper([1, 3, 2, 4, 5])
    (5, 1)
    >>> max_min_helper([1, 1, 1, 1])
    (1, 1)
    '''
    # if the list only has one number
    if len(input_list) == 1:
        (big, small) = (input_list[0], input_list[0])
    # if the list has two numbers, return a tuple which sort
    # the numbers as (big, small)
    elif len(input_list) == 2:
        if input_list[0] > input_list[1]:
            (big, small) = (input_list[0], input_list[1])
        else:
            (big, small) = (input_list[1], input_list[0])
    # if the first number is in the middle, then compare the rest
    elif (input_list[0] >= input_list[1] and input_list[0] <= input_list[2])\
         or (input_list[0] <= input_list[1] and\
             input_list[0] >= input_list[2]):
        (big, small) = max_min_helper(input_list[1:])
    # if the second number is in the middle, then compare the rest
    elif (input_list[1] >= input_list[0] and input_list[1] <= input_list[2])\
         or (input_list[1] <= input_list[0] and\
             input_list[1] >= input_list[2]):
        (big, small) = max_min_helper([input_list[0]] + input_list[2:])
    # if the last number is in the middle or there are
    # two numbers are equal, then compare the rest
    else:
        (big, small) = max_min_helper(input_list[:2] + input_list[3:])
    return (big, small)


def sum_max_min(input_list: list) -> int:
    ''' The function must take a list of int as parameter, and
    return the sum of the biggest and smallest number in
    the input_list.

    REQ: len(input_list) >= 1

    >>> sum_max_min([5])
    10
    >>> sum_max_min([1, 3, 5])
    6
    >>> sum_max_min([5, 3, 1])
    6
    >>> sum_max_min([1, 3, 2, 4, 5])
    6
    >>> sum_max_min([1, 1, 1, 1])
    2
    >>> sum_max_min([1, 2, 3, 3, 2, 1, 1, 1, 2, 2, 3, 3])
    4
    '''
    (big, small) = max_min_helper(input_list)
    return big + small
