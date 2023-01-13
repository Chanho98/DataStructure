# DataStructure
파이썬 언어를 이용하여 자료 구조를 학습하고 구현함

## 1.1. Graph
<p align="center"><img src="https://user-images.githubusercontent.com/78125194/212007122-7d7e3998-7aaa-4eb1-960a-104e2d027a1d.png" width="300" height="200"/></p>
정점(Node)과 간선(Edge)로 이루어진 자료구조로 조직도와 비슷하다. 그래프는 연결된 노드 사이에 우열이 업스며, 방향성이 존재할 수도 존재하지 않을 수도 있다. 또한 서클을 만드는 경우도 있지만 만들지 않는 경우도 있다.

## 1.2. 파이썬의 Class 객체를 이용하여 Graph 노드 구현
```
class StationNode:
    """간단한 지하철 역 노드 클래스"""

    def __init__(self, station_name):
        self.station_name = station_name


def create_station_nodes(input_file):
    """input_file에서 데이터를 읽어 와서 지하철 그래프 노드들을 리턴하는 함수"""
    stations = {}  # 지하철 역 노드들을 담을 딕셔너리

    # 파라미터로 받은 input_file 파일을 연다
    with open(input_file) as stations_raw_file:
        for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
            subway_line = line.strip().split("-")  # 앞 뒤 띄어쓰기를 없애고 "-"를 기준점으로 데이터를 나눈다

            for name in subway_line:
                station_name = name.strip()  # 앞 뒤 띄어쓰기 없애기

                # 지하철 역 이름이 이미 저장한 key 인지 확인
                if station_name not in stations:
                    current_station = StationNode(station_name)  # 새로운 인스턴스를 생성하고
                    stations[station_name] = current_station  # dictionary에 역 이름은 key로, 역 노드 인스턴스를 value로 저장한다

    return stations


stations = create_station_nodes(r"C:\Users\CKIRUser\stations.txt")  # stations.txt 파일로 그래프 노드들을 만든다

# stations에 저장한 역들 이름 출력 (체점을 위해 역 이름 순서대로 출력)
for station in sorted(stations.keys()):
    print(stations[station].station_name)
```

## 2.1. Linked List
<p align="center"><img src="https://user-images.githubusercontent.com/78125194/212218778-da04380b-dd19-48ba-a4ac-068293608d52.png" width="300" height="200"/></p>
링크드 리스트는 노드와 노드를 연결시킨 자료 구조로 데이터를 갖고 있는 데이터의 묶음이다.
링크드 리스트는 데이터를 저장하는 부분과 처음과 끝을 가르키는 포인터를 가지고 있다.  

## 2.2. 파이썬의 Class 객체를 이용하여 Double Linked List 구현
```
class Node:
    """더블리 링크드 리스트 노드"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    """더블리 링크드 리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None
```

## 2.3. 링크드 리스트에서 삭제, 추가, 삽입, 탐색 메소드 구현
```
    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드, 동시에 삭제하는 노드의 데이터를 리턴한다."""
        data = node_to_delete.data

        if self.head is self.tail:  # 빈 리스트가 되는 경우
            self.head = None
            self.tail = None
        elif self.head is node_to_delete:  # 리스트의 헤드를 지워주는 경우
            self.head = self.head.next
            self.head.prev = None
        elif self.tail is node_to_delete:  # 리스트의 테일을 지워주는 경우
            self.tail = self.tail.prev
            self.tail.next = None
        else:   # 중간에 인덱스를 삭제하려는 경우
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return data


    def prepend(self, data):
        """링크드 리스트 가장 앞에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data)

        # 비어있는 리스트의 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:  # 리스트가 비어있지 않은 경우
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, previous_node, data):
        """링크드 리스트 삽입 연산 메소드 - 순서를 반드시 지켜야 한다."""
        new_node = Node(data)   # 새로운 노드 생성
        if self.tail is previous_node:  # tail에 삽입하는 경우
            self.tail.next = new_node   # 새로운 노드를 tail 노드의 다음 노드로 지정한다
            new_node.prev = self.tail   # tail 노드를 새로운 노드의 전 노드로 지정한다
            self.tail = new_node        # 새로운 노드를 tail 노드로 지정한다
        else:   # 중간에 삽입하는 경우
            # 새롭게 생성한 노드를 이미 있는 링크드 리스트에 연결시키고
            new_node.prev = previous_node
            new_node.next = previous_node.next

            # 이미 있는 노드들의 앞과 다음 레퍼런스를 새롭게 생성한 노드로 지정한다
            previous_node.next.prev = new_node
            previous_node.next = new_node

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        # 링크드 리스트가 비어 있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:  # 링크드 리스트가 비어 있지 않은 경우
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정한다"""
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수

        # index 번째 있는 노드로 간다
        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수

        while iterator is not None:
            if iterator.data == data:
                return iterator

            iterator = iterator.next

        return None

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str
```

## 3.1. Tree
<p align="center"><img src="https://user-images.githubusercontent.com/78125194/212224664-11f6be02-8cbc-4521-86c8-7ce28768b4e9.png" width="300" height="200"/></p>
트리는 노드로 구성된 자료 구조이다. 트리는 하나의 루트 노드를 갖으면 0개 이상의 자식 노드를 갖는다. 이러한 구조가 반복되며 Cycle이 존재할 수 없다는 특징을 갖는다.

## 3.2. 이진 탐색 트리 탐색 구현
```
class Node:
    """이진 탐색 트리 노드 클래스"""

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right_child = None
        self.left_child = None


def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class BinarySearchTree:
    """이진 탐색 트리 클래스"""

    def __init__(self):
        self.root = None

    def search(self, data):
        """이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다"""
        temp = self.root  # 탐색용 변수, root 노드로 초기화

        # 원하는 데이터를 갖는 노드를 찾을 때까지 돈다
        while temp is not None:
            # 원하는 데이터를 갖는 노드를 찾으면 리턴
            if data == temp.data:
                return temp
            # 원하는 데이터가 노드의 데이터보다 크면 오른쪽 자식 노드로 간다
            if data > temp.data:
                temp = temp.right_child
            # 원하는 데이터가 노드의 데이터보다 작으면 왼쪽 자식 노드로 간다
            else:
                temp = temp.left_child

        return None  # 원하는 데이터가 트리에 없으면 None 리턴

    def insert(self, data):
        """이진 탐색 트리 삽입 메소드"""
        new_node = Node(data)  # 삽입할 데이터를 갖는 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return

        # 코드를 쓰세요
        temp = self.root  # 저장하려는 위치를 찾기 위해 사용할 변수. root 노드로 초기화한다

        # 원하는 위치를 찾아간다
        while temp is not None:
            if data > temp.data:  # 삽입하려는 데이터가 현재 노드 데이터보다 크다면
                # 오른쪽 자식이 없으면 새로운 노드를 현재 노드 오른쪽 자식으로 만듦
                if temp.right_child is None:
                    new_node.parent = temp
                    temp.right_child = new_node
                    return
                # 오른쪽 자식이 있으면 오른쪽 자식으로 간다
                else:
                    temp = temp.right_child
            else:  # 삽입하려는 데이터가 현재 노드 데이터보다 작다면
                # 왼쪽 자식이 없으면 새로운 노드를 현재 노드 왼쪽 자식으로 만듦
                if temp.left_child is None:
                    new_node.parent = temp
                    temp.left_child = new_node
                    return
                # 왼쪽 자식이 있다면 왼쪽 자식으로 간다
                else:
                    temp = temp.left_child

    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)  # root 노드를 in-order로 출력한다


# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

# 노드 탐색과 출력
print(bst.search(7).data)
print(bst.search(19).data)
print(bst.search(2).data)
print(bst.search(20))
```
## 4.1. Hash Table
<p align="center"><img src="https://user-images.githubusercontent.com/78125194/212225808-20ad2f43-bed5-4718-be2c-ca387619de53.png" width="300" height="200"/></p>
해시 테이블은 (KEY, VALUE)로 데이터를 저장하는 자료구조 중 하나로 데이터를 검색할 수 있는 자료구조이다. 빠른 검색 속도를 제공하며, 평균 시간 복잡도는 1이다.

## 4.2. Hash Table 구현
```
from HDLL import LinkedList


class HashTable:
    def __init__(self, capacity):
        self._capacity = capacity  # 파이썬 리스트 수용 크기 저장
        self._table = [LinkedList() for _ in range(self._capacity)]  # 파이썬 리스트 인덱스에 반 링크드 리스트 저장

    def _hash_function(self, key):
        """
        주어진 key에 나누기 방법을 사용해서 해시된 값을 리턴하는 메소드
        주의: key는 파이썬 불변 타입이여야 한다.
        """
        return hash(key) % self._capacity

    def _get_linked_list_for_key(self, key):
        """주어진 key에 대응하는 인덱스에 저장된 링크드 리스트를 리턴하는 메소드"""
        hashed_index = self._hash_function(key)

        return self._table[hashed_index]

    def _look_up_node(self, key):
        """파라미터로 받은 key를 갖고 있는 노드를 리턴하는 메소드"""
        linked_list = self._get_linked_list_for_key(key)
        return linked_list.find_node_with_key(key)

    def look_up_value(self, key):
        """
        주어진 key에 해당하는 데이터를 리턴하는 메소드
        """
        return self._look_up_node(key).value

    def insert(self, key, value):
        """
        새로운 key - 데이터 쌍을 삽입시켜주는 메소드
        이미 해당 key에 저장된 데이터가 있으면 해당 key에 대응하는 데이터를 바꿔준다
        """
        existing_node = self._look_up_node(key)  # 이미 저장된 key인지 확인한다

        if existing_node is not None:
            existing_node.value = value  # 이미 저장된 key면 데이터만 바꿔주고
        else:
            # 없는 키면 새롭게 삽입시켜준다
            linked_list = self._get_linked_list_for_key(key)
            linked_list.append(key, value)

    def __str__(self):
        """해시 테이블 문자열 메소드"""
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]


test_scores = HashTable(50)  # 시험 점수를 담을 해시 테이블 인스턴스 생성

# 여러 학생들 이름과 시험 점수 삽입
test_scores.insert("현승", 85)
test_scores.insert("영훈", 90)
test_scores.insert("동욱", 87)
test_scores.insert("지웅", 99)
test_scores.insert("신의", 88)
test_scores.insert("규식", 97)
test_scores.insert("태호", 90)

print(test_scores)

# key인 이름으로 특정 학생 시험 점수 검색
print(test_scores.look_up_value("현승"))
print(test_scores.look_up_value("태호"))
print(test_scores.look_up_value("영훈"))

# 학생들 시험 점수 수정
test_scores.insert("현승", 10)
test_scores.insert("태호", 20)
test_scores.insert("영훈", 30)

print(test_scores)
```
