# a = int(input("a입력: "))
# b = input("b입력: ")

# print(a, b) # 자바의 Scanner 클래스와 같음
# print(type(a)) # <class 'int'>
# print(type(b)) # <class 'str'>

# number = input("두 수의 입력").split()
# print(number) # 10 20 입력 -> ['10', '20']

# number1, number2 = map(lambda n : int(n), input("두 수의 입력 : ").split())
def parseInt(n) :
    return int(n)

number1, number2 = map(parseInt, input("두 수의 입력 : ").split())
# number1, number2 = list(map(int, input("두 수의 입력 : ").split()))
# print(type(number1)) # <class 'int'>
# print(number2)