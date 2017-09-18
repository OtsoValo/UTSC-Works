class EmptyError(Exception):
    ''' The error will raise when container is empty and try to get the balue.
    '''
    pass


class ExistElementInBucketError(Exception):
    ''' The error will raise when try to add another element into container
    Bucket.
    '''
    pass


class Queue:
    ''' A normal Queue class.'''

    def __init__(self):
        self._contents = []

    def put(self, data):
        self._contents.append(data)

    def get(self):
        if self.isempty():
            raise EmptyError()
        return self._contents.pop(0)

    def isempty(self):
        return len(self._contents) == 0


class Stack:
    ''' A normal Stack class.'''

    def __init__(self):
        self._contents = []

    def put(self, data):
        self._contents.append(data)

    def get(self):
        if self.isempty():
            raise EmptyError()
        return self._contents.pop()

    def isempty(self):
        return len(self._contents) == 0


class Bucket:
    ''' The container Bucket class, Bucket will only save one element in it.'''

    def __init__(self):
        self._contents = []

    def put(self, data):
        self._contents.append(data)

    def get(self):
        if self.isempty():
            raise EmptyError()
        elif self.isfull():
            raise ExistElementInBucketError()
        return self._contents.pop()

    def isempty(self):
        return len(self._contents) == 0

    def isfull(self):
        return len(self._contents) == 1
