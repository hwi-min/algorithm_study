n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
dp = [[1] * n for _ in range(n)] # 첫째 칸부터 셈

cells = []
for y in range(n):
    for x in range(n):
        cells.append((arr[y][x], x, y)) # (대나무 수, x, y)

cells.sort() # 대나무 수 적은 순 정렬

for value, x, y in cells:
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and arr[ny][nx] > value:
            dp[ny][nx] = max(dp[ny][nx], dp[y][x] + 1) # 이동한 칸 수 최대 값 갱신

for y in range(n): # 모든 시작점 순회
    for x in range(n):
        answer = max(answer, dp[y][x]) # 최대값 갱신

print(answer)