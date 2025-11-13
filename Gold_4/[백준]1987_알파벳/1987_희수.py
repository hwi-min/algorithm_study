def dfs (x, y, cnt):
    global answer, r, c, visited

    answer = max(answer, cnt)

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < c and 0 <= ny < r and board[ny][nx] not in visited:
            visited.add(board[ny][nx])
            dfs(nx, ny, cnt + 1)
            visited.remove(board[ny][nx])

    return


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

queue = [(0, 0, 1)]
visited = set()
visited.add(board[0][0])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
dfs(0, 0, 1)

print(answer)
