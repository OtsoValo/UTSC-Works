from Person import Person
from BankAccount import BankAccount

class Bank():

    def __init__(self,db_file):
        ''' (Bank,str)-> NoneType
        initialize the Bank database from a file given as argument
        '''
        self._database = set()
        handle = open(db_file,"r")
        lines = handle.readlines()
        for line in lines:
            data = line.split(",")
            p = Person(data[0],data[1],data[2])
            a = BankAccount(p)
            a.credit(int(data[3]))
            self._database.add(a)

    def total_asset(self):
        ''' (Bank)-> int
        returns the total asset that the Bank owns
        '''
        result = 0
        for account in self._database:
            result += account.get_balance()
        return result


if __name__ == "__main__":
    canada_bank = Bank("database.txt")
    for a in canada_bank._database:
        print(a)
    print(canada_bank.total_asset())