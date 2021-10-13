# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:09:27 2021

@author: pc03
"""

class Counter:
    def __init__(self):
        self.count=0
    def reset (self): #self를 붙이는 이유 인스턴스의 정보를 넘겨주기 위해서 사용한다.
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count
a = Counter()
a.increment()

a.reset()
a.increment()
print("카운터 a의 값은", a.get())

#%%
import math
class Circle:
    def __init__(self, radius=0):
        self.__radius = 0
    def cal_area(self):
        self.radius = radius
        area = math.pi*(radius**2)
        return area
    def cal_circumference(self):
        radius = self.radius 
        circumference = math.pi*2*radius
        return circumference
    def adjust(self, radius):
        self.__radius = radius
c = Circle(10)
print(c.cal_area())
#%%
class banksalad:
    def __init__(self, balance = 0):
        self.__balance = balance
    def deposit(self, deposit_fee):
        self.deposit_fee = deposit_fee
        self.balance += deposit_fee
        print("입금후 잔고는 {0}입니다.".format(self.balance))
    def withdraw(self, withdraw_fee):
        self.withdraw_fee = withdraw_fee
        if self.balance < withdraw_fee:
            print("잔고가 출금금액보다 모자랍니다.")
        else:
            self.balance -= withdraw_fee
            print("출금후 잔고는 {0}입니다.".format(self.balance))
    def Balanceinquiry(self, balance):
        print("현재잔고는 {0}입니다.".format(self.balance))
#%%
class Car:
    def __init__(self, speed = 0, gear = 'parking', color = 'black'):
        self.__color = color
        self.__gear =gear
        self.__speed = speed
    def set_gear(self, gear):
        self.__gear =gear
    def set_speed(self, speed):
        self.__speed = speed
    def __str__(self):
        return '(%d, %s, %s)' % (self.__speed, self.__gear, self.__color)
h = Car()
h.set_gear(2)
h.set_speed(40)
print(h)
#%%
