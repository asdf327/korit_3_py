# 교집합
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

print(set1 & set2) # {3, 4, 5}

text1 = "mt name is junil"
text2 = "mt name is junlee"
testList1 = text1.split(" ") # 공백
print(testList1) #['mt', 'name', 'is', 'junil']
testList2 = text2.split(" ")
testList1 = set (testList1)
testList2 = set (testList2)
print(testList1) # {'mt', 'name', 'junil', 'is'}
print(testList1 & testList2) # {'mt', 'name', 'is'} 서로 같은 글자
print((testList1 | testList2) - (testList1 & testList2)) #{'junil', 'junlee'} 서로 다른 글자