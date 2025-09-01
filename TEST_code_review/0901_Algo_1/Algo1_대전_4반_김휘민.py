# # cost가 음수 값이 없음 -> mst로 풀면 됨

def find_set(x):
    if x != parents[x]:
        parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    root_x, root_y = find_set(x), find_set(y)
    # 두 대표가 다르면 UNION 가능
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parents[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parents[root_x] = root_y
        else:
            parents[root_y] = root_x
            rank[root_x] += 1
        return True
    return False

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split()) # N: 우주 정거장 수, M: 가능한 연결 수
    parents = [i for i in range(N+1)]
    rank = [0 for _ in range(N+1)]
    edges = []
    min_sum = 0

    for _ in range(M):
        x, y, cost = map(int, input().split())
        edges.append((x, y, cost))

    # edges 정렬
    edges.sort(key=lambda x: x[2])

    for x, y, cost in edges:
        if union(x, y): # union에 성공해서 True가 나오면
            min_sum += cost # 경로 추가

    group = set() # 대표자 그룹 초기화

    # 전체 대표자 돌면서 다시 대표자 확인
    for i in range(1, N+1):
        find_set(i)

    # 전체 대표자를 돌면서 이미 있는 대표자가 아니면 group에 추가
    for j in parents:
        if j not in group: group.add(j)

    # 대표자의 수가 2명이면(1-based이므로 0은 자동으로 들어가니까) 연결 가능하므로 minsum 반환, 그렇지 않은 경우 -1 반환
    print(f"#{t} {min_sum if len(group) == 2 else -1}")
