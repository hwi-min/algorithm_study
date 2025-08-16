import sys
sys.stdin = open('input.txt')
"""
[접근 방식]
DFS (깊이 우선 탐색)를 이용하여 가능한 모든 사각형 경로를 탐색
- 각 지점에서 '현재 방향으로 직진'하는 경로와 '다음 방향으로 꺾는' 경로를 모두 탐색
- 재귀 호출 시, 현재 위치의 디저트를 방문 목록에 추가하고, 
    탐색이 끝나면 다시 제거(백트래킹)
"""

# 좌하 우하 우상 좌상
dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]


def search(x, y, dir, cnt):
    """
    DFS 방식으로 디저트 카페 투어 경로를 탐색하는 재귀 함수

    :param x: 현재 위치의 row 좌표
    :param y: 현재 위치의 col 좌표
    :param dir: 현재 진행 방향 (0:좌하, 1:우하, 2:우상, 3:좌상)
    :param cnt: 지금까지 먹은 디저트의 종류 수
    """
    global result

    # 종료 조건
    # 투어를 시작한 후,
    # 마지막 방향(3:좌상)으로 움직여 출발점으로 돌아온 경우
    # 디저트 개수의 최댓값을 갱신
    if dir == 3 and x == start_row and y == start_col:
        result = max(result, cnt)
        return

    # 현재 위치(x, y)가 유효한 범위 안에 있고,
    # 이 위치의 디저트를 아직 먹지 않은 경우에만 탐색을 진행합니다.
    if 0 <= x < N and 0 <= y < N and data[x][y] not in desserts:

        # 1. 현재 방향으로 계속 직진하는 경우
        # 다음 위치 계산
        nx, ny = x + dx[dir], y + dy[dir]

        # 현재 위치의 디저트를 먹은 것으로 처리
        desserts.append(data[x][y])
        # 다음 위치로 이동하며 재귀 호출
        search(nx, ny, dir, cnt + 1)
        # 다른 경로를 위해 현재 디저트를 먹지 않은 상태로 되돌림 (백트래킹)
        desserts.pop()

        # 2. 다음 방향으로 꺾어서 진행하는 경우
        # 지금 방향(3:좌상)이 아니어야만 방향을 꺾을 수 있음
        if dir < 3:
            # 다음 방향으로 이동할 위치 계산
            nx, ny = x + dx[dir + 1], y + dy[dir + 1]

            # 현재 위치의 디저트를 먹은 것으로 처리
            desserts.append(data[x][y])
            # 다음 위치, 다음 방향으로 재귀 호출
            search(nx, ny, dir + 1, cnt + 1)
            # 탐색이 끝나면, 백트래킹
            desserts.pop()


# === 메인 실행 부분 ===
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    # 못 먹는 상황을 기본 값으로 설정
    result = -1

    # 모든 지점을 시작점으로 하여 투어를 시작
    for x in range(N):
        for y in range(N):
            # 전역 변수로 시작점 좌표 설정
            start_row, start_col = x, y
            # 현재 투어에서 먹은 디저트 종류를 기록할 리스트
            desserts = []
            # DFS 탐색 시작
            search(x, y, 0, 0)

    print(f'#{tc} {result}')