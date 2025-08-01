from collections import deque

N = int(input())
adj_list = [[] for _ in range(N+1)]
parents = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

# 사이클이 없는 연결 그래프이므로 한 노드를 루트로 정하면
# 그 외의 모든 노드에 대해 고유한 부모가 생김
# -> 처음으로 방문해서 도달한 경로 상의 이전 노드가 부모가 됨
def dfs(start):
    queue = deque([start])
    visited = [False] * (N+1)
    visited[start] = True

    while queue:
        node = queue.popleft()
        for neighbor in adj_list[node]: 
            if not visited[neighbor]:
                parents[neighbor] = node # 부모로 저장
                visited[neighbor] = True # 방문 표시
                queue.append(neighbor) # queue에 저장

dfs(1)

for i in range(2, N+1):
    print(parents[i])