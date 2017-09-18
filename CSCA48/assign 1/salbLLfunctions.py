"""
# Copyright Nick Cheng, Qiuyu Huang 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2017
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from salboard import SALboard
from salbnode import SALBnode

# Add your functions here.


def salb2salbLL(salb: 'SALboard') -> 'SALBnode':
    ''' The function will take salb as a parameter which should be
    a SALboard, and the function will change it into SALBnode board.
    The function will return a SALBnode which is a linked list representation
    of the same board.
    The final result should be a SALBnode based on input.

    REQ: The input should ba a SALboard
    REQ: salb.numSquares > 0
    REQ: sslb.snadders is a dict

    >>> salb = SALboard(5, {1: 3})
    >>> board = salb2salbLL(salb)
    >>> board.snadder == board.next.next
    True

    >>> salb = SALboard(5, {1: 3, 3: 4})
    >>> board = salb2salbLL(salb)
    >>> board.snadder == board.next.next
    True
    >>> board.next.next.snadder == board.next.next.next
    True
    >>> board.next.next.next.next.next == board
    True

    >>> salb = SALboard(1, {})
    >>> board = salb2salbLL(salb)
    >>> board == board.next
    True
    '''
    # get the num of squares
    num_squares = salb.numSquares
    # get a copy of the dict of snadders
    snadders = {}
    for source in salb.snadders:
        snadders[source] = salb.snadders[source]

    # create the board and let curr pointer to the board
    board = SALBnode()
    curr = board
    # loop through num_squares to create board
    for num in range(1, num_squares):
        # create a new node and create each pointer
        next = SALBnode()
        curr.next = next
        # if current num has a snadder,
        # then change source in snadders from a numebr to an address of node
        if num in snadders:
            snadders[curr] = snadders[num]
            del snadders[num]
        curr = curr.next
    # let the final node pointer to the first one
    curr.next = board

    # exchange key and value for snadders
    # after change, the key should be destination,
    # and the value should be source
    snadders = {value: key for key, value in snadders.items()}

    # initialize curr for another loop
    curr = board
    # loop through num_squares of snadders to find destination
    for num in range(1, num_squares):
        # if current num has a snadder,
        # then change dest in snadders from a numebr to an address of node
        if num in snadders:
            snadders[curr] = snadders[num]
            del snadders[num]
        curr = curr.next

    # loop through each pair of snadder in snadders
    # to create actual snadder connection
    # in snadder key is dest, and value is source
    for dest in snadders:
        snadders[dest].snadder = dest
    return board


def willfinish(first: 'SALBnode', stepsize: int) -> bool:
    ''' The function will take two parameters which are a linked
    list representationof a salboard and a step size.
    The function will determine will the player finish based on
    the board and step size.
    It will return True if it can be finished, otherwise, return False.

    REQ: stepsize > 0

    >>> salb = SALboard(5, {1: 3, 3: 4})
    >>> board = salb2salbLL(salb)
    >>> willfinish(board, 2)
    True
    >>> willfinish(board, 3)
    True
    >>> willfinish(board, 1)
    True

    >>> salb = SALboard(5, {4:3})
    >>> board = salb2salbLL(salb)
    >>> willfinish(board, 1)
    False

    >>> salb = SALboard(5, {})
    >>> board = salb2salbLL(salb)
    >>> willfinish(board, 1)
    True

    >>> salb = SALboard(5, {1: 3, 3: 4, 4: 2})
    >>> board = salb2salbLL(salb)
    >>> willfinish(board, 2)
    False

    >>> salb = SALboard(5, {})
    >>> board = salb2salbLL(salb)
    >>> willfinish(board, 666)
    True
    '''
    # get the square address where will start by calling the help function
    start = where_start(first, stepsize)
    # check if start square is a source
    if start.snadder is not None:
            start = start.snadder

    # initialize the num of total step
    num_step = 0
    # get the total num of squares by calling the help function
    num_squares = num_of_squares(first)
    # If it can be finished, then the step num must be less than suqares num,
    # because we step num is greater than squares num
    # it must arrive a same square twice and it must in the loop.
    # loop will stop when arrive final square
    while num_step < num_squares and start.next != first:
        # move player by calling help function
        start = move(start, stepsize)
        # check for snadders
        if start.snadder is not None:
            start = start.snadder
        num_step += 1
    # return whether arrived the final square or created a loop
    return start.next == first


def whowins(first: 'SALBnode', step1: int, step2: int) -> int:
    ''' The function will two three parameters.
    The first parameter is a salbnode which is a beginning of a board.
    Other parameters are stepsizes of two players, step1 is the stepsize
    of the first player, step2 is the stepsize of the second player.
    The function will return winning player's number whin its stepsize.
    If no one can finish, then the player 2 wins.
    If they can finish at the same time, the player 1 wins.

    REQ: step1 > 0
    REQ: step2 > 0

    >>> salb = SALboard(5, {1: 3, 3: 4})
    >>> board = salb2salbLL(salb)
    >>> whowins(board, 2, 3)
    2

    >>> salb = SALboard(5, {})
    >>> board = salb2salbLL(salb)
    >>> whowins(board, 1, 2)
    1
    >>> whowins(board, 1, 1)
    1
    >>> whowins(board, 20, 20)
    1

    >>> salb = SALboard(5, {4: 3, 3: 2, 2: 1})
    >>> board = salb2salbLL(salb)
    >>> whowins(board, 2, 3)
    2
    '''
    # find where to start based one stepsizes by calling help function
    p1_curr = where_start(first, step1)
    p2_curr = where_start(first, step2)
    # check if start node has a snadder for both players
    if p1_curr.snadder is not None:
        p1_curr = p1_curr.snadder
    if p2_curr.snadder is not None:
        p2_curr = p2_curr.snadder

    # initialize the num of steps
    steps = 0
    # initialize the two bool for two players
    # to determine whether they finish or not
    p1_finish = False
    p2_finish = False

    # get the total square number by calling the help funcion
    num_squares = num_of_squares(first)
    # loop to move two players until steps reach the num_squares
    # or any player finish
    while steps < num_squares and not p1_finish and not p2_finish:
        # move the player one
        p1_curr = move(p1_curr, step1)
        # check whether there is a snadder
        if p1_curr.snadder is not None:
            p1_curr = p1_curr.snadder
        # check whether the player finish
        if p1_curr.next == first:
            p1_finish = True
        # move the player one
        p2_curr = move(p2_curr, step2)
        # check whether there is a snadder
        if p2_curr.snadder is not None:
            p2_curr = p2_curr.snadder
        # check whether the player finish
        if p2_curr.next == first:
            p2_finish = True
        steps += 1

    # if both finished then player one wins
    if p1_finish and p2_finish:
        return 1
    # if two player can not finish, then player two wins
    elif not p1_finish and not p2_finish:
        return 2
    # if the first player can finish but second can't
    # within the same num of steps, then play one wins
    elif p1_finish and not p2_finish:
        return 1
    # if the second player can finish but first can't
    # within the same num of steps, then play two wins
    else:
        return 2


def dualboard(first: 'SALBnode') -> 'SALBnode':
    ''' The function will only take a salbnode as a parameter.
    The parameter, first, is a beginning of a board.
    The function will get the dualboard of given board.
    The fual board will get the same nuber of suqares,
    but the reverse the snadders.
    Finally, the function will return the dual board.

    >>> salb = SALboard(5, {1: 3, 3: 4, 4: 2})
    >>> board = salb2salbLL(salb)
    >>> dual = dualboard(board)
    >>> board.snadder == board.next.next
    True
    >>> board.next.next.snadder == board.next.next.next
    True
    >>> board.next.next.next.snadder == board.next
    True

    >>> dual.next.snadder == dual.next.next.next
    True
    >>> dual.next.next.next.snadder == dual.next.next
    True
    >>> dual.next.next.snadder == dual
    True

    >>> salb = SALboard(3, {1: 2})
    >>> board = salb2salbLL(salb)
    >>> dual = dualboard(board)
    >>> board.snadder == board.next
    True
    >>> dual.next.snadder == dual
    True
    '''
    # create the first node of dual board
    dual = SALBnode()
    # get curr and d_curr for loop
    curr = first
    d_curr = dual
    # loop through each node in input board first
    while curr.next != first:
        # if the curr node has a snadder
        if curr.snadder is not None:
            # create a node between curr and d_curr and
            # help node's snadder pointer to curr node's snadder
            help_node = SALBnode()
            help_node.next = d_curr
            help_node.snadder = curr.snadder
            curr.snadder = help_node
        # if the curr node does not has a snadder
        else:
            # create a node between curr and d_curr and
            # help node's snadder pointer to None
            help_node = SALBnode()
            help_node.next = d_curr
            curr.snadder = help_node
        # create a new node for d_curr and connect them
        next = SALBnode()
        d_curr.next = next
        d_curr = d_curr.next
        curr = curr.next
    # let the last node in dual pointer to the first node in dual
    d_curr.next = dual

    # initialize curr for new loop
    curr = first
    # loop through each node in curr
    while curr.next != first:
        # help node has a snadder
        if curr.snadder.snadder is not None:
            # let destination in dual pointer to source in dual
            curr.snadder.snadder.snadder.next.snadder = curr.snadder.next
        curr = curr.next

    # initialize the curr for the final loop
    curr = first
    # loop through each node in first to change
    # the first board back to original
    while curr.next != first:
        # if help node has a snadder, then change it back
        if curr.snadder.snadder is not None:
            curr.snadder = curr.snadder.snadder
        # if help node does not have a snadder, then let it pointer to None
        else:
            curr.snadder = None
        curr = curr.next

    return dual


# ------------------------------
# There are some help functions.
# ------------------------------
def num_of_squares(salbLL: 'SALBnode') -> int:
    ''' The function will count the number of squares in the given board.
    The function will return a int which represents the
    num of squares of the given board.

    REQ: salbLL has to be a SALBnode and at least has one node

    >>> board = SALboard(100, {})
    >>> board = salb2salbLL(board)
    >>> num_of_squares(board)
    100

    >>> board = SALboard(1, {})
    >>> board = salb2salbLL(board)
    >>> num_of_squares(board)
    1

    >>> board = SALboard(100, {1: 3, 9:72})
    >>> board = salb2salbLL(board)
    >>> num_of_squares(board)
    100

    >>> board = SALboard(100, {3: 7, 9: 1, 74: 52})
    >>> board = salb2salbLL(board)
    >>> num_of_squares(board)
    100
    '''
    # since salbLL has at least one node
    # let num_squares be 1
    num_squares = 1
    curr = salbLL
    # loop through each node and count each node
    while curr.next != salbLL:
        num_squares += 1
        curr = curr.next
    return num_squares


def move(curr: 'SALBnode', stepsize: int) -> 'SALBnode':
    ''' The function will take two parameters which are a curr node and the
    stepsize the player will move.
    The function woll move the player based on the stepsize and
    finally return the new node that player arrived.
    Everytime call this function will move the player based on
    the stepsize.

    REQ: stepsize > 0

    >>> board = SALboard(100, {1: 3, 9:72})
    >>> board = salb2salbLL(board)
    >>> curr = move(board, 3)
    >>> curr == board.next.next.next
    True

    >>> board = SALboard(2, {})
    >>> board = salb2salbLL(board)
    >>> curr = move(board, 3)
    >>> curr == board.next.next.next
    True

    >>> board = SALboard(2, {})
    >>> board = salb2salbLL(board)
    >>> curr = move(board, 3)
    >>> curr == board.next.next
    False
    '''
    for i in range(stepsize):
        curr = curr.next
    return curr


def where_start(start: 'SALBnode', stepsize: int) -> 'SALBnode':
    ''' The function will take two parameters which are a salbnode and the
    stepsize.
    The function will give the node that the play will start based on
    stepsize.
    The start is the beginning of the board.

    REQ: stepsize > 0

    >>> board = SALboard(2, {})
    >>> board = salb2salbLL(board)
    >>> curr = where_start(board, 3)
    >>> curr == board.next.next.next
    False

    >>> board = SALboard(2, {})
    >>> board = salb2salbLL(board)
    >>> curr = where_start(board, 3)
    >>> curr == board.next.next
    True

    >>> board = SALboard(100, {1: 3, 9:72})
    >>> board = salb2salbLL(board)
    >>> curr = where_start(board, 3)
    >>> curr == board.next.next.next
    False

    >>> board = SALboard(100, {1: 3, 9:72})
    >>> board = salb2salbLL(board)
    >>> curr = where_start(board, 3)
    >>> curr == board.next.next
    True
    '''
    for i in range(stepsize-1):
        start = start.next
    return start
