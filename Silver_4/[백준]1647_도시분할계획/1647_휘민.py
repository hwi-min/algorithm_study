def find_set(x):
    if x == parents[x]:
        return x
    return find_set(x)

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # 두 노드의 대표 노드가 다르다면? -> 결합할 수 있음
    if root_x != root_y:
        # x의 대표 노드의 랭크가 y의 대표 노드의 랭크보다 크다면
        if rank[root_x] > rank[root_y]:
            
            

N, M = map(int, input().split()) # 집의 개수, 간선의 개수
edges = []
parents = [i for i in range(N+1)] # 1-based, N개의 집에 대한 대표 노드 저장
rank = [0] * (N+1) # rank 초기화
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B)) # 유지비, A <-> B


