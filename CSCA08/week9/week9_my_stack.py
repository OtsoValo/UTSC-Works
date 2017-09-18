class Stack():
    '''A last-in, first-out (LIFO) stack of items'''

    def __init__(self):
        '''(Stack) -> NoneType
        Create a new, empty stack.
        '''
        # we'll hold our elements in a list, with the top of
        # the stack being the end of the list
        self._contents = []

    def push(self, new_obj):
        '''(Stack, object) -> NoneType
        Place new_obj on top of this stack.
        '''
        # putting a new item on the stack just means adding
        # a new item to the end of the list
        self._contents.append(new_obj)

    def pop(self):
        '''(Stack) -> object
        Remove and return the top item in this stack.
        '''
        # save the top item from the stack (last item in the list)
        top_item = self._contents[-1]
        # remove the item we just saved from our list
        self._contents = self._contents[:-1]
        # and return that item
        return top_item

    def is_empty(self):
        '''(Stack) -> bool
        Return True iff this stack is empty
        '''
        # if we have an empty list, our stack is empty
        return self._contents == []


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
