



class Stack:
    '''A last-in, first-out (LIFO) stack of items'''

    def __init__(self):
        '''(Stack) -> NoneType
        Create a new, empty stack.
        '''
        # this time, we'll store our stack as a dictionary
        # with the height of the item mapping to the item itself
        # we'll also need to keep track of the current height of
        # the stack
        self._contents = {}
        self._height = 0

    def push(self, new_obj):
        '''(Stack, object) -> NoneType
        Place new_obj on top of this stack.
        '''
        # putting a new item on top of the stack means adding it
        # to the dictionary at the current height (so the bottom
        # element will have index 0), and then increasing the
        # height accordingly
        self._contents[self._height] = new_obj
        self._height += 1

    def pop(self):
        '''(Stack) -> object
        Remove and return the top item in this stack.
        '''
        # top pop an item off the top of the stack, we first have
        # to decrease the height of the stack (remember that in our
        # dictionary we're indexing from 0)
        self._height -= 1
        # we don't really have to delete the item from the dictionary
        # because we'll never access it again, if we ever grow to that
        # height again, we'll just re-map the height value to a new
        # object
        return self._contents[self._height]

    def is_empty(self):
        '''(Stack) -> bool
        Return True iff this stack is empty
        '''
        # if our height is zero, this means our stack is empty
        return self._height == 0


if (__name__ == '__main__'):
    # this is just some sample code that uses our stack
    # if we keep our ADT the same in each of our implementations
    # of our stack, then we should be confident that this code
    # will work identically each time
    stk = Stack()
    stk.push('a')
    stk.push('b')
    stk.push('c')
    print(stk.pop())
    stk.push('d')
    while(not stk.is_empty()):
        print(stk.pop())
