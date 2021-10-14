class Calculater:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val
class UpgradeCalculater(Calculater):
    def minus(self, val):
        self.value -= val
cal = UpgradeCalculater()
cal.add(10)
cal.minus(7)
print(cal.value)
class MaxLimitCalculater(Calculater):
    def add(self, val):
        self.value += val
        if(self.value > 100):
            self.value = 100            
ca = MaxLimitCalculater()
ca.add(60)
ca.add(50)
print(ca.value)