"""
# Copyright Nick Cheng, 2016, Qiuyu Huang, 2017
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2017
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

# Do not change this import statement, or add any of your own!
from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree

# Do not change any of the class declarations above this comment


# Add your functions here.
def build_tree(formula):
    ''' (str) -> FormulaTree

    The function will create a FormulaTree based on
    the input formula str.
    The input str has to be in the right form otherwise,
    return None.
    The function will return a root of FormulaTree if input
    formula is in the valid form.

    The input str has to be in a valid form, which is:
    1. "+" and "*" connect to leaf and arounded by "(" and ")"
    2. for "-", there is no need for parenthesis.

    The function will start at an empty root,
    when we have a "(", we will create a left child, if
    we have a leaf, we will create that leaf and then go back to
    its parent and continune. When we have a ")" we will go
    back to parent. It has used concept of stack, which is
    a list to store parents.

    The function will change input formula into a good form, which is
    for each "-" sign, we have a matching ")" after its leaf.
    For example "-x" will change to "-x)"; "-(-x+y)" will change to
    "-(-x)+y))"

    >>> build_tree('a+b') == None
    True
    >>> build_tree('(a)') == None
    True
    >>> build_tree('-(a)') == None
    True
    >>> build_tree('(a+b+c)') == None
    True

    >>> tree = build_tree('(b+(c+d))')
    >>> tree == OrTree(Leaf('b'), OrTree(Leaf('c'), Leaf('d')))
    True
    >>> tree = build_tree('(x+y)')
    >>> tree == OrTree(Leaf('x'), Leaf('y'))
    True
    >>> tree = build_tree('-(--x+y)')
    >>> tree == NotTree(OrTree(NotTree(NotTree(Leaf('x'))), Leaf('y')))
    True
    >>> tree = build_tree('------x')
    >> tree == NotTree(NotTree(NotTree(NotTree(NotTree(NotTree(Leaf('x')))))))
    True
    '''
    # create a list to store all parents
    stack = []
    # create an empty tree, add it into stack and let curr be it
    tree = FormulaTree(None, [])
    stack.append(tree)
    curr = tree
    # try to do the following
    try:
        # change formula into a good form for code
        formula = build_tree_helper(formula)
        # loop through each symbol in formula
        for s in formula:
            # if we have "("
            if s == '(':
                # create a left subtree, and store parent in stack
                left = FormulaTree(None, [])
                curr.children.append(left)
                stack.append(curr)
                curr = curr.children[0]
            # if we have a laef
            elif s not in ['+', '*', '-', ')']:
                # if s is not alphabet or it is upper case, return None
                if not s.isalpha() or s.isupper():
                    return None
                # create a leaf of its symbol
                leaf = Leaf(s)
                # get the parent from stack
                parent = stack.pop()
                # if curr node has parent
                if curr in parent.children:
                    # let parent pointer to this leaf
                    index = parent.children.index(curr)
                    parent.children[index] = leaf
                    # let curr be parent (go back)
                    curr = parent
                # if curr node has no parent
                else:
                    # let tree be curr leaf
                    tree = leaf
                # if after any leaf, stack is empty, then
                # it must be in invalid form, raise error
                if len(formula) != 1 and stack == []:
                    raise SyntaxError
            # if we have "+", "*", or "-"
            elif s in ['+', '*', '-']:
                # get the parent from stack
                parent = stack[-1]
                # create a new node for its child
                new_node = FormulaTree(None, [])
                # if symbol is * then create AndTree
                if s == '*':
                    replace = AndTree(curr.children[0], new_node)
                # if symbol is + then create OrTree
                elif s == '+':
                    replace = OrTree(curr.children[0], new_node)
                # if symbol is - then create NotTree
                else:
                    replace = NotTree(new_node)
                # if curr node has parent
                if curr in parent.children:
                    # get the index and let parent pointer to curr node
                    index = parent.children.index(curr)
                    parent.children[index] = replace
                    # get the new curr node
                    curr = replace
                # if curr node has no parent
                else:
                    # let tree be replace node
                    tree = replace
                    # get new curr node and reset stack
                    curr = tree
                    stack = [curr]
                # put curr into stack as parent and get next curr
                stack.append(curr)
                curr = curr.children[0] if s == '-' else curr.children[1]
            # if we have ")", then let curr go back to parent
            elif s == ')':
                curr = stack.pop()
            # if there is other situation, it must be error
            else:
                raise SyntaxError
    # if any error, then return None since it is an invalid form
    except:
        return None
    # if stack has anything which means invalid form, or
    # there are still some FormulaTree in result tree, return None
    if stack != [] or 'FormulaTree' in str(tree):
        return None
    return tree


def build_tree_helper(formula):
    ''' (str) -> str

    The function will get a normal formula tree,
    and return a better string of formula tree in order
    to build tree.
    For each "-" sign, we will add a extra ")" in the end of
    "-" sign.
    For example, "-x" will change to "-x)"; "-(-x+y)" will change to
    "-(-x)+y))".

    If the function has "-" precede the brackets, then it will call
    its helper function to count the index of bracket and then
    compute.

    >>> build_tree_helper('(x+y)')
    '(x+y)'
    >>> build_tree_helper('(-x+y)')
    '(-x)+y)'
    >>> build_tree_helper('-(-x+-y)')
    '-(-)x+-)y))'
    '''
    # initialize index in str
    index = 0
    # loop through each symbol in formula
    while index < len(formula):
        # if we have "-" then add ")", otherwise, no change for it
        if formula[index] == '-':
            # if the next symbol is "("
            if formula[index+1] == '(':
                # call count_bracket to get index for ")"
                new_i = count_bracket(formula, index)
                # add brackets into formula
                formula = formula[:index+new_i] + ')' + formula[index+new_i:]
            # if the next symbol is "-"
            elif formula[index+1] == '-':
                # initialize count for counting "-"
                count = 1
                minus_index = 2
                # loop through each symbol after "-", if there is another
                # "-", then add count for 1
                while formula[index+minus_index] == '-':
                    count += 1
                    minus_index += 1
                # if "-" precede a bracket, then call count_bracket
                if formula[index+minus_index] == '(':
                    new_i = count_bracket(formula, minus_index-2)
                    # get the new formula
                    formula = formula[:minus_index+index+new_i-2] + ')'\
                        * (count+1) + formula[minus_index+index+new_i-2:]
                # if "-" precedes just one element
                else:
                    new_i = minus_index - 1
                    # add brackets after this element
                    formula = formula[:index+new_i+2] + ')' * (count+1)\
                        + formula[index+new_i+2:]
                # since there are a lot of "-", we skip all the "-"
                index += count
            # if there is only one element then just add one brackets
            else:
                formula = formula[:index+2] + ')' + formula[index+2:]
        index += 1
    return formula


def count_bracket(formula, index):
    ''' (str, int) -> int

    The function will receive a formula string and an index
    where we have a "-" precede "(".
    The function will count the brackets and return
    the new index, n_index, for the ")"
    The n_index is the DISTANCE between "(" and ")", it is NOT the
    index of ")" in str.

    >>> count_bracket('(x+y)', 0)
    5
    >>> count_bracket('(-x+y)', 0)
    6
    >>> count_bracket('-----(-x+y)', 6)
    5
    '''
    # count the left parenthesis "("
    count = 1
    # initialize new index for tracing items in parenthesis
    new_i = 2
    # loop through each symbol after "-" and "("
    # if find until the last one or find matching ")", stop
    # the loop
    while index+new_i < len(formula) and count != 0:
        # if find a "(", let count plus one
        if formula[index+new_i] == '(':
            count += 1
        # if find a ")", let count minus one
        elif formula[index+new_i] == ')':
            count -= 1
        # check next symbol
        new_i += 1
    # return the new index
    return new_i


def draw_formula_tree(root):
    ''' (FormulaTree) -> str

    The function will receive a root which is a FormulaTree,
    and then return a str which is a tree of that
    FormulaTree.
    The input FormulaTree must be in the valid form,
    otherwise the result would not be expected.

    REQ: type of root has to be formulatree

    >>> formula = build_tree('-(a*b)')
    >>> draw_formula_tree(formula)
    '- * b\n    a'

    >>> formula = build_tree('-(a*(c*(-d+a)))')
    >>> draw_formula_tree(formula)
    '- * * + a\n        - d\n      c\n    a'

    >>> formula = build_tree('((-a+b)*-(-b+a))')
    >>> draw_formula_tree(formula)
    '* - + a\n      - b\n  + b\n    - a'
    '''
    return draw_tree_helper(root, '  ')


def draw_tree_helper(root, indent):
    ''' (FormulaTree, str) -> str

    The function is the helper function for draw_formula_tree.
    The function will receive a FormulaTree as paremeter,
    and return a str which represents the tree.
    The input FormulaTree must be in the valid form

    REQ: type of root has to be formulatree

    >>> formula = build_tree('-(a*b)')
    >>> draw_tree_helper(formula, '  ')
    '- * b\n    a'

    >>> formula = build_tree('-(a*(c*(-d+a)))')
    >>> draw_tree_helper(formula, '  ')
    '- * * + a\n        - d\n      c\n    a'

    >>> formula = build_tree('((-a+b)*-(-b+a))')
    >>> draw_tree_helper(formula, '  ')
    '* - + a\n      - b\n  + b\n    - a'
    '''
    # initialize the tree str
    tree = ''
    # if curr node is a leaf then let tree be symbol
    if root.children == []:
        tree = root.symbol
    # if curr node is "+", "*", or "-"
    else:
        # if curr node is "*", or "+"
        if root.symbol in ['+', '*']:
            # add symbol into tree
            tree = root.symbol + ' '
            # a recursive call to get right tree, and add it into tree
            right = draw_tree_helper(root.children[1], indent+'  ') + '\n'
            tree += right
            # a recursive call to get left tree,
            # and add it into tree with indentation
            left = draw_tree_helper(root.children[0], indent+'  ')
            tree += indent + left
        # if curr node is "-"
        else:
            # a recursive call to get its child with indentation
            tree = '- ' + draw_tree_helper(root.children[0], indent+'  ')
    return tree


def evaluate(root, variables, values):
    ''' (FormulaTree, str, str) -> int

    The function will receive three parameters, which are
    a FormulaTree, and two string.
    The first str represents all the variables that appears
    in the root.
    The second str represents that values matching to variables.
    For each variable in variables has to have a matching
    value in values.
    The function will return a int which should be 1 or 0.
    '1' means True, '0' means False.
    The function will based on evaluate_helper which returns a bool.

    REQ: all the variables in root must in input first str, variables
    REQ: len(variables) == len(values)

    >>> a = Leaf('a')
    >>> b = Leaf('b')
    >>> c = Leaf('c')
    >>> d = Leaf('d')

    >>> evaluate(a, 'a', '0')
    0
    >>> evaluate(a, 'a', '1')
    1

    >>> formula = build_tree('-(a*b)')
    >>> evaluate(formula, 'ab', '11')
    0
    >>> evaluate(formula, 'ab', '10')
    1

    >>> formula = build_tree('-(a*b)')
    >>> evaluate(formula, 'ab', '10')
    1
    >>> evaluate(formula, 'ab', '11')
    0
    >>> evaluate(formula, 'ab', '01')
    1

    >>> formula = build_tree('-((a+b)*-(c*d))')
    >>> evaluate(formula, 'abcd', '1010')
    0
    >>> evaluate(formula, 'abcd', '1111')
    1
    >>> evaluate(formula, 'abcd', '1000')
    0
    >>> evaluate(formula, 'abcd', '0000')
    1
    >>> evaluate(formula, 'abcd', '0110')
    0
    '''
    # call helepr function
    value = evaluate_helper(root, variables, values)
    # return '1' if value is True, otherwise return '0'
    return 1 if value else 0


def evaluate_helper(root, variables, values):
    ''' (FormulaTree, str, str) -> bool

    The function is the helper function to evaluate
    The function will receive three parameters, which are
    a FormulaTree, and two string.
    The first str represents all the variables that appears
    in the root.
    The second str represents that values matching to variables.
    For each variable in variables has to have a matching
    value in values.

    REQ: all the variables in root must in input first str, variables
    REQ: len(variables) == len(values)

    >>> a = Leaf('a')
    >>> b = Leaf('b')
    >>> c = Leaf('c')
    >>> d = Leaf('d')

    >>> evaluate(a, 'a', '0')
    False
    >>> evaluate(a, 'a', '1')
    True

    >>> formula = build_tree('-(a*b)')
    >>> evaluate(formula, 'ab', '11')
    False
    >>> evaluate(formula, 'ab', '10')
    True

    >>> formula = build_tree('-(a*b)')
    >>> evaluate(formula, 'ab', '10')
    True
    >>> evaluate(formula, 'ab', '11')
    False
    >>> evaluate(formula, 'ab', '01')
    True

    >>> formula = build_tree('-((a+b)*-(c*d))')
    >>> evaluate(formula, 'abcd', '1010')
    False
    >>> evaluate(formula, 'abcd', '1111')
    True
    >>> evaluate(formula, 'abcd', '1000')
    False
    >>> evaluate(formula, 'abcd', '0000')
    True
    >>> evaluate(formula, 'abcd', '0110')
    False
    '''
    # if current tree has no child
    if len(root.children) == 0:
        # find the index of symbol in variables
        index = variables.index(root.symbol)
        # if matching value is 1 then return True, otherwise return False
        value = True if values[index] == '1' else False
    # if current tree has one child, for case of not
    elif len(root.children) == 1:
        # return not of the rest, and recall function with the child
        return not evaluate_helper(root.children[0], variables, values)
    # if current tree has two children, for case of '+' and '*'
    else:
        # recall the function to get both children value
        left_child = evaluate_helper(root.children[0], variables, values)
        right_child = evaluate_helper(root.children[1], variables, values)
        # if symbol is '+', then return left or right
        if root.symbol == '+':
            return left_child or right_child
        # if symbol is '*', then return left and right
        else:
            return left_child and right_child
    return value


def play2win(root, turns, variables, values):
    ''' (FormulaTree, str, str, str) -> int

    The function will receive four parameters which are
    a formulatree, a turns which repensents who will choose
    the value, a variables which are all the variables in tree, and
    a values which is existing values for this game.
    The function will give the winning strategy for current person
    who is playing the game.
    If current people is E, then default value is '1';
    A's default value is '0'.
    If there is no wining strategy or choose either '1' or '0'
    is the winning strategy, then the function will return
    default value.

    REQ: len(turns) == len(variables)

    >>> play2win(build_tree('-(x*y)'), 'EE', 'xy', '')
    0
    >>> play2win(build_tree('-(x*y)'), 'EE', 'xy', '0')
    1
    >>> play2win(build_tree('-(x*y)'), 'AA', 'xy', '')
    1
    >>> play2win(build_tree('-(x*y)'), 'AA', 'xy', '1')
    1
    >>> play2win(build_tree('((x+y)*-x)'), 'EE', 'xy', '')
    0
    >>> play2win(build_tree('((x+y)*-x)'), 'EE', 'xy', '0')
    1
    >>> play2win(build_tree('((x+y)*-x)'), 'AA', 'xy', '')
    0
    >>> play2win(build_tree('((x+y)*-x)'), 'EA', 'xy', '')
    1
    '''
    # get the winning strategy for current player by helper function
    result = play2win_helper(root, turns, variables, values)
    # if there is no winning strategy
    if result == '':
        # get the index of curr player
        index = len(variables) - len(values)
        # return default value
        return 1 if turns[-index] == 'E' else 0
    # if there is a winning strategy, then return it
    else:
        return int(result)


def play2win_helper(root, turns, variables, values):
    ''' (FormulaTree, str, str, str) -> str

    The function is the helper function for play2win.
    The difference between this function and play2win
    is that:
    If there is no wining strategy for current people, then return
    an empty string.
    The function will first put the default value into values,
    then check for the next person which may be E or A
    until to the last one.
    If first turn and second turn are the same player and it has
    winning startegy then just return current value.
    If they are different players, and second has winning strategy
    then check another value for first player, if second player
    still has winning strtegy, which means first player meant
    to be failure, or return empty str.

    REQ: len(turns) == len(variables)

    >>> play2win_helper(build_tree('-(x*y)'), 'EE', 'xy', '')
    '0'
    >>> play2win_helper(build_tree('-(x*y)'), 'EE', 'xy', '0')
    '1'
    >>> play2win_helper(build_tree('-(x*y)'), 'AA', 'xy', '')
    '1'
    >>> play2win_helper(build_tree('-(x*y)'), 'AA', 'xy', '1')
    '1'
    >>> play2win_helper(build_tree('((x+y)*-x)'), 'EE', 'xy', '')
    '0'
    >>> play2win_helper(build_tree('((x+y)*-x)'), 'EE', 'xy', '0')
    '1'
    >>> play2win_helper(build_tree('((x+y)*-x)'), 'AA', 'xy', '')
    '0'
    >>> play2win_helper(build_tree('((x+y)*-x)'), 'EA', 'xy', '')
    ''
    '''
    # base case: curr player is in last turn
    if len(values) == len(variables) - 1:
        # choose its default value and do the evaluation
        values = values + '1' if turns[-1] == 'E' else values + '0'
        result = evaluate_helper(root, variables, values)
        # if curr player can win by choosing default value
        if (result and turns[-1] == 'E') or (not result and turns[-1] == 'A'):
            # return default value
            return values[-1]
        # if it default value can't lead to win
        else:
            # choosing another value
            values = values[:-1] + '0' if turns[-1] == 'E'\
                else values[:-1] + '1'
            # get the result by evaluating it
            result = evaluate_helper(root, variables, values)
            # if it is winning strategy, then return it
            if (result and turns[-1] == 'E') or\
               (not result and turns[-1] == 'A'):
                return values[-1]
            # if there is no winning strategy, return empty str
            else:
                return ''
    # if curr pleyer is not the last one
    else:
        # find player's index
        index = len(variables) - len(values)
        # first choose default value and get the result by recursive call
        values = values + '1' if turns[-index] == 'E' else values + '0'
        value = play2win_helper(root, turns, variables, values)
        # if curr player and next player are not same
        if turns[-index] != turns[-index+1]:
            # if next player meant to be fail, return curr value
            if value == '':
                return values[-1]
            # if next player has winning strategy
            else:
                # choose another value for curr player, and get result
                values = values[:-1] + '0' if turns[-index] == 'E'\
                    else values[:-1] + '1'
                value = play2win_helper(root, turns, variables, values)
                # return winning strategy if next player meant to be fail
                return values[-1] if value == '' else ''
        # if curr player and next player are the same
        else:
            # if next player has no winning strategy
            if value == '':
                # choose another value for curr player and get result
                values = values[:-1] + '0' if turns[-index] == 'E'\
                    else values[:-1] + '1'
                value = play2win_helper(root, turns, variables, values)
                # return curr value if next player has winning strategy
                return '' if value == '' else values[-1]
            # if next player hsa winning strategy, return its value
            else:
                return value
