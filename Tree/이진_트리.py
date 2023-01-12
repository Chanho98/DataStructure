class Node:
    """이진 트리 노드 클래스"""
    def __init__(self, data):
            self.data = data
            self.left_child = None
            self.right_child = None

# root 노드 생성
root_node = Node("A")

# 다른 노드들 생성
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")

# 노드들을 연결
root_node.left_child = node_B
root_node.right_child = node_C

node_B.left_child = node_D
node_B.right_child = node_E

node_E.left_child = node_G
node_E.right_child = node_H

node_C.right_child =node_F


# 실행 코드
test_node = root_node.right_child.right_child
print(test_node.data)

test_node = root_node.left_child.right_child.left_child
print(test_node.data)

test_node = root_node.left_child.right_child.right_child
print(test_node.data)