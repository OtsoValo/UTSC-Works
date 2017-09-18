class Person:
    '''A class to represent a human being'''

    def __init__(self, firstname, lastname, age):
        '''(Person, str, str, int) -> NoneType
        Create a new person named firstname lastname, who is age years old
        REQ: age >=0
        '''
        self._firstname = firstname
        self._lastname = lastname
        self._age = age

    def set_age(self,age):
        '''(Person, int) -> Nonetype
        Sets the age of the person
        REQ: age >=0
        '''        
        self._age = age

    def __str__(self):
        '''(Person) -> str
        Return a string representing this Person
        '''
        return self._firstname + " " + self._lastname + ", " + str(self._age) + " years old" 

if __name__ == "__main__":
    alice = Person("Alice","Alicson",28)
    print (alice)