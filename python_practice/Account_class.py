import random

class Account:
    account_num = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "Sc은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3) + '-'
        num2 = str(num2).zfill(2) + '-'
        num3 = str(num3).zfill(6)
        self.account_number = (num1 + num2 + num3)
        Account.account_num += 1
    def get_account_num(self):
        print(self.account_num)
    def deposit(self,money):
        self.deposit_count=0
        if money >=1 :
            self.balance += money
        if self.deposit_count % 5==0:
            self.balance += self.balance / 100
        self.deposit_count+=1
    def withdraw(self,money):
        if money <= self.balance:
            self.balance -= money
    def __str__(self):
        return f"은행이름 : {self.bank}\n예금주 : {self.name}\n계좌번호 : {self.account_number}\n잔고 : {self.balance}원"
kim = Account("김민수", 1000)
print(kim.account_number)
kim.get_account_num()
print(kim)