# 강의실 배정
'''
    모든 수업을 가능하게 하는데 필요한 최소 강의실 개수
'''

import heapq,sys

input = sys.stdin.readline

N = int(input())
rooms = []
for _ in range(N):
    start, end = map(int, input().split())
    rooms.append([start, end])

rooms.sort(key=lambda x : (x[0],x[1]))
# print(rooms)
heap = []

for s,e in rooms:
    if heap:
        # 만약 시작시간이 가장 빨리 끝나는 강의보다 빨리 시작하면
        if s < heap[0]: # 강의장 하나 추가
            heapq.heappush(heap, e)
        else: # 똑같거나 더 늦게 시작하면
            heapq.heappop(heap)
            heapq.heappush(heap,e)
    else:
        heapq.heappush(heap, e)
    
print(len(heap))