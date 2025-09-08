'''
    물고기는 번호가 작은 순서대로 이동함.

    물고기는 방향이 이동할 수 있는 칸을 향할 때까지 반향을 45도 반시계 회전시킴.
    만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다.
    다른 물고기가 이미 존재하는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.

    물고기의 이동이 모두 끝나면 상어가 이동함. 
    상어는 방향에 있는 칸으로 이동할 수 있는데 한번에 여러개의 칸을 이동 가능하다.
    상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다.
    이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다.
    물고기가 없는 칸으로는 이동할 수 없다.

    상어가 이동할 수 있는 칸이 없으면 집으로 감.
'''
import copy

# 더미, 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]

# 초기값 받기
fish = list()
f_direction = list()
for i in range(4):
    temp = list(map(int, input().split()))
    f = [temp[i] for i in range(8) if i % 2 == 0]
    fish.append(f)
    d = [temp[i] for i in range(8) if i % 2 != 0]
    f_direction.append(d)

max_eat = 0

def dfs(fish, f_direction, shark_row, shark_col, shark_dir, now_eat):
    global max_eat
    # 물고기 이동
    
    for f_num in range(1, 17):
        f_row, f_col = -1, -1
        # 현재 물고기 위치 찾기
        for i in range(4):
            for j in range(4):
                if fish[i][j] == f_num:
                    f_row, f_col = i, j
                    break
        
        # 물고기가 없으면 건너뜀
        if f_row == -1:
            continue
            
        original_dir = f_direction[f_row][f_col]
        
        # 이동할 수 있는 방향을 찾을 때까지 45도씩 반시계 회전
        for i in range(8):
            new_dir = (original_dir - 1 + i) % 8 + 1

            ny, nx = f_row + dy[new_dir], f_col + dx[new_dir]
            
            if 0 <= ny < 4 and 0 <= nx < 4 and fish[ny][nx] != -1:
                f_direction[f_row][f_col] = new_dir
                
                fish[f_row][f_col], fish[ny][nx] = fish[ny][nx], fish[f_row][f_col]
                f_direction[f_row][f_col], f_direction[ny][nx] = f_direction[ny][nx], f_direction[f_row][f_col]
                break
    
    # 물고기 이동 끝
    
    # 종료 조건
    # 상어의 이동 경로에 주어진 물고기가 없을 경우
    cannot_eat = True
    
    # 상어 이동
    for i in range(1, 4):
        ny, nx = shark_row + (dy[shark_dir] * i), shark_col + (dx[shark_dir] * i)
        
        # 상어는 물고기가 있는 칸(0보다 큰 칸)으로만 이동 가능
        if 0 <= ny < 4 and 0 <= nx < 4 and fish[ny][nx] > 0:
            cannot_eat = False
            
            # 다음 재귀로 넘어가기 전 상태 변경
            temp_fish = fish[ny][nx]
            fish[ny][nx] = -1                  #  상어의 새 위치
            fish[shark_row][shark_col] = 0     #  상어가 떠난 자리는 빈칸(0)으로 만듦
            
            dfs(copy.deepcopy(fish), copy.deepcopy(f_direction), ny, nx, f_direction[ny][nx], now_eat + temp_fish)
            
            # 재귀가 끝난 후 상태 원상 복구 (Backtracking)
            fish[shark_row][shark_col] = -1    # 상어의 위치를 원래대로 복원
            fish[ny][nx] = temp_fish           # 먹혔던 물고기도 원래대로 복원
        
    if cannot_eat:
        max_eat = max(max_eat, now_eat)
    
    return

start = fish[0][0]
fish[0][0] = -1
dfs(fish, f_direction, 0, 0, f_direction[0][0], start)

print(max_eat)