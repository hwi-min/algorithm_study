from collections import deque

N, K = map(int, input().split())
queue = deque([i for i in range(1, N+1)])
result = []

while queue:
    for _ in range(K-1): # K-2 인덱스는 다시 queue에 삽입
        elem = queue.popleft()
        queue.append(elem)
    result.append(queue.popleft()) # K-1 인덱스는 결과에 append


print(f'<{", ".join(map(str, result))}>')