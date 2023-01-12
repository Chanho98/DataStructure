# 모든 요소를 0으로 초기화시킨 크기 6 x 6 인접 행렬
adjacency_matrix = [[0 for i in range(6)] for i in range(6)]

# 코드를 쓰세요
adjacency_matrix[0] = [0, 1, 1, 0, 0, 0]
adjacency_matrix[1] = [1, 0, 0, 1, 0, 1]
adjacency_matrix[2] = [1, 0, 0, 0, 0, 1]
adjacency_matrix[3] = [0, 1, 0, 0, 1, 1]
adjacency_matrix[4] = [0, 0, 0, 1, 0, 1]
adjacency_matrix[5] = [0, 1, 1, 1, 1, 0]

print(adjacency_matrix)