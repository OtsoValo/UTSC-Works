from Student import Student
from Bank import BankAccount

# alice = Person("Alice","Alicson",28)
alice = Student("Alice","Alicson",28, "1234", 3.9)
alice_account = BankAccount(alice)
alice_account.credit(1000)
print(alice_account)

print(alice_account.debit(500))
print(alice_account)  

print(alice_account.debit(600))
print(alice_account)  