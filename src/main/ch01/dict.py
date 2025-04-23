# 딕셔너리 선언 및 초기화
studentDiot = dict()
studentDiot = {
    "name" : "심민호",
    "age" : 25
}
print(studentDiot) #{'name': '심민호', 'age': 25}

# 딕셔너리 값 추가
studentDiot["address"] = "부산"
print(studentDiot) #{'name': '심민호', 'age': 25, 'address': '부산'}

# 딕셔너리와 리스트의 값 추가 차이
"""
anyList = [] -> 빈 리스크 
anyList[0] = "test" -> 빈 리스크는 0번 인덱스가 없음므로
print(anyList) -> 오류 
딕셔너리는 빈 딕셔너리로도 값을 넣을 수 있지만 리스트는 빈 리스트에 값을 넣을 수 없다! 
"""
anyList = []
anyList.append("test")
print(anyList)

# 딕셔너리 값 조회
name = studentDiot.get("name")
print(name)
# print(studentDiot.name) #자바의 방법
print(studentDiot["name"]) # 파이썬의 방법
name = studentDiot["name"] #.get을 안 써도 print(studentDiot["name"])과 동일하게 조회할 수 있음
print(name)
address = studentDiot["address"]
print(address)

# 딕셔너리 값 수정
studentDiot["address"] = "서울"
print(studentDiot) #{'name': '심민호', 'age': 25, 'address': '서울'}

# 딕셔너리 삭제
del studentDiot["age"]
print(studentDiot) # {'name': '심민호', 'address': '서울'}
studentDiot.pop("name")
print(studentDiot) # {'address': '서울'}

# 딕셔너리 키, 값  한쌍 -> 아이템이라 부름
print(type(studentDiot.items())) # dict_items
studentDiot["name"] = "김미진"
print(list(studentDiot.items())) # [('address', '서울'), ('name', '김미진')]
print(studentDiot.items())  # dict_items([('address', '서울'), ('name', '김미진')])
# -> dict_items면 함수나 여러 가지 기능을 쓰지 못함. 그래서 리스트나 튜폴로 형변환 필수
print(list(studentDiot.items())[0])
key, value = list(studentDiot.items())[0] # studentDiot의 0번 인덱스의 키와 값을 key, value에 넣기
print(f"key : {key}, value : {value}") # key : address, value : 서울

# 딕셔너리 키들만 모두 뽑아 보고 싶을 때
print(studentDiot.keys()) #dict_keys(['address', 'name'])
print(list(studentDiot.keys())) #['address', 'name'] ! 리스트 형변환 필수

# 딕셔너리 값들만 모두 뽑아 보고 싶을 때
print(studentDiot.values())
print(list(studentDiot.values())) # ['서울', '김미진']

searshKey = "code"

students = [
    {
        "code" : 1,
        "name" : "심인호"
    },
    {
        "code" : 2,
        "name" : "윤현지"
    },
    {
        "code" : 3,
        "name" : "이동규"
    },
]

result = []

i = 0

while i < len(students):
    student = students[i]
    result.append(student[searshKey])
    i += 1

print(result)

result = {
    "code" : [1,2,3],
    "name" : ['심민호', '윤현지', '이동규']
}

i = 0
while i < len(students):
    student = students[i]
    keys = list(student.keys())
    j = 0
    while j < len(keys):
        key = keys[j]
        j += 1
        if key in result :
            result[key].append(student[key])
            continue
        result[key] = [student[key]]
    i += 1

print(result)