from collections import deque


def wall(cnt, arr, idx):
    global max_result
    if cnt == 3: # 정지 조건 : 벽 3개 다 세움
        after_lab = virus(arr) # 벽 세운 상태에서 바이러스 퍼뜨리기
        result = sum(row.count(0) for row in after_lab) # 0 개수 반환
        max_result = max(max_result, result) # 최대값 찾기
        return
    
    if idx >= N * M: # 범위 벗어나면 탈출
        return

    # 처음에 for문 + visited 했는데 시간초과 나서 인덱스로 바꿈
    # 모든 인덱스 방문하기
    if arr[idx // M][idx % M] == 0: 
        arr[idx // M][idx % M] = 1
        wall(cnt + 1, arr, idx + 1)
        arr[idx // M][idx % M] = 0 # 백트래킹
    wall(cnt, arr, idx + 1)


def virus(arr):
    new_arr = [row[:] for row in arr] # 새 배열로 복사
    q = deque() # 큐 사용 (BFS)

    for i in range(N):
        for j in range(M):
            if new_arr[i][j] == 2: # 모든 칸 확인하면서 바이러스 있는 곳 큐에 저장
                q.append((i, j))
            
    while q:
        y, x = q.popleft()
        for d in range(4): # 감염된 곳의 인접 칸들 확인
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < M and 0 <= ny < N and new_arr[ny][nx] == 0: # 범위 안이면서, 바이러스 아직 감염 안된 곳인 경우
                new_arr[ny][nx] = 2 # 감염시킴
                q.append((ny, nx)) # 바이러스 큐에 저장

    return new_arr



N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
max_result = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

wall(0, lab, 0)
print(max_result)
