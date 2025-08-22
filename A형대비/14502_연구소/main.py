from itertools import combinations
from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(comb, row, col):
    queue = deque([(row, col)])
    sub_lab = lab.copy()
    visited = [[False] * M for _ in range(N)]
    visited[row][col] = True
    
    # comb에 대한 벽 먼저 세움
    for comb_x, comb_y in comb:
        sub_lab[comb_x][comb_y] == 1

    while queue:
        x, y = queue.popleft() # 바이러스가 있는 좌표 가져옴
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < N and 0 <= ny < M and sub_lab[nx][ny] != 1 and not visited[nx][ny]: # 1이 아니면 바이러스 감염
                sub_lab[nx][ny] = 2
                queue.append((nx, ny))
                visited[nx][ny] = True
                nx, ny = nx + dx, ny + dy

    return sub_lab.count(0)




N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(M)]

"""
- 0인 좌표들의 모든 조합을 구함 (combinations)
- 해당 좌표들에 대한 시뮬레이션을 실행 -> 계속해서 min값을 업데이트

- bfs
    - 모든 행을 돌면서 만약, 
"""
# 안전영역의 최대값 초기화
max_safe_zone = 0

blank_list = []
# 빈칸(0)인 좌표들만 따로 저장
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            blank_list.append((i, j))


# 모든 blank_list의 조합을 찾음
for comb in combinations(blank_list, 3):
    # 해당 comb에 대한 bfs 결과 후 안전영역의 수를 셈
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                current_safe_zome = bfs(comb, i, j)
                if current_safe_zome > max_safe_zone:
                    max_safe_zone = current_safe_zome

print(max_safe_zone)


"""
from collections import deque

def bfs(graph, start_node):
    # 1. 큐(Queue) 생성 및 시작 노드 추가
    queue = deque([start_node])
    
    # 2. 방문 리스트(visited) 생성 및 시작 노드 방문 처리
    visited = [False] * (len(graph) + 1)
    visited[start_node] = True
    
    # 3. 큐가 빌 때까지 반복
    while queue:
        # 4. 큐에서 노드 하나를 꺼내기
        current_node = queue.popleft()
        print(current_node, end=' ')
        
        # 5. 현재 노드와 연결된 인접 노드 탐색
        for neighbor in graph[current_node]:
            # 6. 인접 노드가 아직 방문하지 않은 노드라면
            if not visited[neighbor]:
                # 7. 방문 처리하고 큐에 추가
                visited[neighbor] = True
                queue.append(neighbor)

# 예시 그래프
graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2, 8],
    5: [2, 8],
    6: [3, 8],
    7: [3, 8],
    8: [4, 5, 6, 7]
}

# BFS 실행
print("BFS 탐색 순서:")
bfs(graph, 1)"""