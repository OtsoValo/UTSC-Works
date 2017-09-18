# Code for working with word search puzzles
#
# Do not modify the existing code
#
# Complete the tasks below marked by *task*
#
# Before submission, you must complete the following header:
#
# I hear-by decree that all work contained in this file is solely my own
# and that I received no help in the creation of this code.
# I have read and understood the University of Toronto academic code of
# behaviour with regards to plagiarism, and the seriousness of the
# penalties that could be levied as a result of committing plagiarism
# on an assignment.
#
# Name: Qiuyu(Joey) Huang
# MarkUs Login: huangq41
#

PUZZLE1 = '''
tlkutqyu
hyrreiht
inokdcne
eaccaayu
riainpaf
rrpnairb
ybybnick
ujvaynak
'''

PUZZLE2 = '''
fgbkizpyjohwsunxqafy
hvanyacknssdlmziwjom
xcvfhsrriasdvexlgrng
lcimqnyichwkmizfujqm
ctsersavkaynxvumoaoe
ciuridromuzojjefsnzw
bmjtuuwgxsdfrrdaiaan
fwrtqtuzoxykwekbtdyb
wmyzglfolqmvafehktdz
shyyrreihtpictelmyvb
vrhvysciipnqbznvxyvy
zsmolxwxnvankucofmph
txqwkcinaedahkyilpct
zlqikfoiijmibhsceohd
enkpqldarperngfavqxd
jqbbcgtnbgqbirifkcin
kfqroocutrhucajtasam
ploibcvsropzkoduuznx
kkkalaubpyikbinxtsyb
vjenqpjwccaupjqhdoaw
'''


def rotate_puzzle(puzzle):
    '''(str) -> str
    Return the puzzle rotated 90 degrees to the left.
    '''

    raw_rows = puzzle.split('\n')
    rows = []
    # if blank lines or trailing spaces are present, remove them
    for row in raw_rows:
        row = row.strip()
        if row:
            rows.append(row)

    # calculate number of rows and columns in original puzzle
    num_rows = len(rows)
    num_cols = len(rows[0])

    # an empty row in the rotated puzzle
    empty_row = [''] * num_rows

    # create blank puzzle to store the rotation
    rotated = []
    for row in range(num_cols):
        rotated.append(empty_row[:])
    for x in range(num_rows):
        for y in range(num_cols):
            rotated[y][x] = rows[x][num_cols - y - 1]

    # construct new rows from the lists of rotated
    new_rows = []
    for rotated_row in rotated:
        new_rows.append(''.join(rotated_row))

    rotated_puzzle = '\n'.join(new_rows)

    return rotated_puzzle


def lr_occurrences(puzzle, word):
    '''(str, str) -> int
    Return the number of times word is found in puzzle in the
    left-to-right direction only.

    >>> lr_occurrences('xaxy\nyaaa', 'xy')
    1
    '''
    return puzzle.count(word)

# ---------- Your code to be added below ----------

# *task* 3: write the code for the following function.
# We have given you the header, type contract, example, and description.


def total_occurrences(puzzle, word):
    '''(str, str) -> int
    Return total occurrences of word in puzzle.
    All four directions are counted as occurrences:
    left-to-right, top-to-bottom, right-to-left, and bottom-to-top.

    >>> total_occurrences('xaxy\nyaaa', 'xy')
    2
    '''
    # Define the count times and finally return it
    # search the word from left-to-right
    count = lr_occurrences(puzzle, word)
    # search the word from top-to-bottom
    top_to_bottom = rotate_puzzle(puzzle)
    count += lr_occurrences(top_to_bottom, word)
    # search the word from right-to-left
    right_to_left = rotate_puzzle(top_to_bottom)
    count += lr_occurrences(right_to_left, word)
    # search the word from bottom-to-top
    bottom_to_top = rotate_puzzle(right_to_left)
    count += lr_occurrences(bottom_to_top, word)
    # return final times
    return count

# *task* 5: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_horizontal(puzzle, word):
    '''(str, str) -> bool
    The function will decide whether the word in the horizontal line of the
    puzzle.
    If the word can be searched in left-to-right or in right-to-left, then
    it will return True. Otherwise, it will return False.

    >>> in_puzzle_horizontal('abce\nabcd', 'cd')
    True
    >>> in_puzzle_horizontal('sadj\nuiwq', 'jd')
    True
    >>> in_puzzle_horizontal('abcede', 'ed')
    True
    >>> in_puzzle_horizontal('jasd\njkdf', 'jj')
    False
    '''
    # Reverse the puzzle in order to search from right to left
    right_to_left = rotate_puzzle(rotate_puzzle(puzzle))
    # If the word is in horizontal line, then the result is True
    count1 = lr_occurrences(puzzle, word)
    count2 = lr_occurrences(right_to_left, word)
    result = (count1 > 0) or (count2 > 0)
    return result

# *task* 8: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle_vertical(puzzle, word):
    '''(str, str) -> bool
    The function will decide whether the word in the vertical line of the
    puzzle.
    If the word can be searched in top-to-bottom or in bottom-to-top, then
    it will return True. Otherwise, it will return False.

    >>> in_puzzle_vertical('abce\nabcd', 'aa')
    True
    >>> in_puzzle_vertical('sadj\nuiwq', 'ia')
    True
    >>> in_puzzle_vertical('abcede', 'ce')
    False
    >>> in_puzzle_vertical('jasd\njkdf', 'jj')
    True
    '''
    # Define the puzzle string in vertical orientations which includes both
    # top-to-bottom and bottom-to-top.
    top_to_bottom = rotate_puzzle(puzzle)
    bottom_to_top = rotate_puzzle(rotate_puzzle(top_to_bottom))
    # If the word is in vertical orientations, then the result is True.
    count1 = lr_occurrences(top_to_bottom, word)
    count2 = lr_occurrences(bottom_to_top, word)
    result = (count1 > 0) or (count2 > 0)
    return result

# *task* 9: write the code for the following function.
# We have given you the function name only.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_puzzle(puzzle, word):
    '''(str, str) -> bool
    The function will return wheather the word is in any orientation.
    All the orientation is:
    eft-to-right, top-to-bottom, right-to-left, and bottom-to-top.
    If the word is in any four of directions, then it will return True
    Othereise, it will return False.

    >>> in_puzzle('abcd\nefgh\nigkln', 'gfb')
    True
    >>> in_puzzle('xyz\nabc', 'ac')
    False
    >>> in_puzzle('xaxy\nyaaa', 'xy')
    True
    >>> in_puzzle('xaxy\nyaaa', 'joey')
    False
    '''
    # By using the previous function total_occurrences
    result = total_occurrences(puzzle, word) > 0
    return result

# *task* 10: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def in_exactly_one_dimension(puzzle, word):
    '''(str, str) -> bool
    The function will decide wheather the word is in horizontal or in vertical.
    If the word is in horizontal or vertical directions, the function will
    return True.
    However, if the word is in both horizontal and vertical directions, the
    result is False.

    >>> in_exactly_one_dimension('abcd\nefgh\nigkln', 'gfb')
    True
    >>> in_exactly_one_dimension('abce\nabcd', 'ce')
    True
    >>> in_exactly_one_dimension('aaaa\naaaa', 'aa')
    False
    >>> in_exactly_one_dimension('abce\nebcd', 'aa')
    False
    '''
    # If the result is True, it should match two conditions
    # condition one is that the word is in any dimensions
    cond_1 = in_puzzle(puzzle, word)
    # condition two is that the word does not appear in both vertical and
    # horizontal directions.
    cond_2 = not (
       in_puzzle_horizontal(puzzle, word) and in_puzzle_vertical(puzzle, word))
    result = cond_1 and cond_2
    return result

# *task* 11: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def all_horizontal(puzzle, word):
    '''(str, str) -> bool
    The function decide wheather the supplied word is only in the horizontal
    directions.
    If the word is not in the puzzle at all, the function will still return
    True.

    >>> all_horizontal('abcd\nefgh\nigkln', 'gfb')
    False
    >>> all_horizontal('xaxy\nyaaa', 'xy')
    False
    >>> all_horizontal('abce\nabcd', 'cd')
    True
    >>> all_horizontal('abce\nebcd', 'aa')
    True
    '''
    # If these is not any supplied word in vertical, then it match the
    # situzation of all_horizontal.
    result = not in_puzzle_vertical(puzzle, word)
    return result

# *task* 12: write the code for the following function.
# We have given you only the function name and parameters.
# You must follow the design recipe and complete all parts of it.
# Check the handout for what the function should do.


def at_most_one_vertical(puzzle, word):
    '''(str, str) -> bool
    The function will return True if and only if that the supplied word occurs
    at most once in the whole puzzle and that occurrence is vertical.

    >>> at_most_one_vertical('aaaa\naaaa', 'aa')
    False
    >>> at_most_one_vertical('abce\nabcd', 'de')
    True
    >>> at_most_one_vertical('abce\nabcd', 'aa')
    False
    >>> at_most_one_vertical('abcda\nabcda', 'a')
    False
    >>> at_most_one_vertical('abce\nebcd', 'aa')
    False
    '''
    # There are two conditions:
    # first, total occurrence is less or equal than 1
    cond_1 = total_occurrences(puzzle, word) <= 1
    # second, the only occurrence must be vertical
    cond_2 = in_puzzle_vertical(puzzle, word)
    result = cond_1 and cond_2
    return result


def do_tasks(puzzle, name):
    '''(str, str) -> NoneType
    puzzle is a word search puzzle and name is a word.
    Carry out the tasks specified here and in the handout.
    '''

    # *task* 1a: add a print call below the existing one to print
    # the number of times that name occurs in the puzzle left-to-right.
    # Hint: one of the two starter functions defined above will be useful.

    # the end='' just means "Don't start a newline, the next thing
    # that's printed should be on the same line as this text
    print('Number of times', name, 'occurs left-to-right: ', end='')
    # your print call here
    print(lr_occurrences(puzzle, name))
    # *task* 1b: add code that prints the number of times
    # that name occurs in the puzzle top-to-bottom.
    # (your format for all printing should be similar to
    # the print statements above)
    # Hint: both starter functions are going to be useful this time!
    print('Number of times', name, 'occurs top-to-bottom: ', end='')
    print(lr_occurrences(rotate_puzzle(puzzle), name))
    # *task* 1c: add code that prints the number of times
    # that name occurs in the puzzle right-to-left.
    print('Number of times', name, 'occurs right-to-left: ', end='')
    print(lr_occurrences(rotate_puzzle(rotate_puzzle(puzzle)), name))
    # *task* 1d: add code that prints the number of times
    # that name occurs in the puzzle bottom-to-top.
    print('Number of times', name, 'occurs bottom-to-top: ', end='')
    print(lr_occurrences(rotate_puzzle(rotate_puzzle(rotate_puzzle(puzzle))),
                         name))
    # *task* 4: print the results of calling total_occurrences on
    # puzzle and name.
    # Add only one line below.
    # Your code should print a single number, nothing else.
    print(total_occurrences(puzzle, name))
    # *task* 6: print the results of calling in_puzzle_horizontal on
    # puzzle and name.
    # Add only one line below. The code should print only True or False.
    print(in_puzzle_horizontal(puzzle, name))


do_tasks(PUZZLE1, 'brian')

# *task* 2: call do_tasks on PUZZLE1 and 'nick'.
# Your code should work on 'nick' with no other changes made.
# If it doesn't work, check your code in do_tasks.
# Hint: you shouldn't be using 'brian' anywhere in do_tasks.
do_tasks(PUZZLE1, 'nick')
# *task* 7: call do_tasks on PUZZLE2  and 'nick'.
# Your code should work on the bigger puzzle with no changes made to do_tasks.
# If it doesn't work properly, go over your code carefully and fix it.
do_tasks(PUZZLE2, 'nick')
# *task* 9b: print the results of calling in_puzzle on PUZZLE1 and 'nick'.
# Add only one line below. Your code should print only True or False.
print(in_puzzle(PUZZLE1, 'nick'))
# *task* 9c: print the results of calling in_puzzle on PUZZLE2 and 'thierry'.
# Add only one line below. Your code should print only True or False.
print(in_puzzle(PUZZLE1, 'thierry'))
