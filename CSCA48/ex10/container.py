class Queue():
    def __init__(self: 'Queue') -> None:
        # Representation invariant:
        # _contents is a list.
        # len(_contents) is the number of elements in me.
        # If len(_contents)>0, then
        #   _contents[0] is the head,
        #   _contents[-1] is the tail,
        #   _contents[:] contains
        #    the elements in the order they were inserted.
        self._contents = []

    def __str__(self: 'Queue') -> str:
        s = ""
        for item in self._contents:
            s = s + str(item) + ", "
        return s[:-2]

    def put(self: 'Queue', item: 'object') -> None:
        self._contents.append(item)

    def get(self: 'Queue') -> object:
        return self._contents.pop(0)

    def is_empty(self: 'Queue') -> bool:
        return (len(self._contents) == 0)

    def peek(self):
        return self._contents[0]

    def copy(self):
        copy = Queue()
        copy._contents = self._contents[:]
        return copy


# A stack class
# Uses a list for the stack.
# Raises EmptyStackError when popping from an empty stack.
# Needs comments.

class ContainerEmptyException(Exception):
    pass

class Stack():
    def __init__(self: 'Stack') -> None:
        self._contents = []

    def __str__(self: 'Stack') -> str:
        s = ""
        for item in self._contents:
            s = s + str(item) + ", "
        return s[:-2]

    def put(self: 'Stack', item: 'object') -> None:
        self._contents.append(item)

    def get(self: 'Stack') -> object:
        if self.is_empty():
            raise ContainerEmptyException
        return self._contents.pop()

    def is_empty(self: 'Stack') -> bool:
        return (len(self._contents) == 0)

    def peek(self):
        return self._contents[-1]

    def copy(self):
        copy = Stack()
        copy._contents = self._contents[:]
        return copy


class ContainerFullException(Exception):
    pass


class Bucket:
    def __init__(self: 'Stack') -> None:
        self._contents = []

    def __str__(self: 'Stack') -> str:
        s = ""
        for item in self._contents:
            s = s + str(item) + ", "
        return s[:-2]

    def put(self: 'Stack', item: 'object') -> None:
        if self.is_empty():
            self._contents.append(item)
        else:
            raise ContainerFullException

    def get(self: 'Stack') -> object:
        if self.is_empty():
            raise EmptyStackError
        return self._contents.pop()

    def is_empty(self: 'Stack') -> bool:
        return (len(self._contents) == 0)

    def peek(self):
        return self._contents[-1]

    def copy(self):
        copy = Bucket()
        copy._contents = self._contents[:]
        return copy
