from collections import deque

n, m = map(int, input().split()) # 세로, 가로
arr = [list(map(int, input())) for _ in range(n)]

visited = [[[0, 0] for _ in range(m)] for _ in range(n)] #[y][x][벽 부시기 전/후 방문(0/1)]
queue = deque([(0, 0, 0, 1)]) # x, y, 벽 부신 여부, 지나온 칸 수
visited[0][0][0] = 1 # 벽 부시기 전 (0, 0) 방문 처리

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = n * m
is_arrived = False

while queue: #BFS
    x, y, b, c = queue.popleft() # x, y, 벽 부신 여부, 지나온 칸 수

    if x == m - 1 and y == n - 1: # 도착점 도착 시,
        answer = min(answer, c) # 답 최소값 갱신
        is_arrived = True # 도착점 도착 표시

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d] # 이동

        if nx >= 0 and nx < m and ny >= 0 and ny < n:
            if b == 0 and not visited[ny][nx][0]: # 벽 안부시고, 벽 부시기 전 방문 안했을 때,
                if arr[ny][nx] == 0: # 벽이 아니면
                    queue.append((nx, ny, b, c + 1))  # 이동 처리, 지나온 칸 + 1
                    visited[ny][nx][0] = 1 # 벽 부시기 전 방문 처리

                else: # 벽이면
                    queue.append((nx, ny, 1, c + 1)) # 이동 처리, 벽 부신 여부 갱신, 지나온 칸 + 1
                    visited[ny][nx][0] = 1 # 벽 부시기 전 방문 처리

            elif b == 1 and not visited[ny][nx][1]: # 벽 부시고, 벽 부신 후 방문 안했을 때,
                if arr[ny][nx] == 0: # 벽이 아니면
                    queue.append((nx, ny, b, c + 1)) # 이동 처리, 지나온 칸 + 1
                    visited[ny][nx][1] = 1 # 벽 부신 후 방문 처리

if is_arrived:
    print(answer)
else:
    print(-1)
