import heapq

n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]
lectures.sort()

heap = []

for start, end in lectures:
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

print(len(heap))