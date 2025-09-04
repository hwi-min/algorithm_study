import copy

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

def move_fish(board, sx, sy): # 물고기 이동
    for num in range(1, 17): # 모든 물고기 순회
        found = False
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == num:
                    found = True
                    y, x = i, j
                    break
            if found: break

        if not found: # 이미 먹힌 경우 넘기기
            continue

        d = board[y][x][1]
        for _ in range(8): # 방향 회전
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx != sx or ny != sy): # 범위 안이고, 상어 위치 아니면 이동
                board[y][x][1] = d
                board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
                break
            d = d % 8 + 1 # 아니면 회전

def dfs(board, sx, sy, total):
    global answer
    new_board = copy.deepcopy(board)

    n, d = new_board[sy][sx] # 현재칸 물고기 번호, 방향
    total += n # 먹음
    answer = max(answer ,total) # 최대값 갱신
    new_board[sy][sx] = (0, 0) # 먹은 처리

    move_fish(new_board, sx, sy) # 물고기 이동

    # 상어 이동
    for step in range(1, 4):
        nx, ny = sx + dx[d] * step, sy + dy[d] * step
        # 이동 가능하고 먹이 있으면
        if 0 <= nx < 4 and 0 <= ny < 4 and new_board[ny][nx][0] > 0:
            dfs(new_board, nx, ny, total)


info = [list(map(int, input().split())) for _ in range(4)]
board = [[(0, 0)] * 4 for _ in range(4)]  # [물고기 번호, 방향]
for i in range(4):
    for j in range(4):
        board[i][j] = [info[i][j*2], info[i][j*2+1]]
answer = 0

dfs(board, 0, 0, 0)
print(answer)
