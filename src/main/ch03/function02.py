# 여러 값 리턴
def fx1():
    return "함수1", "함수2", "함수3"

r1, r2, r3 = fx1()
print(r1, r2, r3) # 함수1 함수2 함수3,
# (함수1, 함수2, 함수3)라는 튜폴 -> r1(함수1), r2(함수2), r3(함수3) 할당

r4, r5, r6 = "함수4", "함수5", "함수6"
print(r4, r5, r6) # 함수4 함수5 함수6
# "함수4", "함수5", "함수6"가 하나의 튜폴이 되어, 그 값이 각 변수에 할당 됨

r7 = "함수7", "함수8"
print(r7) # ('함수7', '함수8') -> r7에 ('함수7', '함수8') 튜폴을 할당
# 이렇게 할 수 있는 이유는 여러 값이 아닌 튜폴 하나로 묶기 때문이다.

# 기본값 매개변수
def fx2(name, membershipType = "일반회원"): # 매개변수에 디톨트 값을 줄 수 있음.
    # def fx2(membershipType = "일반회원", name): # 오류. 디폴트 값을 넣으려면 빈 매개변수 뒤에 넣어야 함.
    return {
        "회원종류" : membershipType,
        "이름" : name
    }
member1 = fx2("김준일")
print(member1) #{'회원종류': '일반회원', '이름': '김준일'}
member2 = fx2("김준이", "골드회원")
print(member2) #{'회원종류': '골드회원', '이름': '김준이'}
member3 = fx2("김준삼")

# 키워드 매개변수(인수) -> 어떤 매개변수에 값을 전달할지 명시
def fx3(name, membershipType):
    return {
        "회원종류" : membershipType,
        "이름" : name
    }

member4 = fx3("김준사", "VIP")
member5 = fx3(membershipType = "VIP", name = "김준사") # 매개변수를 지정하기에 순서가 상관없다.
# 키워드를 쓸 거면 하나만 쓰는 게 아니라 매개변수 전부를 써야 한다 -> 왜? 순서가 섞여서
# 값이 미리 디폴트 된 상태라면 쓰지 않아도 된다

# 가변 인자 *변수명(args), **변수명(kwargs)
def fx4(*args):
    print(args)

fx4(1,2,3,4,5,6,7) #(1, 2, 3, 4, 5, 6, 7)

def fx5(*aa, bb):
    print(f"aa: {aa}")
    print(f"bb: {bb}")

# fx5(1,2,3,4,5,6,7) #오류, 키워드 지정 오류 *에 7까지 다 들어가기에 bb를 따로 지정해 값을 넣어야 한다.
fx5(1,2,3,4,5,6,7,bb=8)

# def fx6(**cc, address): #오류
def fx6(address,**cc): #cc가 앞에 있다면 address까지 딕셔너리로 묶인다.
    print(f"cc : {cc}")
    print(f"address : {address}")

# fx6(10) # 오류
# fx6({"name" : "김준일", "age" : 32}) # 오류
fx6(address = "부산", name="김준일", age=32) #지정한 게 없지만 자동으로 딕셔너리로 변환 cc 매개변수를 쓰는 게 아님

"""
매개변수 순서 요약
1. 일반 인자 
2. 기본값(디폴트)이 있는 인자 
3. *arge
4. 키워드 전용 인자, fx6(address = "부산") <- 이런걸 말함
5. **kwargs
"""

def fx(a, b=0, *arge, **kwargs):
    print(f"a : {a}")
    print(f"b : {b}")
    print(f"arge : {arge}")
    print(f"kwargs : {kwargs}")

fx(10,20, 30, 40, 50, name = "김준일", age=32)
"""
a : 10 = 일반 인자 
b : 20 = 기본값(디폴트)이 있는 인자 
arge : (30, 40, 50) = *arge
kwargs : {'name': '김준일', 'age': 32} = **kwargs
"""