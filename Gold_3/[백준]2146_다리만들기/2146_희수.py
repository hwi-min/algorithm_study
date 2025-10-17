n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 0 = 바다, 1 = 육지
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
idx = 2 # 섬 구분 지을 인덱스 값
a, b = 0, 0 # 육지 경계 위치 저장할 값
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1: # 육지 발견하면
            island = [(j, i)]  #(x, y) # 육지 처음 발견한 값 큐에 넣기
            a, b = j, i # 육지 위치 값 저장

            while island: #BFS
                x, y = island.pop(0)
                if arr[y][x] == 1: # 처음 위치 섬 구분 인덱스 부여
                    arr[y][x] = idx
                    visited[y][x] = 1 # 방문 처리
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n and not visited[ny][nx]:
                        if arr[ny][nx] == 1: # 이동한 위치가 육지인 경우 섬 구분 인덱스 부여
                            arr[ny][nx] = idx
                            island.append((nx, ny))
                            visited[ny][nx] = 1
            idx += 1 #한 섬 모두 인덱스 부여했으면 다른 섬 구분
# for row in arr:
#     print(*row)
queue = [(a, b, 0, 0)] # (x, y, 시작 위치 정보, 다리 길이)
visited = [[n * n] * n for _ in range(n)]
answer = n * n

while queue: # 섬끼리 구분된 지도에서 BFS 탐색
    x, y, s, l, = queue.pop(0) # x, y, 시작 섬 인덱스, 다리 길이

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if arr[y][x] == 0 and arr[ny][nx] != 0 and arr[ny][nx] != s:
                # 이동 전 위치 = 바다 & 이동 후 위치 = 시작 섬과 다른 섬인 경우
                answer = min(answer, l) # 다리길이 최소값 갱신
                queue.append((nx, ny, arr[ny][nx], 0)) # 다시 섬에서 시작, 초기화
                visited[ny][nx] = 0 # 육지 방문 처리

            elif arr[y][x] != 0 and arr[ny][nx] == 0 and visited[ny][nx] > l + 1:
                # 이동 전 위치 = 육지 & 이동 후 위치 = 바다 & 다리 길이 이전 방문 시 다리 길이보다 짧은 경우
                queue.append((nx, ny, arr[y][x], l + 1)) # 위치 정보 업데이트, 시작 섬 인덱스 갱신, 다리 길이 추가
                visited[ny][nx] = l + 1 # 방문 처리 (다리 길이 정보 저장)

            elif arr[y][x] != 0 and arr[ny][nx] != 0 and visited[ny][nx] == n * n:
                # 이동 전 위치 = 육지 & 이동 후 위치 육지 & 아직 방문 안한 경우
                queue.append((nx, ny, s, 0)) # 위치 정보 업데이트, 다리 길이 = 0
                visited[ny][nx] = 0 # 육지 방문 처리

            elif arr[y][x] == 0 and arr[ny][nx] == 0 and visited[ny][nx] > l + 1:
                # 이동 전 위치 바다 = & 이동 후 위치 = 바다 & 다리 길이 이전 방문 시 다리 길이보다 짧은 경우
                queue.append((nx, ny, s, l + 1)) # 위치 정보 업데이트, 다리 길이 추가
                visited[ny][nx] = l + 1 # 방문 처리 (다리 길이 정보 저장)

print(answer)
