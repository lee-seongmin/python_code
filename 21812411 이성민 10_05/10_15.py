class car:
    def __init__(self,color = None,velo=0 ,geer=0):
        self.__color = color
        self.__velo = velo
        self.__geer = geer
        
    def set_color(self):
        color = input("무슨 색? ")
        self.__color = color
        print("차의 색상은 {}".format(self.__color))
        
    def set_velo(self):
        velo = int(input("가속할 속도는? "))
        self.__velo += velo
        print("달리는 속도는 {}".format(self.__velo))

    def set_mino(self):
        velo = int(input("감속할 속도는? "))
        self.__velo -= velo
        print("달리는 속도는 {}".format(self.__velo))
        
    def set_geer(self):
        geer = int(input("바꿀 기어는? "))
        self.__geer = geer
        print("현재 기어는 {}".format(self.__geer))
        
    def __str__(self):
        return "(%s, %d, %d)" % (self.__color,self.__velo,self.__geer)
        
a = car("빨강",100,3)

state = True

while(state):
    print("현재 상태는 {}".format(a))
    a.set_color()
    c = int(input("1. 가속 2. 감속"))
    if (c==1):
        a.set_velo()
    else:
        a.set_mino()
    a.set_geer()
    b=input("끝낼까요?")
    if b=='y':
        state = False