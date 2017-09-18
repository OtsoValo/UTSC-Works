def traverse(container, root):
    result = ''
    container.put(root)
    while(not container.is_empty()):
        next_node = container.get()
        if(next_node is not None):
            result += next_node.data
            container.put(next_node.left)
            container.put(next_node.right)
    return result

# Queue Class
class EmptyQueueError(Exception):
    pass

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
        if self.is_empty():
            raise EmptyQueueError
        return self._contents.pop(0)

    def is_empty(self: 'Queue') -> bool:
        return (len(self._contents) == 0)


# Stack class
class EmptyStackError(Exception):
    pass

class Stack():
    def __init__(self: 'Stack') -> None:
        self._contents = {}
        self._num_items = 0

    def __str__(self: 'Stack') -> str:
        s = ""
        for i in range(1, self._num_items + 1):
            s = s + str(self._contents[i]) + ", "
        return s[:-2]

    def put(self: 'Stack', item: 'object') -> None:
        self._num_items = self._num_items + 1
        self._contents[self._num_items] = item

    def get(self: 'Stack') -> object:
        if self.is_empty():
            raise EmptyStackError
        item = self._contents[self._num_items]
        del self._contents[self._num_items]
        self._num_items = self._num_items - 1
        return item

    def is_empty(self: 'Stack') -> bool:
        return (self._num_items == 0)


# alternating Queue class
class AlternatingQueue:
    def __init__(self: 'AlternatingQueue') -> None:
            self._contents = []
            self._last_op_on_left = False
    
    def __str__(self: 'AlternatingQueue') -> str:
        s = ""
        for item in self._contents:
            s = s + str(item) + ", "
        return s[:-2]

    def put(self: 'AlternatingQueue', item: 'object') -> None:
        if self._last_op_on_left:
            self._contents.append(item)
        else:
            self._contents.insert(0, item)
        self._last_op_on_left = not self._last_op_on_left

    def get(self: 'AlternatingQueue') -> object:
        if self.is_empty():
            raise EmptyQueueError
        if self._last_op_on_left:
            item = self._contents.pop()
        else:
            item = self._contents.pop(0)
        self._last_op_on_left = not self._last_op_on_left
        return item

    def is_empty(self: 'AlternatingQueue') -> bool:
        return (len(self._contents) == 0)


# neck Queue class
class NeckQueue():
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
        if self.is_empty():
            raise EmptyQueueError
        if len(self._contents) == 1:
            return self._contents.pop()
        else:
            return self._contents.pop(1)

    def is_empty(self: 'Queue') -> bool:
        return (len(self._contents) == 0)


# Steue class
class Steue:
    def __init__(self: 'AlternatingQueue') -> None:
            self._contents = []
            self._last_op_on_right = False
    
    def __str__(self: 'AlternatingQueue') -> str:
        s = ""
        for item in self._contents:
            s = s + str(item) + ", "
        return s[:-2]

    def put(self: 'AlternatingQueue', item: 'object') -> None:
        self._contents.append(item)

    def get(self: 'AlternatingQueue') -> object:
        if self.is_empty():
            raise EmptyQueueError
        if self._last_op_on_right:
            item = self._contents.pop(0)
        else:
            item = self._contents.pop()
        self._last_op_on_right = not self._last_op_on_right
        return item

    def is_empty(self: 'AlternatingQueue') -> bool:
        return (len(self._contents) == 0)


# BST class
class BinTreeNode:
    """
    A node in a binary tree.
    """

    def __init__(self, data, left=None, right=None):
        """ (BinTreeNode, str, BinTreeNode, BinTreeNode) -> NoneType

        Initialize a new BinTreeNode with data, left and right children.
        """

        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """ (BinTreeNode) -> str

        Return a string representing self.
        """

        return ("BinTreeNode(" + repr(self.data) + ", " +
                repr(self.left) + ", " + repr(self.right) + ")")


if __name__ == '__main__':
    tree = BinTreeNode('C')
    tree.right = BinTreeNode('O')
    tree.right.left = BinTreeNode('M')
    tree.right.left.left = BinTreeNode('E')
    tree.right.right = BinTreeNode('P')
    tree.right.right.right = BinTreeNode('U')
    tree.right.right.right.left = BinTreeNode('T')
    tree.right.right.right.left.left = BinTreeNode('R')
    tree.right.right.right.left.left.right = BinTreeNode('S')
    stack = Stack()
    queue = Queue()
    neck_queue = NeckQueue()
    alternating_queue = AlternatingQueue()
    steue = Steue()
    print('Stack: ' + traverse(stack, tree))
    print('Queue: ' + traverse(queue, tree))
    print('AlternatingQueue: ' + traverse(alternating_queue, tree))    
    print('NeckQueue: ' + traverse(neck_queue, tree))
    print('Steue: ' + traverse(steue, tree))
