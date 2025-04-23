anyTuple = (1,2,3,4)
print(anyTuple[2:])
newList = list(anyTuple) # 형변환을 하면 다양한 함수를 쓸 수 있다

newTuple = anyTuple + (5,6,7,8)
print(newTuple) # 튜플 + 튜플 가능, 주소 값을 확장하지만 anyTuple 확장하는 게 아님

"""
오류 
a, b, c = newList
d, e, f = newTuple
"""

a, b, *c = newList # (1,2,3,4)
d, e, *f = newTuple # (1,2,3,4,5,6,7,8)
print(a, b, c, d, e, f) # 1 2 [3, 4] 1 2 [3, 4, 5, 6, 7, 8]
# 변수 앞에 *을 붙이면 리스트의 형식으로 가져 온다
newTuple = 1,2,3,4,5
print(newTuple) # (1, 2, 3, 4, 5)

