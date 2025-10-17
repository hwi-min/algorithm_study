from collections import deque
import sys
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,-1,1]

N = int(input().strip())
grid = [list(map(int, input().split())) for _ in range(N)]

# 1) 섬 레이블링: 2,3,... 로 바꾼다
def label_island(sy, sx, label):
    q = deque()
    q.append((sy, sx))
    grid[sy][sx] = label
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and grid[ny][nx] == 1:
                grid[ny][nx] = label
                q.append((ny, nx))

label = 2
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:
            label_island(i, j, label)
            label += 1

owner = [[0]*N for _ in range(N)]   # 어떤 섬이 이 칸을 확장했는가 (섬 번호)
dist = [[-1]*N for _ in range(N)]    # 해당 섬으로부터의 거리 (육지 셀은 0)
q = deque()

# 초기화: 모든 육지 칸을 큐에 넣고 owner=섬번호, dist=0
for i in range(N):
    for j in range(N):
        if grid[i][j] > 0:
            owner[i][j] = grid[i][j]
            dist[i][j] = 0
            q.append((i, j))

# BFS 돌리면서 다른 섬과 접하면 후보 다리 길이 계산
INF = 2*N
ans = INF

while q:
    y, x = q.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if not (0 <= ny < N and 0 <= nx < N):
            continue

        # 아직 방문되지 않은 바다이면 현재 섬 소유로 채우고 확장
        if owner[ny][nx] == 0:
            owner[ny][nx] = owner[y][x]
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))
        # 이미 다른 섬이 확장해놓은 칸이면 다리 길이 후보 계산
        elif owner[ny][nx] != owner[y][x]:
            # 현재 칸과 상대 칸의 dist 합이 (건설해야 할 바다 칸 수)
            candidate = dist[ny][nx] + dist[y][x]
            if candidate < ans:
                ans = candidate

# for o in owner:
#     print(o)
    
# print()
# for d in dist:
#     print(d)
    
print(ans if ans != INF else 0)