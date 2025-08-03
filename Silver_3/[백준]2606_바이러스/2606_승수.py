from collections import deque

# bfs 함수
def bfs(computer, start, visited):
    virus = deque([start])  # 퍼지는 바이러스를 저장할 virus queue
    visited[start] = True   # 시작점 방문 표시
    infected_computer = 0   # 감염된 컴퓨터 수

    # virus queue가 비어있지 않다면 반복
    # 뭐를 반복? 시작점부터 출발해 인접한 미방문 노드들을 queue에 삽입하며 깊이우선탐색
    while virus:
        v = virus.popleft()
        # print(v, end=' ')     # bfs의 순서를 알고 싶다면

        for i in computer[v]:   # queue에서 추출한 노드의 인접 노드들을 queue에 삽입
            if not visited[i]:  # 단 미방문 했을 때에만
                virus.append(i)
                visited[i] = True
                infected_computer += 1

    print(infected_computer)


com_cnt = int(input())  # 컴퓨터의 수
visited = [False] * (com_cnt + 1)     # 방문 표시할 리스트
computer = [[] for _ in range(com_cnt + 1)]     # bfs에 넘길 computer list

connected_pair = int(input())   # 네트워크 상 연결되어 있는 컴퓨터 쌍의 수

# 연결된 컴퓨터의 쌍 만큼 인접 쌍을 입력받아 리스트에 append
for _ in range(connected_pair):
    a, b = map(int, input().strip().split())
    computer[a].append(b)
    computer[b].append(a)

# 1번 노드를 시작으로 bfs 수행
bfs(computer, 1, visited)