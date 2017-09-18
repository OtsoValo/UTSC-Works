class Stack():
    
    def __init__(self):
        '''contructor'''
        self._data = []
    
    def push(self, obj):
        '''(Stack, Object) -> NoneType
        and something on the top of ythe stack
        '''
        self._data.append(obj)
        return None
    
    def pop(self):
        '''(Stack) -> Object
        remove and return the last object that was pushed to the stack
        '''
        result = self._data[-1]
        self._data = self._data[-1]
        return result
    
    def is_empty(self):
        '''(Stack) -> Boolean
        return true if the stack is empty, false otherwise
        '''
        return (len(self._data) == 0)