N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0

for i in range(N): # 배열 완탐
    for j in range(M):
        if j + 3 < M: # 가로 일자
            result = sum(arr[i][j : j+4])
            max_sum = max(max_sum, result)

        if i + 3 < N: # 세로 일자
            result = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+3][j]
            max_sum = max(max_sum, result)
        
        if j + 2 < M and i + 1 < N: # ㄹ 모양
            result = arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2]
            max_sum = max(max_sum, result)
            result = arr[i+1][j] + arr[i+1][j+1] + arr[i][j+1] + arr[i][j+2]
            max_sum = max(max_sum, result)
        
        for a in range(3): # ㄱ자 ㅗ자
            if i + 2 < N and j + 1 < M:
                result = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+a][j+1]
                max_sum = max(max_sum, result)
            
            if i + 2 < N and j - 1 >= 0:
                result = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+a][j-1]
                max_sum = max(max_sum, result)

            if i + 1 < N and j + 2 < M:
                result = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+a]
                max_sum = max(max_sum, result)

            if i - 1 >= 0 and j + 2 < M:
                result = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i-1][j+a]
                max_sum = max(max_sum, result)
            
        if i + 2 < N and j + 1 < M: # ㄹ 회전모양
            result = arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1]
            max_sum = max(max_sum, result)
            result = arr[i+1][j] + arr[i+2][j] + arr[i][j+1] + arr[i+1][j+1]
            max_sum = max(max_sum, result)
        
        if j + 1 < M and i + 1 < N: # ㅁ 모양
            result = arr[i][j] + arr[i+1][j+1] + arr[i][j+1] + arr[i+1][j]
            max_sum = max(max_sum, result)
        

print(max_sum)
