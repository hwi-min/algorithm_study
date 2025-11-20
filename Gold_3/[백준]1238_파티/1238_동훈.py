import sys
input = sys.stdin.readline

# N명의 학생이 X번 마을에 모여서 파티를 함. 마을 사이에는 총 M개의 단방향 도로들이 있음
N, M, X = map(int, input().split())

from collections import defaultdict
import heapq

# adj_list = dict(list())
adj_list = defaultdict(list)
reverse_adj_list = defaultdict(list)

for _ in range(M):
    s,e,t = map(int, input().split())
    adj_list[s].append((t,e))
    reverse_adj_list[e].append((t,s))
# print(adj_list)

pq = list()
dist_from_X = [float('inf')] * (N+1)
dist_from_X[X] = 0
heapq.heappush(pq, (0,X))

while pq:
    cur_cost, cur = heapq.heappop(pq)
    
    if dist_from_X[cur] < cur_cost: continue
    
    for cost, next_v in adj_list[cur]:
        new_cost = cur_cost + cost
        if new_cost < dist_from_X[next_v]:
            dist_from_X[next_v] = new_cost
            heapq.heappush(pq, (new_cost, next_v))

pq.clear()
dist_to_X = [float('inf')] * (N+1)
dist_to_X[X] = 0
heapq.heappush(pq, (0,X))

while pq:
    cur_cost, cur = heapq.heappop(pq)
    
    if dist_to_X[cur] < cur_cost: continue
    
    for cost, next_v in reverse_adj_list[cur]:
        new_cost = cur_cost + cost
        if new_cost < dist_to_X[next_v]:
            dist_to_X[next_v] = new_cost
            heapq.heappush(pq, (new_cost, next_v))

ans = 0
for i in range(1,N+1):
    cand = dist_from_X[i] + dist_to_X[i]
    if ans < cand:
        ans = cand
# print(dist_from_X)
# print(dist_to_X)
print(ans)