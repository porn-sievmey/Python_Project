class BankAccount :
    #consructor
    def __init__(self,name, balance, secret):
        self.balance = balance
        self.__secret = secret
        self.name = name

    #check balance
    def chechBalance(self, secret):
        if secret == self.__secret:
            print(f'{self.name}: your balance is {self.balance}')
        else:
            print(f"{self.name}: you can't check balance!!!")

    #deposit
    def deposet(self, amount, secret):
        if secret == self.__secret:
            self.balance +=amount
            print(f"{self.name} your deposit is{amount}")
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

#create abject
Thida = BankAccount("Thida", 2000, 246)
Bopha = BankAccount("Bopha",2500,168)

#ex transfer
Thida.transfer(Bopha,1000,246)

#ex checkbalance
Bopha.chechBalance(168)

