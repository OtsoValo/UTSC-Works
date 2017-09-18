def insert(listA, listB, index):
    '''(?, ?, int) -> ?
    The function will insert listB at the index between listA.
    This function will only work on str or list.
    The function will return a string or list based on the parameter.
    REQ: index >= 0
    >>> insert([1, 2, 3], ['a', 'b', 'c'], 2)
    [1, 2, 'a', 'b', 'c', 3]
    >>> insert('123', 'abc', 2)
    '12abc3'
    >>> insert('joey', 'huang', 4)
    'joeyhuang'
    '''
    result = listA[:index] + listB[:] + listA[index:]
    return result


def up_to_first(a_list, an_object):
    '''(?, ?) -> ?
    The fuction will search the object in the string or the list,
    and if it can find the object in a_list, then return all the factors before
    the object.
    If it can not find the object, then print a_list

    >>> up_to_first([1, 2, 3, 4], 3)
    [1, 2]
    >>> up_to_first([1, 2, 3, 4], 9)
    [1, 2, 3, 4]
    >>> up_to_first('Hello World!', 'o')
    'Hell'
    '''
    # when can find object in the list or string
    if an_object in a_list:
        result = a_list[:a_list.index(an_object)]
    # when can not find object in the list or string
    else:
        result = a_list[:]
    return result


def cut_list(a_list, index):
    '''(?, int) -> ?
    The function will receive two parameters.
    The first is a list or string, and the second is an index.
    The function will return a string or a list which swap items that before
    and after the index.
    REQ: index >= 0
    >>> cut_list([0,1,2,3,4,5,6,7,8,9], 3)
    [4, 5, 6, 7, 8, 9, 3, 0, 1, 2]
    >>> cut_list('ABCDEFGX1234', 7)
    '1234XABCDEFG'
    '''
    result = a_list[index+1:] + a_list[index:index+1] + a_list[:index]
    return result
