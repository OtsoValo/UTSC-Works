from container import *


def banana_verify(soure, goal, container, moves):
    ''' (str, str, Container, list of str) -> bool

    The function will have four parameters which are soure word,
    goal word, container type and a list of moves.
    The function will determine the moves can make the soure word
    to become to the goal word.
    The function will return True if the moves changes soure word
    exactly to goal word; otherwise, it return False.
    The list of moves should be 'P', 'M', and 'G' which are put move and
    get.
    '''
    # create a str to store letters after moves
    result = ''
    # loop through each move in list of loves
    for move in moves:
        # when the move is put
        if move == 'P':
            # try to follow the moves
            try:
                container.put(soure[0])
                soure = soure[1:]
            # if the move cause the error, result should directly be False
            except:
                return False
        # when the move is move, add it in result
        elif move == 'M':
            # try to follow the moves
            try:
                result += soure[0]
                soure = soure[1:]
            # if the move cause the error, result should directly be False
            except:
                return False
        # when the move is get
        elif move == 'G':
            # try to follow the moves
            try:
                result += container.get()
            # if the move cause the error, result should directly be False
            except:
                return False
    # cheack if result and goal word are the same
    return result == goal


if __name__ == '__main__':
    container_1 = Queue()
    container_2 = Stack()
    word = 'BANANA'
    moves = ['P', 'M', 'G', 'M']
    print('CAT: ', banana_verify('CAT', 'ACT', container_1, moves))
    moves = ['P', 'M', 'P', 'M', 'P', 'M', 'G', 'G', 'G']
    print('AAANNB: ', banana_verify(word, 'AAANNB', container_2, moves))