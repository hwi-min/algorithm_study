import sys
input = sys.stdin.readline

# R 격자의 행, C 격자의 열, T 시간
R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 공청기 위치 찾기
aircleaner_top_row = -1
for row in range(R):
    if grid[row][0] == -1:
        aircleaner_top_row = row
        break
aircleaner_bottom_row = aircleaner_top_row + 1

# T초 동안 반복
for _ in range(T):
    # --- 1. 미세먼지 확산 ---
    # 확산 결과를 저장할 임시 배열 생성 (동시성을 위해)
    temp_grid = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if grid[r][c] > 0:
                amount = grid[r][c] // 5
                count = 0
                for i in range(4):
                    nr, nc = r + dy[i], c + dx[i]
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != -1:
                        temp_grid[nr][nc] += amount
                        count += 1
                # 남은 미세먼지 양 계산
                grid[r][c] -= amount * count

    # 확산된 양과 남은 양을 합쳐줌
    for r in range(R):
        for c in range(C):
            grid[r][c] += temp_grid[r][c]

    # 2. 공기청정기 순환
    # 위쪽 공기청정기 (반시계방향)
    # 아래 -> 위 (왼쪽 열)
    for r in range(aircleaner_top_row - 1, 0, -1):
        grid[r][0] = grid[r - 1][0]
    # 왼쪽 -> 오른쪽 (맨 윗줄)
    for c in range(0, C - 1):
        grid[0][c] = grid[0][c + 1]
    # 위 -> 아래 (오른쪽 열)
    for r in range(0, aircleaner_top_row):
        grid[r][C - 1] = grid[r + 1][C - 1]
    # 오른쪽 -> 왼쪽 (공기청정기 윗줄)
    for c in range(C - 1, 1, -1):
        grid[aircleaner_top_row][c] = grid[aircleaner_top_row][c - 1]
    # 공기청정기에서 나온 바람은 정화됨
    grid[aircleaner_top_row][1] = 0

    # 아래쪽 공기청정기 (시계방향)
    # 위 -> 아래 (왼쪽 열)
    for r in range(aircleaner_bottom_row + 1, R - 1):
        grid[r][0] = grid[r + 1][0]
    # 왼쪽 -> 오른쪽 (맨 아랫줄)
    for c in range(0, C - 1):
        grid[R - 1][c] = grid[R - 1][c + 1]
    # 아래 -> 위 (오른쪽 열)
    for r in range(R - 1, aircleaner_bottom_row, -1):
        grid[r][C - 1] = grid[r - 1][C - 1]
    # 오른쪽 -> 왼쪽 (공기청정기 아랫줄)
    for c in range(C - 1, 1, -1):
        grid[aircleaner_bottom_row][c] = grid[aircleaner_bottom_row][c - 1]
    # 공기청정기에서 나온 바람은 정화됨
    grid[aircleaner_bottom_row][1] = 0

# T초 후 남은 미세먼지 양 계산
total_dust = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] > 0:
            total_dust += grid[r][c]

print(total_dust)