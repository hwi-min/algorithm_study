"""
main: 탈주범검거
"""

import sys
from collections import deque

# 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

# 파이프 타입별로 이동 가능한 방향 정의
pipes = {
    1: [0, 1, 2, 3], 2: [0, 1], 3: [2, 3],
    4: [0, 3], 5: [1, 3], 6: [1, 2], 7: [0, 2]
}

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    # 세로크기 N, 가로크기 M, 시작위치세로 R, 시작위치가로 C, 소요시간 L
    N, M, R, C, L = map(int, input().split())
    base_tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    # 시작 위치 좌표
    # x,y,time
    queue = deque([(R,C,1)])
    visited[R][C] = True
    
    # 정답 초기화
    count = 1 # 시작 지점
    
    # queue가 빌 때 까지 반복
    while queue:
        y, x, current_time = queue.popleft()
        # 종료조건
        # 소요 시간이 다 되었으면 종료
        if current_time == L:
            continue

        current_pipe_type = base_tunnel[y][x]
        # 현 위치에서 갈 수 있는 모든 지점을 확인
        for direction in pipes[current_pipe_type]:
            # 파이프 타입에 따른 상하좌우로 이동
            ny = y + dy[direction]
            nx = x + dx[direction]
            # 이제 이동할 곳이 갈 수 있는 곳인지 확인

            # 경계 밖 조건 처리
            if ny < 0 or ny >= N or nx < 0 or nx >= M: continue
            # 이미 방문 했는지
            if visited[ny][nx] == True: continue
            # 파이프가 존재 하는지
            if base_tunnel[ny][nx] == 0: continue
            # 연결될 상대 파이프 정보를 확인
            neighbor_pipe_type = base_tunnel[ny][nx]
            # 이제 내 파이프와 연결될 파이프가 연결 될지 확인
            # direction : 상(0)하(1)좌(2)우(3)
            # pipe의 타입에 따라 상하좌우로 갈 수 있는 곳이 정해져 있음
            # 내가 위로 가려면 상대는 아래가 뚫려잇어야함
            # 내 방향 == direction, 상대의 방향 pipes[neighbor_pipe_type]
            is_connected = False # 기본값
            if direction == 0 and 1 in pipes[neighbor_pipe_type]: is_connected = True
            elif direction == 1 and 0 in pipes[neighbor_pipe_type]: is_connected = True
            elif direction == 2 and 3 in pipes[neighbor_pipe_type]: is_connected = True
            elif direction == 3 and 2 in pipes[neighbor_pipe_type]: is_connected = True

            # 아래는 모든 조건을 통과한 후보군들
            if is_connected:
                visited[ny][nx] = True
                queue.append((ny, nx, current_time + 1))
                count += 1


    print(f'#{tc} {count}')
