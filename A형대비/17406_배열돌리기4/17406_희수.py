def rotate(r, c, s, arr):
    new_arr = [row[:] for row in arr]
    left = c-s-1
    up = r-s-1
    right = c+s-1
    down = r+s-1
    mi = 0
    while left < right and up < down:
        new_arr[up][left + 1 : right + 1] = arr[up][left : right]
        new_arr[down][left : right] = arr[down][left + 1 : right + 1]
        for i in range(2 * s - mi):
            new_arr[up + 1 + i][right] = arr[up + i][right]
            new_arr[down - 1 - i][left] = arr[down - i][left]
        left += 1
        right -= 1
        up += 1
        down -= 1
        mi += 2
    return new_arr

def dfs(arr):
    global min_sum
    if len(visited) == k:
        for row in arr:
            min_sum = min(min_sum, sum(row))
        return

    for i in range(k):
        if i not in visited:
            visited.append(i)
            r, c, s = info[i]
            result = rotate(r, c, s, arr)
            dfs(result)
            visited.pop()
        

n, m, k = map(int, input().split())
arra = [list(map(int, input().split())) for _ in range(n)]
info = [list(map(int, input().split())) for _ in range(k)]
visited = []
min_sum = float('inf')

dfs(arra)
print(min_sum)