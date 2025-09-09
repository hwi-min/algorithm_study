"""
find_eatable_fishes 함수
: 현재 위치(start_x, start_y) 기준으로 먹을 수 있는 물고기(eatable_fishes)를 '모두'탐색
: sort를 활용해 가장 가깝거나, 가장 위에 있거나, 왼쪽에 있는 물고기 하나를 선택할 수 있게함

함수 실행부
: 각 이동 위치에 따른 먹을 수 있는 물고기(find_eatable_fishes)중 가장 첫 물고기를 먹음
: 그리고 자신의 크기만큼의 물고기를 다 먹으면 -> 상어상태 업데이트
: 모두 완료하면 -> 그 다음 갈 수 있는 위치 탐색해서 먹음
"""
from collections import deque

# 아기 상어의 이동 방향 (상, 좌, 하, 우 순으로 우선순위)
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)] 

# 현재 위치에서 먹을 수 있는 물고기들을 찾음
def find_eatable_fishes(start_x, start_y, shark_size):
    # 이 BFS는 한 번의 탐색만을 위한 것 -> 매번 큐와 방문 기록을 새로 만듦.
    visited = [[False] * N for _ in range(N)]
    queue = deque([(0, start_x, start_y)]) # (거리, x좌표, y좌표)
    visited[start_x][start_y] = True
    
    eatable_fishes = [] # 현재 위치에서 먹을 수 있는 물고기들의 정보를 담을 리스트

    while queue: # N * N 그리그를 최대 한 번씩 방문 -> 최악의 경우 O(N^^2) : 400번
        dist, x, y = queue.popleft()

        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            # 맵 범위 안이고, 아직 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 1. 이동 가능한 경우 (물고기 크기가 상어보다 작거나 같은 경우)
                if grid[nx][ny] <= shark_size:
                    visited[nx][ny] = True
                    queue.append((dist + 1, nx, ny)) # 거리를 1 증가시켜 큐에 추가

                    # 2. 먹을 수 있는 경우 (물고기가 있고, 상어보다 크기가 작은 경우)
                    if 0 < grid[nx][ny] < shark_size:
                        eatable_fishes.append((dist + 1, nx, ny))
    
    # 찾은 물고기들을 문제 조건(거리 -> y좌표 -> x좌표)에 맞게 정렬하여 반환
    if eatable_fishes:
        eatable_fishes.sort() # -> 최악의 경우 물고기 개수는 400개 
                              # O(n log n) 이므로 최악의 경우 O(N^^2 log N^^2) -> 즉 O(N^^2 log N)
                              # 400 log 20 -> 대략 400 * 4~5 = 1600 ~ 2000 
        return eatable_fishes
    else:
        return None # 먹을 수 있는 물고기가 없으면 None 반환


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 상어의 초기 상태 설정
shark_size = 2
ate_count = 0
total_time = 0
start_x, start_y = 0, 0

# 시작 위치 찾기 O(N^^2) -> 400
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            start_x, start_y = i, j
            grid[i][j] = 0 # 상어가 있던 자리는 빈칸으로 만듦
            break

while True:
    # 1. 현재 상어 위치에서 먹을 수 있는 물고기 목록을 찾음
    fishes = find_eatable_fishes(start_x, start_y, shark_size)
    
    # 2. 먹을 수 있는 물고기가 더 이상 없으면 엄마 상어에게 도움 요청 (종료)
    if not fishes:
        break
        
    # 3. 가장 우선순위가 높은 물고기(가장 가깝고, 위쪽, 왼쪽)를 선택
    dist_to_fish, fish_x, fish_y = fishes[0]
    
    # 4. 상어 상태 업데이트
    total_time += dist_to_fish # 물고기 먹으러 가는 데 걸린 시간 추가
    ate_count += 1
    
    # 상어 크기 성장 확인
    if ate_count == shark_size:
        shark_size += 1
        ate_count = 0 # 다시 먹은 물고기 수 초기화
    
    # 5. 상어 위치 이동 및 물고기 먹기
    grid[fish_x][fish_y] = 0 # 물고기를 먹어서 빈칸으로 만듦
    start_x, start_y = fish_x, fish_y # 상어 위치를 물고기 위치로 변경

print(total_time)

## 최종: 400 * 2000 = 800,000(80만)