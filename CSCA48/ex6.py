def rsum(input_list: list) -> int:
    ''' The function will get one parameter which must be
    a nest list of int, and the function will return the sum of
    all int in this list.

    >>> rsum([[[1, [[[2]], [3]]], 4]])
    10
    >>> rsum([[[1, [[[2]], [3]]], [[[4]], [[[]]]]]])
    10
    >>> rsum([[[1, [[[2]], [3]]], [[[4]], [[[0]]]]]])
    10
    >>> rsum([1, 3, 2, 4, 5])
    15
    >>> rsum([1, 1, 2, 2, 3])
    9
    '''
    # if it is a number then return it
    if isinstance(input_list, int) or isinstance(input_list, float):
        result = input_list
    # if it is an empty list then return 0 adding to result
    elif len(input_list) == 0:
        result = 0
    # if only one element in list
    elif len(input_list) == 1:
        # if it is a sublist, then recall function
        if isinstance(input_list[0], list):
            result = rsum(input_list[0])
        # if it is a number, then return it
        else:
            result = input_list[0]
    # if there are more than one element in list, recall the function
    else:
        result = rsum(input_list[0]) + rsum(input_list[1:])
    return result


def rmax(input_list: list) -> int:
    ''' The function will get one parameter which must be
    a nest list of int, and the function will return the max int
    in the input_list.

    REQ: input_list has to have at least one number

    >>> rmax([[], [], [], [], [1, [[[2]]]], [3], []])
    3
    >>> rmax([[1, [[[2]]]], [3], []])
    3
    >>> rmax([[1, [[[2]]]], [3]])
    3
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
    # if it is a number then return it
    if isinstance(input_list, int) or isinstance(input_list, float):
        result = input_list
    # if it is an empty list then return None
    elif len(input_list) == 0:
        result = None
    # if only one element in list
    elif len(input_list) == 1:
        # if it is a sublist, then recall function
        if isinstance(input_list[0], list):
            result = rmax(input_list[0])
        # if it is a number, then return it
        else:
            result = input_list[0]
    # if the first element is an empty list
    elif rmax(input_list[0]) is None:
        # compare another one with others
        result = rmax(input_list[1:])
    # if the second element is an empty list or it is smaller
    # then compare first one with others
    elif (rmax(input_list[1]) is None)or(rmax(input_list[0]) >
                                         rmax(input_list[1])):
        result = rmax([input_list[0]]+input_list[2:])
    # else condition only happens when first one is smaller
    # then compare the second one with others
    else:
        result = rmax(input_list[1:])
    return result


def small_2(input_list, extra_s=None, small=None):
    ''' (list, float, float) -> tuple
    The function will receive a nest list of int as parameter and
    two numbers, which are bound for the function.
    The function will take all numbers in nest list and two
    bounds, and compare all numbers.
    The function will return a tuple with the smallest and
    the second smallest number.

    REQ: input_list has to have at least two number

    >>> small_2([2, 5])
    (2, 5)
    >>> small_2([1, 3, 5])
    (1, 3)
    >>> small_2([5, 3, 1])
    (1, 3)
    >>> small_2([1, 3, 2, 4, 5])
    (1, 2)
    >>> small_2([1, 2, 3, 3, 2, 1])
    (1, 1)
    >>> small_2([[3, [], []], 2])
    (2, 3)
    >>> small_2(([1, 2, 3, [-5, [-7, [-1, -10, [[[]]]]]]]))
    (-10, -7)
    '''
    if isinstance(input_list, float) or isinstance(input_list, int):
        if extra_s is None:
            (extra_s, small) = (input_list, input_list)
        if extra_s <= input_list < small:
            small = input_list
        elif input_list < extra_s:
            (extra_s, small) = (input_list, extra_s)
        elif small == extra_s:
            small = input_list
    elif len(input_list) == 1:
        if isinstance(input_list[0], list):
            (extra_s, small) = small_2(input_list[0], extra_s, small)
        else:
            if extra_s is None:
                (extra_s, small) = (input_list[0], input_list[0])
            if extra_s <= input_list[0] < small:
                small = input_list[0]
            elif input_list[0] < extra_s:
                (extra_s, small) = (input_list[0], extra_s)
            elif small == extra_s:
                small = input_list[0]
    elif len(input_list) > 1:
        (extra_s, small) = small_2(input_list[0], extra_s, small)
        (extra_s, small) = small_2(input_list[1:], extra_s, small)
    return (extra_s, small)


def second_smallest(input_list: list) -> int:
    ''' The function will get one parameter which must be
    a nest list of numbers, and the function will return the second
    smallest number in the input_list.

    REQ: input_list has to have at least two number

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
    >>> second_smallest([[3,[],[]], 2])
    3
    >>> second_smallest(([1, 2, 3, [-5, [-7, [-1, -10, [[[]]]]]]]))
    -7
    '''
    (extra_s, small) = small_2(input_list)
    return small


def max_min_helper(input_list, big=None, small=None):
    ''' (list, float, float) -> tuple
    The function is a help function for sum_max_min.
    The function must take nest list of numbers as parameter and
    two numbers which are bounds.
    The function will take all numbers in nest list and two
    bounds, and compare all numbers.
    The function will return a tuple with the largest and
    the smallest numbers.

    REQ: input_list has to have at least one number

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
    >>> max_min_helper([[3, [], []], 2])
    (3, 2)
    >>> max_min_helper(([1, 2, 3, [-5, [-7, [-1, -10, [[[]]]]]]]))
    (3, -10)
    '''
    if isinstance(input_list, float) or isinstance(input_list, int):
        if big is None:
            (big, small) = (input_list, input_list)
        elif input_list > big:
            big = input_list
        elif input_list < small:
            small = input_list
    elif len(input_list) == 1:
        if isinstance(input_list[0], list):
            (big, small) = max_min_helper(input_list[0], big, small)
        else:
            if big is None:
                (big, small) = (input_list[0], input_list[0])
            elif input_list[0] > big:
                big = input_list[0]
            elif input_list[0] < small:
                small = input_list[0]
    elif len(input_list) > 1:
        (big, small) = max_min_helper(input_list[0], big, small)
        (big, small) = max_min_helper(input_list[1:], big, small)
    return (big, small)


def sum_max_min(input_list: list) -> int:
    ''' The function must take a nest list of int as parameter, and
    return the sum of the biggest and smallest number in
    the input_list.

    REQ: input_list has to have at least one number

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
    >>> sum_max_min([[3, [], []], 2])
    5
    >>> sum_max_min(([1, 2, 3, [-5, [-7, [-1, -10, [[[]]]]]]]))
    -7
    '''
    (big, small) = max_min_helper(input_list)
    return big + small
