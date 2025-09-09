import heapq


def dijk(graph, start): # 다익스트라
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cur_d, u = heapq.heappop(pq)
        if cur_d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = cur_d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    
    return dist


V, E = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(E)]
graph = [[] for _ in range(V + 1)]
M, x = map(int, input().split())
macs = list(map(int, input().split()))
S, y = map(int, input().split())
stars = list(map(int, input().split()))
INF = float('inf')
for s, e, w in info:
    graph[s].append((e, w))
    graph[e].append((s, w))

min_dist = INF

for i in range(M): # 모든 맥도날드 정점 돌기
    for j in range(S): # 모든 스타벅스 정점 돌기
        mac_dist = dijk(graph, macs[i]) # i번째 맥도날드 시작점 최단 거리 리스트
        star_dist = dijk(graph, stars[j]) # j번째 스타벅스 시작점 최단 거리 리스트
        for k in range(1, len(graph)): # 모든 집이랑 거리 비교
            if mac_dist[k] <= x and star_dist[k] <= y and i not in set(macs) and j not in set(stars):
                # 맥도날드와의 거리가 기준 이하고, 스타벅스와의 거리가 기준 이하고, 맥도날드 스타벅스 위치가 아닌 집에 대하여
                min_dist = min(min_dist, mac_dist[k] + star_dist[k]) # 최소값 구하기

if min_dist == INF: # 만약 갱신 안됐으면 -1 반환
    min_dist = -1
print(min_dist)