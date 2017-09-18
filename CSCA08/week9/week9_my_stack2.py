class Stack():
    '''A last-in, first-out (LIFO) stack of items'''

    def __init__(self):
        '''(Stack) -> NoneType
        Create a new, empty Stack.
        '''
        # this time, let's represent our stack with a list such that the top
        # of the stack is at the 0th element of the list
        self._contents = []

    def push(self, new_obj):
        '''(Stack, object) -> NoneType
        Place new_obj on top of this stack.
        '''
        # putting a new element on top of the stack means putting that element
        # at the beginning of our list
        self._contents.insert(0, new_obj)

    def pop(self):
        '''(Stack) -> object
        Remove and return the top item in this stack.
        '''
        # the top item on the stack is the 0th item in the list
        # so first save it
        top_item = self._contents[0]
        # then remove it from the list
        self._contents = self._contents[1:]
        # then return it
        return top_item

    def is_empty(self):
        '''(Stack) -> bool
        Return True iff this stack is empty.
        '''
        # just for fun, let's try a different way of testing for an empty
        # list this time (which means an empty stack)
        return len(self._contents) == 0


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
