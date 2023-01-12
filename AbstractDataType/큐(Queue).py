# FIFO : First_in_First_out
# 데이터 추가, 삭제, 접근 연산
# 순서대로 등록된걸 처리하는 추상화 연산
from collections import deque

queue = deque()

# 큐의 맨 끝에 데이터 삽입
queue.append("태호")
queue.append("현승")
queue.append("지웅")
queue.append("동욱")
queue.append("신의")

print(queue)

# 큐의 가장 앞 데이터에 접근
print(queue[0])

# 큐 맨 앞 데이터 삭제, 추가적으로 삭제된 데이터를 리턴
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print(queue)