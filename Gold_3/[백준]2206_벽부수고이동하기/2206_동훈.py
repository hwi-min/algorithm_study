from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

# visited[r][c][0] : 벽 안 부숨, visited[r][c][1] : 벽 부숨
visited = [[[False]*2 for _ in range(M)] for _ in range(N)]
queue = deque()
queue.append((0, 0, 0, 1))  # (row, col, 벽부숨여부, 거리)
visited[0][0][0] = True

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ans = -1

while queue:
    r, c, broken, dist = queue.popleft()
    if r == N-1 and c == M-1:
        ans = dist
        break
    
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if 0 <= nr < N and 0 <= nc < M:
            # 벽이 아닌 곳
            if grid[nr][nc] == 0 and not visited[nr][nc][broken]:
                visited[nr][nc][broken] = True
                queue.append((nr, nc, broken, dist+1))
            # 벽인데 아직 안 부순 상태라면
            elif grid[nr][nc] == 1 and broken == 0 and not visited[nr][nc][1]:
                visited[nr][nc][1] = True
                queue.append((nr, nc, 1, dist+1))

print(ans)