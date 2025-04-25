class 클래스:
    def __init__(self, 변수1, 변수2):
        # 생성자 -> 인스턴스 변수 정의
        self.변수1 = 변수1
        self.변수2 = 변수2

    #toString() __str__이 __repr__보다 우선 순위가 높다. 하는 일은 똑같음
    def __str__(self):
        return f"변수1: {self.변수1}, 변수2: {self.변수2}"

    #toString() -> 레퍼런스(개발단계, 디버깅)
    def __repr__(self):
        return f"변수1: {self.변수1}, 변수2: {self.변수2}"

    # 객체 비교 -> 파이썬은 메서드명이 정해져있음, 필요한 게 있으면 골라서 쓰면 됨
    def __eq__(self, other):
        return self.변수1 == other.변수1 and self.변수2 == other.변수2

    def __add__(self, other):
        return 클래스(self.변수1 + other.변수1, self.변수2 + other.변수2)

    def __sub__(self, other):
        return 클래스(self.변수1 - other.변수1, self.변수2 - other.변수2)

    def __contains__(self, item):
        return item in (self.변수1, self.변수2) # 튜폴에 객체를 넣기

c1 = 클래스(10, 20)
c2 = 클래스(10,20)
print(c1) # <__main__.클래스 object at 0x0000018678B6B190> -> __str__ : 변수1: 10, 변수2: 20
print(c1.__eq__(c2)) # True
c3 = c1.__add__(c2)
print(c3) # 변수1: 20, 변수2: 40
c4 = c1.__sub__(c2)
print(c4) # 변수1: 0, 변수2: 0
print(c3.__contains__(10)) # False
print(c3.__contains__(20)) # True
print(c3.__contains__(30)) # False
print(c3.__contains__(40)) # True