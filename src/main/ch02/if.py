# 논리 연산 -> 이프를 잘하려면 논리 연산을 잘해야 한다
date1 = 10
date2 = 2

r1 = date1 == date2
r2 = date1 != date2
print(r1, r2) #False True

# r3 = r1 && r2 #자바의 논리연산자
r3 = r1 and r2
r4 = r1 or r2
print(r3, r4) #False True
# print(!r3) #자바의 논리연산자
print(not r3) #True
print(not (r3 and r4)) #True, and -> not
print(not r3 and r4) #위와 다르다. not -> and

# 멤버 연산자  (in, not in) -> in 포함되는가
print("a" in "apple") #True, a가 apple에 포함되는가
print("b" in "apple") #False
print("a" in ["a", "b", "c"]) #True, 리스트에 포함되는가?도 가능
print("b" in ["a", "b", "c"]) #True
print("c" in ("a", "b", "c")) #True, 튜폴도 가능
print("ㅇ" in {"a", "b", "c"}) #False, set도 가능
print("name" in {"name" : "김준일", "age" : 32} ) #True, 딕셔너리도 가능
print("address" in {"name" : "김준일", "age" : 32} ) #False
print("김준일" in {"name" : "김준일", "age" : 32}.values()) #True, .values()로 값을 검증

# 식별 연산자 (is, is not) -> 이다, 아니다
print([1,2,3,4] is [1,2,3,4]) #False, 객체의 주소값 비교 즉, 동일 객체인가를 봄
print([1,2,3,4] == [1,2,3,4]) #True, 값비교
print(10 == 10) #True
# print(10 is 10) #True -> 리터널이니 주소도 같다

# 조건문
if date1 == date2 :
    print(f"date1: {date1}이 date2: {date2} 같다 ")
else:
    print(f"date1: {date1}이 date2: {date2} 다르다 ")
# date1: 10이 date2: 2 다르다

# 다중 조건문
if date1 == 2:
    print("date1은 2입니다")
elif date2 == 2:
    print("date2은 2입니다")
else:
    print("둘다 아닙니다")
# date2은 2입니다