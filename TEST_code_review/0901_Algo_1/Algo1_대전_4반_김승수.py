def find_set(x):    # 루트 찾기
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):    # 합치기
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parent[root_y] = root_x


def find_min_cost(edges):
    weights = []    # 최소 신장 트리에 포함될 정거장의 가중치 리스트

    # 가중치에 대해서 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    for edge in edges:  # 모든 간선에 대해서
        x, y, w = edge  # x: 시작정점, y: 도착정점, w: 가중치
        if find_set(x) != find_set(y):  # 루트 노드가 다르면
            union(x, y)         # 합치고
            weights.append(w)   # 리스트에 해당 가중치 추가

    # 최소 신장 트리에 포함된 간선의 개수가 정점의 개수 - 1이 아니라면
    # 모든 정거장 연결이 불가능하다는 뜻 -> -1 반환
    if len(weights) != N - 1: return -1

    # 아니라면 가중치 리스트의 합 반환
    return sum(weights)


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())    # N: 정점의 개수, E: 간선의 개수

    # 간선들의 정보(시작정점, 도착정점, 가중치)
    edges = [list(map(int, input().split())) for _ in range(E)]

    parent = [i for i in range(N + 1)]  # 부모 초기화
    min_cost = find_min_cost(edges)     # mst 함수 실행

    print(f'#{tc} {min_cost}')
