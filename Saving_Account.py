from Account import Account

class Savings(Account):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.interest_rate = 0.02
        self.withdrawal_limit = 100
    
    def withdraw(self,amount):
        if amount>self.withdrawal_limit:
            print(f"Withdrawal denied.Amount exceeds the withdrawal limit of ${self.withdrawal_limit}.")
        elif O < amount <= self.get_balance():
            super().withdraw(amount)
        else:
            print("Invalid withdrawal amount or insufiicent funds.")
    
    def apply_interest(self):
        interest = self.get_balance * self.interest_rate
        self.deposit (interest)
        print(f"Interest of ${interest} applied.New balance: {self.get_balance()}") 

#Test the Savings Account
print("---Savings Account---")
savings= Savings ("Alice", 1000)
print (f"Initial balance:{savings.get_balanced()}")
savings.deposit(500)
savings.withdraw(200)#Should be denied (exceeds $100 limit)
savings.withdraw (50)#Should succeed

