# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]

# diag1 = [False] * (2*N)   # 우하향 대각선
# diag2 = [False] * (2*N)   # 좌하향 대각선

# pos_black, pos_white = [], []
# for i in range(N):
#     for j in range(N):
#         if board[i][j] == 1:   # 비숍 놓을 수 있는 칸
#             if (i+j) % 2 == 0:
#                 pos_black.append((i, j))
#             else:
#                 pos_white.append((i, j))

# def dfs(idx, cnt, positions):
#     if idx == len(positions):
#         return cnt

#     x, y = positions[idx]
#     res = dfs(idx+1, cnt, positions)  # 놓지 않음
#     if not diag1[x+y] and not diag2[x-y+N]:
#         diag1[x+y] = diag2[x-y+N] = True
#         res = max(res, dfs(idx+1, cnt+1, positions))
#         diag1[x+y] = diag2[x-y+N] = False
#     return res

# ans = dfs(0, 0, pos_black) + dfs(0, 0, pos_white)
# print(ans)


def is_valid_pos(board, row, col):
    # 좌상향 대각선 위 체크
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # 우상향 대각선 위 체크
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def dfs(idx, positions, board, cnt):
    # 모든 칸을 다 확인했다면 최대 개수 갱신
    global max_cnt
    if idx == len(positions):
        max_cnt = max(max_cnt, cnt)
        return

    x, y = positions[idx]

    # 현재 칸에 놓는 경우
    if is_valid_pos(board, x, y):
        board[x][y] = 1
        dfs(idx + 1, positions, board, cnt + 1)
        board[x][y] = 0

    # 현재 칸에 놓지 않는 경우
    dfs(idx + 1, positions, board, cnt)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 흑/백 칸 분리

# 체스판을
# 흑 백 흑 백
# 백 흑 백 흑
# 흑 백 흑 백
# 백 흑 백 흑
# 으로 생각하면 (행+열)의 합이 짝수인 칸은 흑, 홀수인 칸은 백
# 서로 공격할 수 없으므로 흑/백 칸을 나누어 각각 독립적으로 탐색 가능 -> 시간 단축

black_positions = []
white_positions = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:  # 비숍 놓을 수 있는 칸
            if (i + j) % 2 == 0:
                black_positions.append((i, j))
            else:
                white_positions.append((i, j))

# 흑/백 독립 탐색
max_cnt = 0
dfs(0, black_positions, [[0]*n for _ in range(n)], 0)
black_max = max_cnt

max_cnt = 0
dfs(0, white_positions, [[0]*n for _ in range(n)], 0)
white_max = max_cnt

print(black_max + white_max)
