def dfs(x, y, direction):
    global count
    if x == n-1 and y == n-1:
        return 1
    
    if dp[y][x][direction] != -1:
        return dp[y][x][direction]
    
    ways = 0
    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= n or ny >= n: continue
        if abs(direction - i) > 1: continue
        if house[ny][nx]: continue
        if i == 1 :
            if house[y][nx] or house[ny][x]:
                continue
        ways += dfs(nx, ny, i)
    
    dp[y][x][direction] = ways
    return ways

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 1, 0]
dy = [0, 1, 1]
dp = [[[-1] * 3 for _ in range(n)] for _ in range(n)]

print(dfs(1, 0, 0))