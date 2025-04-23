numbers = [1,2,3,4,5]

print(numbers[0])
print(numbers[0:3]) # [1(0), 2(1), 3(2), 4(3), 5(4)], 끝부분은 +1해야 함
print(numbers[:3]) #시작 지점 생략 가능
print(numbers[3:]) #끝 지점 생략 가능
print(numbers[-3:]) #결과 값 : [3, 4, 5] | [1(-5),2(-4),3(-3),4(-2),5(-1)]
print(numbers[:-2]) #결과 값 : [1, 2, 3]
print("부산 동래구"[3:]) #결과 값 : 동래구, 즉 문자열도 가능
print((1,2,3,4) [2:]) #튜폴도 가능. 단, 튜폴로 표시됨
# print({1,2,3,4}[2:]) # 오류

anyList = [[1, "김미진", [3,4, [7, "김일남"], 6]]]

print(anyList[0][1]) #김미진
print(anyList[0][2][2][1]) #김일남
print(anyList[0][2][1:3]) #[4, [7, '김일남']]

print("------------연산자--------------")
"""
 +, -, *, **(제곱), /, //(몫), % 
"""

print(3//2) #나눗셈 소수점 제거
print(3**2) #제곱
print("*", "\n", "*" * 2, "\n", "*" * 3, sep="")

i = 0
while(i < 5) :
    print("*" * (i + 1))
    i += 1

i = 0
while(i < 5) :
    print("*" * (5 - i))
    i += 1

print([1,2,3] + [4,5,6]) #[1, 2, 3, 4, 5, 6]
print([1,2,3] * 3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]
# print([1,2,3] - [2,3]) #오류

print(len([1,2,3])) # 3, len = 리스트의 길이

anyList = [1,2,3,4]
i = 0
while i < len(anyList):
    print(anyList[i])
    i += 1

# print(3 + "hi") # 오류, 숫자 + 자료형은 X
print(str(3) + "hi") # 숫자를 자료형으로 바꾸는 str 사용 필요
print(int("1") + 2) # 자료형을 숫자로 바꾸는 int을 쓰면 결과 값이 3으로 나옴
print(bool("True")) # 자료형을 참 거짓으로 바꿈

del anyList[2] # del 키워드로 삭제를 할 때 값이 꼭 존재해야 함
print(anyList)

try:
    anyList.pop(10) # 공백이면 맨 끝에 값을 지움
    print(anyList)
except Exception as e:
    print("해당 리스트의 범위를 초과하였습니다") # 이렇게 쓰기 위해 del 보다 pop 쓰는 게 좋음
# anyList.remove(10)

anyList = [1,5,2,3,9]
# anyList.sort()
# print(anyList) # [1, 2, 3, 5, 9]
# copyAnyList = anyList.copy() # 원본 데이터는 어떻게 쓰일지 모르니 유지 해야 하기에 새로운 변수를 만듬
copyAnyList = anyList[:] # [:] 처음 부터 끝까지
copyAnyList.sort()
print(copyAnyList)

print([1,2,3,4,5] == [1,2,3,4,5]) #True
print([1,2,3,4,5] == [1,3,2,4,5]) #False
anyList = [1,2,3,4,5]
anyList2 = [1,2,3,4,5]
print(anyList == anyList2) #True
print(id(anyList) == id(anyList2)) #False
print(id(anyList), id(anyList2)) #결과 값 : 2257846781888 2257846781824
# 즉 값이 같더라도 주소 값이 다르다. anyList과 anyList2는 다른 배열이니까

anyList = [1,2,3]
anyList2 = [4,5]
print(id(anyList)) # 2480486725824
anyList = anyList + anyList2
print(id(anyList)) # 2480486725568, anyList2로 덮어씌운 것이기에 주소가 같다
anyList.extend([6,7])
print(id(anyList)) #2764948944768, 값만 추가한 것이기에 주소가 같다
