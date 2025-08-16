# dir은 직접적으로 사용하지 않고, 단지 index 수정에서 실수하지 않기 위해 작성함
              # 가로    대각선     세로
dir = [(0, 1), (1, 1), (1, 0)]

def dfs(row, col, dir):
    global N, cnt
    """
    Parameters:
    - row: 현재 위치의 row
    - col: 현재 위치의 col
    -m dir: 현재 방향
    """

    # 종료 조건
    if (row, col) == (N-1, N-1):
        cnt += 1
        return

    # 현재 방향이 가로방향일때
    if dir == 0:
        # 가로로 이동 가능한지 확인
        if col + 1 < N and houses[row][col+1] != 1:
            dfs(row, col+1, 0)
        # 대각선으로 이동 가능한지 확인
        if col + 1 < N and row + 1 < N and houses[row+1][col+1] != 1:
            dfs(row+1, col+1, 1)

    elif dir == 1:
        # 가로로 이동 가능한지 확인
        if col + 1 < N and houses[row][col + 1] != 1:
            dfs(row, col + 1, 0)
        # 대각선으로 이동 가능한지 확인
        if col + 1 < N and row + 1 < N and houses[row + 1][col + 1] != 1:
            dfs(row + 1, col + 1, 1)
        # 세로로 이동 가능한지 확인
        if row + 1 < N and houses[row+1][col] != 1:
            dfs(row+1, col, 2)

    elif dir == 2:
        # 대각선으로 이동 가능한지 확인
        if col + 1 < N and row + 1 < N and houses[row + 1][col + 1] != 1:
            dfs(row + 1, col + 1, 1)
        # 세로로 이동 가능한지 확인
        if row + 1 < N and houses[row + 1][col] != 1:
            dfs(row + 1, col, 2)


# 실행
N = int(input())
houses = [list(map(int, input().strip().split())) for _ in range(N)]
cnt = 0 # 가능한 경로 초기화로

dfs(0, 1, 0)
print(cnt)


