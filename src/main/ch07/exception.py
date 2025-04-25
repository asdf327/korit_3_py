if __name__ == '__main__':
    print("예외처리") # 예외처리

    numbers = [1,2,3,4,5]
    try:
        print(numbers[5])
    except IndexError as e:
        print(e) # list index out of range
        print("범위 초과") #범위 초과

    try:
        print("예외 강제 방생") # 예외 강제 방생
        raise TypeError("지료형 맞춰라")
    except TypeError as e:
        print(e) # 지료형 맞춰라