import heapq


INF = float('inf')

def multi_source_dijkstra(graph, sources): # 멀티소스 다익스트라
    n = len(graph) - 1
    dist = [INF] * (n + 1)
    pq = []
    for s in sources: # 모든 시작점 다 넣기
        dist[s] = 0
        heapq.heappush(pq, (0, s))
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
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

M, x = map(int, input().split())
macs = list(map(int, input().split()))
S, y = map(int, input().split())
stars = list(map(int, input().split()))

dist_mac = multi_source_dijkstra(graph, macs) # 모든 맥도날드 중 각 집의 최단 거리
dist_star = multi_source_dijkstra(graph, stars) # 모든 스타벅스 중 각 집의 최단 거리

min_dist = INF

for v in range(1, V + 1): # 모든 집이랑 거리 비교
    if v in set(macs) or v in set(stars): # 맥날 위치, 스벅 위치 패스
        continue

    if dist_mac[v] <= x and dist_star[v] <= y: # 거리 기준 부합하면
        min_dist = min(min_dist, dist_mac[v] + dist_star[v]) # 최소값 갱신

if min_dist == INF: # 갱신 한 번도 안됐으면 -1 반환
    min_dist = -1
print(min_dist)
