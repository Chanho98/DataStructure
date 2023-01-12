class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data    # 노드가 저장하는 데이터
        self.next = None    # 다음 노드에 대한 레퍼런스스


class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_after(self, previous_node, data):
        """링크드 리스트 주어진 노드 뒤 삽입 연산 메소드"""
        new_node = Node(data)

        # tail 노드 다음에 노드를 삽입할 때
        if previous_node is self.tail:
            self.tail = new_node
            previous_node.next = new_node
        else:   # 꼬리 뒤에 삽입 하지 않는 경우
            previous_node.next, new_node.next = new_node, previous_node.next

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head
        finding_node = Node(data)

        while iterator is not None:
            if iterator.data == finding_node.data:
                return iterator
            # 찾지 못했다면 다음 노드로 넘어간다.
            iterator = iterator.next

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        if self.head is None:   # 링크드 리스트가 비어있는 경우
            self.head = new_node
            self.tail = new_node
        else:   # 링크드 리스트가 비어있지 않은 경우
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"
        iterator = self.head

        while iterator is not None:
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next

        return res_str



# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

print(my_list)   # 전체 링크드 리스트 출력

node_2 = my_list.find_node_at(2)   # 인덱스 2에 있는 노드에 접근
my_list.insert_after(node_2, 6)

print(my_list)