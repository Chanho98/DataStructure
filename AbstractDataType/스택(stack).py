# LIFO : Last_in_first_out
# 맨뒤 데이터 추가, 삭제, 접근
from collections import deque

# 리스트로 만들어 주어도 된다.
stack = deque()

# 스택 맨 끝에 데이터 추가
stack.append("T")
stack.append("a")
stack.append("e")
stack.append("h")
stack.append("o")

print(stack)

# 맨 끝 데이터 접근
print(stack[-1])

# 맨 끝 데이터 접근
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)