# 배열 회전
def rotate(r, c, s, arr):
    new_arr = [row[:] for row in arr] # 새 배열 복사
    left = c-s-1 # 왼쪽 끝
    up = r-s-1 # 위쪽 끝
    right = c+s-1 # 오른쪽 끝
    down = r+s-1 # 아래쪽 끝
    mi = 0 # 회전 대상 점점 작아지게 만들 숫자
    while left < right and up < down: # 회전할 수 있을 때까지 배열 돌림
        new_arr[up][left + 1 : right + 1] = arr[up][left : right]
        new_arr[down][left : right] = arr[down][left + 1 : right + 1]
        for i in range(2 * s - mi):
            new_arr[up + 1 + i][right] = arr[up + i][right]
            new_arr[down - 1 - i][left] = arr[down - i][left]
        left += 1
        right -= 1
        up += 1
        down -= 1
        mi += 2 # 배열 크기 줄이기
    return new_arr

# 회전 연산 순서 순열 + 최소값 찾기
def dfs(arr):
    global min_sum
    if len(visited) == k: # 모든 연산 수행하면
        for row in arr: # 배열 행별로 계산
            min_sum = min(min_sum, sum(row)) # 최소값 저장
        return

    for i in range(k): # 회전 연산 순열
        if i not in visited:
            visited.append(i)
            r, c, s = info[i]
            result = rotate(r, c, s, arr)
            dfs(result)
            visited.pop()
        

n, m, k = map(int, input().split())
# 열, 행, 회전 연산 개수
arra = [list(map(int, input().split())) for _ in range(n)]
# 배열
info = [list(map(int, input().split())) for _ in range(k)]
# 회전 연산 정보 [r, c, s]
visited = []
min_sum = float('inf')

dfs(arra)
print(min_sum)