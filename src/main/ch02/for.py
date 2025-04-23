# 범위 생성 함수 range()
from src.main.ch01.dict import student

r = range(10)
print(r) #range(0, 10)
rList = list(r)
print(rList) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
r2 = range(5, 10)
print(r2) #range(5, 10)
print(list(r2)) #[5, 6, 7, 8, 9], 파이썬에서는 리스트를 잘 써야 한다
r3 = range(0, 10, 2)
print(r3) #range(0, 10, 2)
print(list(r3)) #[0, 2, 4, 6, 8]

for num in range(10): # 0부터 하나씩 num에 대입
    print(num) # 0 1 2 3 4 5 6 7 8 9

for num in [1,2,3,4]: # 리스트도 순회 가능
    print(num) # 1 2 3 4

studentDict = {
    "name" : "김준일",
    "age" : 32,
    "address": "부산 동래구"
}

studentItems = studentDict.items()
print(studentItems) #dict_items([('name', '김준일'), ('age', 32), ('address', '부산 동래구')])
for item in studentItems:
    print(item)
"""
('name', '김준일')
('age', 32)
('address', '부산 동래구')
"""

for key, valus in studentItems:
    print(key, valus)
"""
name 김준일
age 32
address 부산 동래구
"""

for i in range(2, 10) :
    for j in range (1, 10) :
        print(f"{i} * {j} = {i*j}", end="\t")
        # print(f"{i} * {j} = {i * j}", end="\n" if j == 9 else "\t")
    print()

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} + {j} = {i+j}", end="\t")
    print()