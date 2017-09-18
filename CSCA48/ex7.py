def edit_distance(s1: str, s2: str) -> int:
    ''' The function will return a number that s1 will take to
    edit becoming to s2.
    '''
    if len(s1) == 0:
        result = 0
    elif s1[0] != s2[0]:
        result = 1 + edit_distance(s1[1:], s2[1:])
    else:
        result = edit_distance(s1[1:], s2[1:])
    return result


def subsequence(s1, s2):
    ''' (str, str) -> bool

    The function will receive two str for compare.
    The function will return True iff after removing letters
    from s2, s2 can become s1, which means letters in s1
    should in s2 in the same order.

    >>> subsequence('dog', 'XYZdABCo123g!!!')
    True
    >>> subsequence('dog', 'gXYZdABCo123!!!')
    False
    '''
    if len(s1) == 0:
        result = True
    else:
        (s2, find) = sub_helper(s1, s2)
        result = s1 == s2[:len(s1)]
    return result


def sub_helper(s1, s2, find=0):
    ''' (str, str, int) -> (str, int)

    The function is the helper function of subsquence.
    The function will remove letters in s2 iff these ltters
    doesn't appear in s1.
    The function will return a tuple of new s2 and an int
    which is the times we manipulate s2.

    >>> sub_helper('dog', 'XYZdABCo123g!!!')
    ('dog!!!', 3)
    >>> sub_helper('dog', 'gXYZdABCo123!!!')
    ('do123!!!', 2)
    '''
    if len(s1) == 1:
        if s1 in s2:
            s2 = s2[:find] + s2[s2.index(s1):]
            find += 1
    else:
        (s2, find) = sub_helper(s1[0], s2, find)
        (s2, find) = sub_helper(s1[1:], s2, find)
    return (s2, find)


def perms(s: str) -> set:
    ''' The function will take a str,
    and return all the permutation of that str.
    '''
    if len(s) == 0:
        return set()
    elif len(s) == 1:
        return {s}
    elif len(s) == 2:
        return {s[0]+s[1], s[1]+s[0]}
    elif len(s) > 2:
        result = set()
        i = 0
        while i < len(s):
            last = perms(s[:i]+s[i+1:])
            for j in last:
                result.add(j+s[i])
            i += 1
    return result
