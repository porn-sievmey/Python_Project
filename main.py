class BankAccount :
    #consructor
    def __init__(self,name, balance, secret):
        self.balance = balance
        self.__secret = secret
        self.name = name

    #check balance
    def checkBalance(self, secret):
        if secret == self.__secret:
            print(f'{self.name}: your balance is {self.balance}')
        else:
            print(f"{self.name}: you can't check balance!!!")

    #deposit
    def deposet(self, amount, secret):
        if secret == self.__secret:
            self.balance +=amount
            print(f"{self.name} your deposit is {amount}")
        else:
            print("Your secret is not correct. Please, try again!!!")
    #withdraw
    def withdraw(self, secret,balance, amount):
        if secret == self.__secret:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Your money withdraw is {self.balance}')
            else:
                print("Your balance is not enough")
        else:
            print("Your secret is not correct. Please, try again!!!")

    #payment
    def payment(self, service_type, amount, secret):
        if secret == self.__secret:
            if self.balance >= amount:
                self.balance -= amount
                print(f'{self.name} paid {amount} for {service_type}' )
            else:
                print("Your balance is not enough")
        else:
            print("Your secret is not correct. Please, try again!!!")

    #transfer
    def transfer(self, to_name, amount, secret):
        if secret == self.__secret:
            if self.balance >= amount:
                to_name.balance += amount
                print(f"{self.name} transfer {amount} to {to_name.name}")
            else:
                print("Your balance is not enough")
        else:
            print("Your secret is not correct. Please, try again!!!")

    #Take loan
    def takeLoan(self,amount):
            self.balance += amount
            print(f'Loan approved! New your balance is {self.balance}')

#create abject
Thida = BankAccount("Thida", 2000, 246)
# Bopha = BankAccount("Bopha",2500,168)

#Create class Student_BankAccount
class Student_BankAccount(BankAccount) :
    def withdraw(self,secret, Withdraw):
        if Withdraw <= 499:
            self.balance -= Withdraw
            print(f"Your total balance is {self.balance}")
        else:
            print("You are a student cannot withdraw 499$up")
#create abject
Chantha = Student_BankAccount("Chantha",2000,666)
Chantha.withdraw(666,660)
Chantha.checkBalance(666)


#Create class SavingAcc
class SavingAccount(BankAccount):
    def calculate_interest(self):
        self.balance += 10
        print(f"Your total balance is {self.balance}")

#create object
Dara = SavingAccount("Dara",1000,132)
#Dara.checkBalance(132)
#Dara.deposet(500,132)

#Create class PremiumSaving
class PremiumSaving(SavingAccount):
    def deposet(self, amount, secret):
            self.balance += amount * 0.02
            print(f'Your total balance is{self.balance}')
#Create object
lyly = PremiumSaving("lyly",1000,111)

lyly.deposet(500,111)

# Create class BusinessAccount
class BusinessAccount(BankAccount):
    def takeLoan(self, amount):
        if amount >= 1000:
            self.balance += (amount - (amount * 0.01))
            print(f'Loan approved! your balance has accrued interest is {self.balance}')
        else:
            self.balance += (amount - (amount * 0.02))
            print(f'Loan approved! your balance has accrued interest is {self.balance}')



#create object
Kaka = BankAccount("Kaka",500,333)
Kaka.checkBalance(333)
Kaka.takeLoan(110)




















