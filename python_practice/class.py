from typing import AsyncGenerator


class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __del__(self):
        print("나의 죽음을 알리지마라")
    def who(self):
        print(f"이름 : {self.name}, 나이 : {self.age}, 성별 : {self.sex}")
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
areum=Human('모름', 0, '모름')
print(f"이름 : {areum.name}, 나이 : {areum.age}, 성별 : {areum.sex}")
areum.setInfo('아름', 25, '여성')
areum.who()
del areum
