# 세트는 중복데이터 저장이 불가하다.

finished_classes = set()

# 데이터 저장
finished_classes.add("자료 구조")
finished_classes.add("알고리즘")
finished_classes.add("프로그래밍 기초")
finished_classes.add("인터렉티브 웹")
finished_classes.add("데이터 사이언스")

print(finished_classes)  # 세트 출력


# 중복 데이터 저장 시도
finished_classes.add("자료 구조")
finished_classes.add("알고리즘")

print(finished_classes)

# 데이터 탐색
print("컴퓨터 개론" in finished_classes)

# 데이터 삭제
finished_classes.remove("자료 구조")

print(finished_classes)