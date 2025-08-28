def find_set(x):
    if x == parents[x]:
        return x
    return find_set(parents[x])

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # 두 노드의 대표 노드가 다르다면? -> 결합할 수 있음
    if root_x != root_y:
        # x의 대표 노드의 랭크가 y의 대표 노드의 랭크보다 크다면
        if rank[root_x] > rank[root_y]:
            parents[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parents[root_x] = root_y
        else: 
            parents[root_y] = root_x
            rank[root_x] += 1
                         
            
N, M = map(int, input().split()) # 집의 개수, 간선의 개수
edges = [] # (1, 2, 3) (1, 3, 2) ... 
parents = [i for i in range(N+1)] # 1-based, N개의 집에 대한 대표 노드 저장
rank = [0] * (N+1) # rank 초기화
weight_sum = 0 # 최소 유지비 합
weight_list = [] # 선택된 가중치들의 합

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C)) # 시작점, 끝점, 유지비


# 가중치 기준 edges 정렬
edges.sort(key=lambda x: x[2]) # 유지비 기준 오름차순 정렬
# print(edges)

for edge in edges:
    s, e, w = edge

    # 두 집의 대표자가 다르면 union
    if find_set(s) != find_set(e): 
        union(s, e)
        weight_sum += w # 선택했으니까 유지비를 더해줌
        weight_list.append(w) # 유지비 리스트에 추가 -> 나중에 가장 큰 유지비를 뺄 것이기 때문에

# 길 하나를 끊어 두개의 집합으로 만들기
hightest = max(weight_list)
weight_sum -= hightest

print(weight_sum)



