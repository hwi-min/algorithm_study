'''
    N x M 인 지도가 존재한다. 지도의 좌표는 r,c로 나타내면
    이동한 칸에 쓰여있는 수가 0이면, 바닥면에 쓰여있는 수가 복사됨.
    0이 아닌 경우 칸에 쓰여있는 수가 복사되고 칸은 0이됨.
    
    놓은곳의 좌표와 이동시키는 명령이 주어질 때,
    이동할 때 마다 상단에 쓰여있는 값을 출력
    
    만약 바깥으로 이동할려하면 명령 취소
'''
# 세로크기 N, 가로크기 M, 좌표 x,y, 명령의 개수 K
N, M, x, y, K = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

# 동쪽 : 1 서쪽 : 2 북쪽 : 3 남쪽 : 4 
# 동서북남 순
orders = input().split()
# 1-base
# top, bottom, E, W, N, S
# 0, 1, 2, 3, 4, 5
dice = [0] * 6

dd = {
    'top' : 0,
    'bottom' : 1,
    'east' : 2,
    'west' : 3,
    'north' : 4,
    'south' : 5
}
# 동 서 북 남
dy = [0,0,-1,1]
dx = [1,-1,0,0]

ny, nx = x, y
# 초기 바닥은 3
now_bottom = 3

for order in orders:
    order = int(order)-1
    # 0~3으로 바꾸어줌
    if 0 <= ny + dy[order] < N and 0 <= nx + dx[order] < M:
        ny, nx = ny + dy[order], nx + dx[order]
        # print(order, ny + dy[order], nx + dx[order])
        # 각 방향으로 이동
        # 동쪽 : 남,북 빼고 다 바뀜
        # east -> bottom, bottom -> west, west -> top, top -> east
        if order == 0:
            dice[dd['east']], dice[dd['bottom']], dice[dd['west']], dice[dd['top']] = \
                dice[dd['bottom']], dice[dd['west']], dice[dd['top']], dice[dd['east']]
        # 서쪽
        if order == 1:
            dice[dd['bottom']], dice[dd['east']], dice[dd['top']], dice[dd['west']] = \
                dice[dd['east']], dice[dd['top']], dice[dd['west']], dice[dd['bottom']]
        # 북쪽
        if order == 2:
            dice[dd['bottom']], dice[dd['south']], dice[dd['top']], dice[dd['north']] = \
                dice[dd['south']], dice[dd['top']], dice[dd['north']], dice[dd['bottom']]
        # 남쪽
        if order == 3:
            dice[dd['bottom']], dice[dd['north']], dice[dd['top']], dice[dd['south']] = \
                dice[dd['north']], dice[dd['top']], dice[dd['south']], dice[dd['bottom']]
                
        # 현재 바닥에서 이동 후 윗 방향 표시
        # 바닥 계산
        if grid[ny][nx] == 0:
            grid[ny][nx] = dice[dd['bottom']]
        else:
            dice[dd['bottom']] = grid[ny][nx]
            grid[ny][nx] = 0
        print(dice[dd['top']])
    # 범위 밖이면 pass
    else: continue
    
