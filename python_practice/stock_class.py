class Stock:
    def __init__(self, name, code, PER, PBR, suik):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.suik = suik
    def setName(self, name):
        self.name = name
    def setCode(self, code):
        self.code =code
    def get_code(self):
        return self.code
    def get_name(self):
        return self.name
    def set_per(self, PER):
        self.PER = PER
    def set_pbr(self, PBR):
        self.PBR = PBR
    def set_suik(self, suik):
        self.suik = suik
삼성 = Stock("삼성","005930", 15.79, 1.33, 2.83)
print(삼성.suik)
삼성.setName('삼성전자')
print(삼성.name)
print(삼성.get_name(),삼성.get_code())
print(삼성.PER)
삼성.set_per(12.75)
print(삼성.PER)
h = Stock("현대차","005380", 8.70, 0.35, 4.27)
l = Stock("LG전자", "006570", 317.34, 0.69, 1.37)
stockList = [삼성, h, l]
for i in stockList:
    print(i.code, i.PER)