# 사용자 지정 해시 함수
def hash_function_remainder(key, array_size):
    """해시 테이블의 key를 나누기 방법으로 0 ~ array_size - 1 범위의 자연수로 바꿔주는 함수"""
    return key % array_size


print(hash_function_remainder(40, 200))
print(hash_function_remainder(120, 200))
print(hash_function_remainder(788, 200))
print(hash_function_remainder(2307, 200))


def hash_function_multiplication(key, array_size, a):
    """해시 테이블의 key를 곱셈 방법으로 0 ~ array_size - 1 범위의 자연수로 바꿔주는 함수"""
    temp = a * key  # a와 key를 곱한다
    temp = temp - int(temp)  # a와 key를 곱한 값의 소숫점 오른쪽 부분만 저장한다

    return int(array_size * temp)  # temp와 배열 크기를 곱한 수의 자연수 부분만 리턴한다


print(hash_function_multiplication(40, 200, 0.61426212))
print(hash_function_multiplication(120, 200, 0.61426212))
print(hash_function_multiplication(788, 200, 0.61426212))
print(hash_function_multiplication(2307, 200, 0.61426212))


# 파이썬 내장 hash 함수 아무수나 return 해준다.
# hash 함수에 서로 다른 두 값을 파라미터로 넣었을 때 같은 정수가 리턴될 수 없다
# 정수 값
print(hash(12345))  # 12345
print(hash(12345))  # 12345

# 다른 정수 값
print(hash(12346))  # 12346
# 소수 값
print(hash(15.1234))  # 284541027336970255
print(hash(15.1234))  # 284541027336970255

# 다른 소수 값
print(hash(81.1234))  # 284541027336978513
# 문자열
print(hash("파이썬"))  # -8002119629611903017
print(hash("파이썬"))  # -8002119629611903017

# 다른 문자열
print(hash("자바"))  # -8553573703343279427

