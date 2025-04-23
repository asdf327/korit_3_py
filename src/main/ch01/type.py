number = 10
name = "김미진"
isOpen1 = True
isOpen2 = False
print(number)
print(name) # 언어는 두 개가 있는데 전체 번역과 한줄 번역 중에 파이썬은 한줄 번역

print(name.index("미")) #1
# print(name.index("준")) 오류
print(name.find("미")) #1
print(name.find("준")) # -1

# print(name.index("미", 2))

print("이름 : {0}, 숫자 : {1}, 열림 : {2} ".format(name, number, isOpen1))
print("이름 : {name}, 숫자 : {number}, 열림 : {isOpen1} ".format(name = name, number = number, isOpen1 = isOpen1))
print(f"이름 : {name}, 숫자 : {number}, 열림 : {isOpen1}")

address = """부산
동래구
중앙대로"""

print(address)
# number = 12 # 초기화
