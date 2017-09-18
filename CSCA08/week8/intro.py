class MyCoolClass():
    '''A class with no real functionality, use to explain how OOP works'''

    def __init__(self, d):
        self.data = d

if __name__ == "__main__":
    alice = MyCoolClass("Hello")
    bob = MyCoolClass("Bye")
    print(alice.data)
    print(bob.data)