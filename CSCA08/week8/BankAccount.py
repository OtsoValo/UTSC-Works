from Person import Person

class BankAccount():
    
    def __init__(self, p):
        '''(BankAcount, Person) -> NoneType
        Create a new BankAccount own by a Person with a initial balance of $0 
        '''        
        self._owner = p
        self._balance = 0
    
    def credit(self,amount):
        '''(BankAcount, int) -> NoneType
        credit the BankAccount of the amount given as argument
        '''          
        self._balance += amount
        
    def debit(self,amount):
        '''if the remaining balance is greater than the amount given as argument, update the balance and returns True. Otherwise leaves the balance unchanged and return false '''
        if (self._balance >= amount):
            self._balance -= amount
            return True
        else:
            return False
        
    def get_balance(self):
            '''(BankAcount) -> int
            returns the current balance
            '''          
            return self._balance
    
    def __str__(self):
        '''(BankAccount) -> str
        Return a string representing this BankAccount
        '''        
        return str(self._owner) + ", has a remaining balance of $" + str(self._balance)
        
if __name__ == "__main__":
    alice = Person("Alice","Alicson",28)
    alice_account = BankAccount(alice)
    alice_account.credit(1000)
    print(alice_account)
    
    print(alice_account.debit(500))
    print(alice_account)  
    
    print(alice_account.debit(600))
    print(alice_account)        