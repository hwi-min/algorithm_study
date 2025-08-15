# 우, 우하, 하
# 현재 50분

dy = [0,1,1]
dx = [1,1,0]

def pipe_move(direction, row, col):
    '''
        현재 진행 방향, 현재 파이프의 좌표
    '''
    global way_to_carry
    
    # 종료조건
    # 파이프이 한쪽 끝이 N,N에 도달하면 방법 + 1
    if (row,col) == (N-1,N-1): way_to_carry += 1; return
    
    # 대각선이면 3방향에 벽이 있는지 확인해야함.
    if direction == 1: # 대각선 방향
        for i in [0,2]:
            ny, nx = row - dy[i], col - dx[i] # 좌, 상 확인
            # ny, nx가 집 안안지도 확인해야함.
            if 0 <= ny < N and 0 <= nx < N:
                if house[ny][nx] == 1 : return
            else: return
    
    # 재귀 작용
    # 3방향으로 모두 이동, 이동시 가능한지도 확인
    # 그 전에 현재 파이프 모양도 확인 해야 함.
    # 이동할 위치에 벽이 존재하면 가지 않음
    if direction == 1: # 대각선일 땐 세방향으로 이동 가능
        for i in range(3):
            ny, nx = row + dy[i], col + dx[i]
            if 0 <= ny < N and 0 <= nx < N and house[ny][nx] != 1:
                pipe_move(i, ny, nx)
    elif direction == 0: # 가로방향이였으면 우, 우하
        for i in [0,1]:
            ny, nx = row + dy[i], col + dx[i]
            if 0 <= ny < N and 0 <= nx < N and house[ny][nx] != 1:
                pipe_move(i, ny, nx)
    elif direction == 2: # 세로방향이였으면 우하, 하
        for i in [1,2]:
            ny, nx = row + dy[i], col + dx[i]
            if 0 <= ny < N and 0 <= nx < N and house[ny][nx] != 1:
                pipe_move(i, ny, nx)
    return

# 정방행렬의 크기
N = int(input())
# 집 구조
house = [list(map(int, input().split())) for _ in range(N)]

way_to_carry = 0
for i in [0,1]: # 처음엔 가로로 존재함, 우, 우하
    pipe_move(i, 0, 1) # 움직이는 끝 방향 좌표 (0,1)
    
print(way_to_carry)