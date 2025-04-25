# import module01_2
# import module01_3
from src.main.ch06 import name, add, Student

# print("모듈 4번 파일 실행")
"""
모듈 1번 파일 실행
김준일
30
name : 김준일, age : 30
김준일
50
name : 김준이, age : 33
모듈 4번 파일 실행

파이썬은 한 줄씩 실행되는 코드이기 때문에 인폴트를 하는 순간 저 파일들이 한 번에 실행된다 

import module01_2 실행 -> module01_2 파일 실행 -> module01_1 파일 실행
"""
print("모듈 4번 파일 실행")
if __name__ == "__main__": # 파이썬의 메인 함수
    pass
"""
모듈 1번 파일 실행
module01_1 # module01_1의 print(__name__)
ch06 패키지
모듈 4번 파일 실행
__main__ # 실행된 파일이 __main__으로 뜬다 
"""
"""
module01_1에 메인 함수가 생겨 재생했을 경우 이렇게 출력됨 -> 파일마다 메인 함수를 만들어 전체 실행이 아닌 그 파일만 실행할 수 있음
ch06 패키지
모듈 4번 파일 실행
"""
