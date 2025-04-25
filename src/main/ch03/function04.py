# 람다함수
"""
JAVA
@functionalInerface
public interfaca Addition{
    int add(int n, int b);
}
public class Test {
    public static void main(String[] arge) {
        Addition a = (n, n2) -> n + n2;
        int result = a.add(10,20);
        System.out.println(result)
    }
}
"""

# 파이썬 람다 함수
# lambda 매개 변수 : 표현식
def add(num1, num2):
    return num1 + num2
print(add(10,20))
add = lambda num1, num2 : num1 + num2
print(add(10, 20))

numbers = (1,5,23,2,6,4)
print(sorted(numbers)) # [1, 2, 4, 5, 6, 23] -> sorted : 정렬하여 새로운 리스트를 반환.
print(numbers) # (1, 5, 23, 2, 6, 4), 원본 리스트는 유지.

students = [("김준일", 90), ("김이준", 85), ("김준삼", 95)] # 리스트[]를 생성, 리스트릐 각 요소는 튜플()
sorted_students = sorted(students, key = lambda student : student[1])
print(sorted_students) # [('김이준', 85), ('김준일', 90), ('김준삼', 95)]

numbers2 = map(lambda num : num * 2, numbers)
print(numbers2) # <map object at 0x000001B59988DFA0>
numbers2 = list(map(lambda num : num * 2,numbers)) # 리스트로 형변환
print(numbers2) # [2, 10, 46, 4, 12, 8]

print(numbers)
numbers3 = list(filter(lambda num : num % 2 == 0, numbers)) # 람다 함수로 짝수만 출력
print(numbers3) # [2, 6, 4]
numbers4 = list(map(lambda num : f"<h1>{num}</h1>", numbers3))
print(numbers4) # ['<h1>2</h1>', '<h1>6</h1>', '<h1>4</h1>']