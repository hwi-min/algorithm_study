'''
    시작 좌표 : 0,0 시작 뱀 길이 : 1
    벽이나 자신의 몸과 부딫히면 게임 종료
'''
from collections import deque

# N x N 배열
N = int(input())
board = [[0] * N for _ in range(N)]

# 사과의 개수
K = int(input())
for _ in range(K):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1
    
# 변환 횟수 L
L = int(input())
# 변환 정보 X초 뒤에 L(왼쪽) 또는 D(오른쪽)으로 90도 회전
infos = [input().split() for _ in range(L)]

now_time = 0
now_direction = 1
# 현재 위치하고 있는 좌표 저장
snake = deque([(0,0)])

# 상 우 하 좌 
dy = [-1,0,1,0]
dx = [0,1,0,-1]
ny, nx = 0,0
flag = False
for time, direction in infos:
    # 방향 바뀌기 전까지 반복
    # print(time, direction, "for문")
    while now_time < int(time):
        # 1. 시간 추가
        now_time += 1
        # 머리 이동
        ny += dy[now_direction]
        nx += dx[now_direction]
        #print(now_time,ny,nx,snake)
        # 2. 범위, 몸 닿았는지 확인
        if 0 <= ny < N and 0 <= nx < N: # 범위 안
            if (ny,nx) in snake: # 머리가 몸에 닿았을때
                # print('닿음')
                flag = True
                break
            # 사과 먹으면 길이가 늘어남
            if board[ny][nx] == 1:
                # print('사과먹음')
                board[ny][nx] = 0
                snake.append((ny,nx))
            else: # 안먹었음 자리 이동
                snake.append((ny,nx))
                snake.popleft()
        else: # 범위 밖
            #print('범위초과')
            flag = True
            break
        
    # 종료 플래그
    if flag: break
    # 종료되지 않으면 방향 변환
    if direction == 'L': now_direction = (now_direction - 1) % 4
    elif direction == 'D': now_direction = (now_direction + 1) % 4

if flag == False:
    while True:
        # 1. 시간 추가
        now_time += 1
        # 머리 이동
        ny += dy[now_direction]
        nx += dx[now_direction]
        # print(now_time,ny,nx,snake)
        # 2. 범위, 몸 닿았는지 확인
        if 0 <= ny < N and 0 <= nx < N: # 범위 안
            if (ny,nx) in snake: # 머리가 몸에 닿았을때
                # print('닿음')
                break
            # 사과 먹으면 길이가 늘어남
            if board[ny][nx] == 1:
                # print('사과먹음')
                board[ny][nx] = 0
                snake.append((ny,nx))
            else: # 안먹었음 자리 이동
                snake.append((ny,nx))
                snake.popleft()
        else: # 범위 밖
            # print('범위초과')
            break
    
print(now_time)