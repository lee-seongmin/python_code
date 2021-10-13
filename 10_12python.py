# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:06:36 2021

@author: pc03
"""

class Employee:
    empCount = 1
    emp_num = 0
    def __init__(self, name = '최사장', salary = 1000, rank='사장'):
        self.__name = name
        self.__salary = salary
        self.__rank = rank
        Employee.empCount += 1
        Employee.emp_num += 1
        self.__number = Employee.emp_num
    def setname(self, name):
        self.__name = name
    def setsalary(self, salary):
        self.__salary = salary
    def setrank(self, rank):        
        print(self.__rank)
        self.__rank = rank
        print(self.__rank)
        print("승급이 완료되었습니다.")
        
    def __str__(self):
        return '(%s, %s, %d, %d)' % (self.__name, self.__rank, self.__salary, self.__number)
list_name = ['이부장', '권부장', '김팀장', '곽팀장', '박사원', '강사원', '윤사원']
list_salary = [900, 950, 900, 850, 800, 750, 700]
list_rank = ['부장', '부장', '팀장','팀장', '사원', '사원', '사원']
list_company = []

choi = Employee()
print(choi) # 최사장
for i in range(7):
    list_company.append(Employee(list_name[i], list_salary[i], list_rank[i]))
    print(list_company[i])
list_company[2].setsalary(950)
list_company[2].setrank('부장')
print(list_company[2])#메소드 실행방법