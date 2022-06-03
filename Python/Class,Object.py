# import 쓰는 법:
# import 모듈이름
# from 모듈이름 import *
# from 모듈이름 import 모듈함수1, 모듈함수2 

from ast import Pass


class FourCal:
    def __init__(self, first, second): # 생성자. 생성자는 객체가 생성될 때 자동으로 호출되는 메소드. 가장 먼저 실행된다.
        self.first = first
        self.second = second
    
    def setdata(self, first, second): # self는 setdata를 호출한 객체 a가 자동으로 전달된다
        self.first = first
        self.second = second
        
    def add(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second
        


# 상속
class MoreFourCal(FourCal): # FourCal의 모든 기능을 수행할 수 있다.
    def pow(self):
        return self.first ** self.second
    
a = MoreFourCal(4, 2)
print(a.pow())

# 실행파일이 main일 때 실행된다. 
# 즉, 다른 파일에서 이 모듈을 불러와서 사용할 때는 거짓이 되어 if 다음 문장이 실행되지 않는다.
if __name__ == "__main__":
    pass