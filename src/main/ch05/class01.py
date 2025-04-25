# 파이썬 클래스 정의
class Student:
    # 파이썬은 클래스 메서드와 스태틱 메서드를 구분
    #멤버(클래스) 변수 -> 자바에서의 static 변수
    name = "김준일(클래스 변수)"
    age = "32(클래스 변수)"

    def __init__(self): # 파이썬의 생성자
        # 인스턴스 변수
        self.name = "김준일"
        self.age = 32
        # -> 멤버 변수 초기화. 이곳에 써야 클래스 변수가 아닌 인스턴스 변수가 된다.

    def toString(self): #파이썬에서는 클래스 안의 함수는 반드시 self 매개변수를 넣는다. cls 쓰지 않음. -> 클래스 변수를 가져와야 함(self.__class__.name)
        return f"Student(name: {self.name}, age: {self.age}, clsName: {self.__class__.name})" # 멤버 변수를 그대로 넣으면 오류가 뜨기에 self.을 넣어야 한다
        # 멤버 변수는 값이 초기화되지 않은 변수가 있다면 클래스 변수를 가져와 쓸 수 있다.

    @classmethod
    def toString2(cls): # self가 아닌 cls를 씀. self를 쓸 수 없음.
        return f"Student(name: {cls.name}, age: {cls.age})"

    @staticmethod
    def toString3(name, age): # 클래스 변수에 접근할 수 없다
        return f"Student(name: {name}, age: {age})"

# print(Student()) # <__main__.Student object at 0x000001EEFD96F1F0
# print(Student().name) # 김준일
# print(Student().age) # 32
#
# s1 = Student() # 변수가 없으면 재사용이 불가능하기에 클래스를 변수에 할당
#
# print(s1.name) #김준일
# print(s1.age) # 32
# print(s1.toString()) #Student(name: 김준일, age: 32)
# Student.name = "김준이" # 김준이로 바뀜
# s1.name = "김준삼" # 바뀌지 않음
# print(Student.toString2()) # Student(name: 김준이, age: 32)

print(Student.name) # 김준일(클래스 변수)
print(Student.age) # 32(클래스 변수)
s1 = Student()
print(s1.name) # 김준일
print(s1.age) # 32
print(s1.toString()) # Student(name: 김준일, age: 32, clsName: 김준일(클래스 변수))