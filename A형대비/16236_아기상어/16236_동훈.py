from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

# 공간의 크기 N
N = int(input())

# 공간의 상태
grid = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어의 현재 크기, 위치, 먹은 물고기 수
shark_size = 2
shark_y, shark_x = 0, 0
eat_count = 0

# 총 걸린 시간
total_time = 0

for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            shark_y, shark_x = i, j
            grid[i][j] = 0  # 상어가 있던 자리는 빈칸(0)으로 처리
            break

def find_fish(start_y, start_x):
    """
    현재 상어 위치에서 먹을 수 있는 모든 물고기를 찾아
    (거리, y좌표, x좌표) 리스트로 반환하는 함수
    """
    q = deque([(start_y, start_x, 0)])  # 큐에 (y, x, 거리)를 넣음
    visited = [[False] * N for _ in range(N)]  # 방문 여부 체크 배열
    visited[start_y][start_x] = True
    
    edible_fishes = []  # 먹을 수 있는 물고기들을 저장할 리스트

    while q:
        y, x, dist = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            # 1. 지도 범위 안인지 확인
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            
            # 2. 방문했거나, 상어보다 큰 물고기가 있어 지나갈 수 없는지 확인
            if visited[ny][nx] or grid[ny][nx] > shark_size:
                continue
            
            # 3. 방문 처리 및 큐에 추가
            visited[ny][nx] = True
            
            # 4. 먹을 수 있는 물고기인지 확인 (0보다 크고 상어 크기보다 작음)
            if 0 < grid[ny][nx] < shark_size:
                # (거리, y, x) 순서로 저장 -> 정렬 시 우선순위 자동 적용
                edible_fishes.append((dist + 1, ny, nx))
            
            # 먹지는 못해도 지나갈 수는 있으므로 큐에 계속 추가
            q.append((ny, nx, dist + 1))
            
    return edible_fishes

while True:
    # 1. 현재 위치에서 먹을 수 있는 물고기 리스트를 찾음
    fishes = find_fish(shark_y, shark_x)

    # 2. 먹을 수 있는 물고기가 없는 경우 (엄마 상어에게 도움 요청)
    if not fishes:
        break  # 루프 종료
    
    # 3. 먹을 물고기 선택 (거리가 가장 가깝고, 가장 위쪽, 가장 왼쪽 순)
    fishes.sort()
    dist, fish_y, fish_x = fishes[0]

    # 4. 상어 이동 및 상태 업데이트
    total_time += dist  # 이동 시간 추가
    shark_y, shark_x = fish_y, fish_x  # 상어 위치 갱신
    grid[fish_y][fish_x] = 0  # 물고기 먹음 처리
    eat_count += 1

    # 5. 상어 성장 조건 확인
    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

print(total_time)