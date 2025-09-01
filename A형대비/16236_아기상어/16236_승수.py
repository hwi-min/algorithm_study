from collections import deque

#     상  하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_fish(row, col, size):
    queue = deque([(0, row, col)])  # (거리, 행, 열)
    visited = [[False] * N for _ in range(N)]
    # 현재 상어 위치 방문 표시
    visited[row][col] = True

    # 먹을 수 있는 물고기 리스트 (거리, 행, 열)
    # 먹을 수 있는 물고기가 여러 개라면
    # 거리 -> 행(위) -> 열(왼쪽) 순서에 따른 우선순위로 먹을 예정
    # 사실 거리에 대해서는 27번째 줄에서 걸러지기 때문에 행, 열만 따지면 된다
    can_eat_fish = []

    while queue:
        d, r, c = queue.popleft()

        # 현재 위치에 먹을 수 있는 물고기가 있다면
        if space_status[r][c] != 0 and space_status[r][c] < size:
            can_eat_fish.append((d, r, c))  # 후보군에 추가

        # 후보군에 존재하는 최단거리보다 긴 거리에 있는 물고기를 찾았다면 종료
        # 일종의 가지치기?
        if can_eat_fish and can_eat_fish[0][0] < d: break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 공간을 벗어나지 않고 방문하지 않았으며
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                # 상어 크기보다 물고기 크기가 작거나 같다면
                if space_status[nr][nc] <= size:
                    visited[nr][nc] = True  # 방문
                    queue.append((d + 1, nr, nc))    # 거리 + 1 해서 queue에 저장

    # 먹을 수 있는 물고기 후보군이 없다면 None 반환
    if not can_eat_fish: return None

    # 있다면 정렬
    can_eat_fish.sort()
    # 제일 거리가 가까운 (거리가 같다면 행이 가장 작은,
    # 행도 같으면 열이 가장 작은) 후보군 반환
    return can_eat_fish[0]


N = int(input())    # 공간의 크기
space_status = [list(map(int, input().split())) for _ in range(N)]
shark_row, shark_col = 0, 0     # 상어의 위치를 넣을 변수
time = 0    # 엄마 찾기까지 걸린 시간
eat_count = 0   # 먹은 물고기 수
shark_size = 2  # 상어의 크기

# 공간에서 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if space_status[i][j] == 9:
            shark_row, shark_col = i, j # 상어 위치 저장
            space_status[i][j] = 0      # 상어가 있던 곳은 0으로

# 먹을 물고기가 없을 때까지 반복
while True:
    # 현재 상어 위치에서 가장 가까운 물고기 찾기
    closest_fish = find_fish(shark_row, shark_col, shark_size)

    # 먹을 물고기가 없다면 종료
    if closest_fish is None: break

    # (가까운 물고기 까지의 거리, 물고기의 행, 열)
    dist, fish_row, fish_col = closest_fish

    time += dist    # 이동한 거리만큼 시간 증가
    eat_count += 1  # 물고기 먹어버리기

    shark_row, shark_col = fish_row, fish_col   # 상어 위치를 물고기 위치로 갱신
    space_status[fish_row][fish_col] = 0    # 물고기가 있던 곳은 0으로

    if eat_count == shark_size: # 상어의 크기만큼 물고기를 먹었다면
        shark_size += 1 # 상어의 크기 증가
        eat_count = 0   # 먹은 물고기 수 초기화

print(time)
