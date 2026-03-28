class Account:
    def __init__(self, owner, balance):
        self.owner=self.balance

    def deposit(self, amount):
        self.balance +=amount

    def withdraw(self , amount):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
             self.balance -= amount
             return self.balance
b_val, w_val= map(int , input().split()) 
my_account=Account("User", b_val)
result= my_account.withdraw(w_val)
print(result)

