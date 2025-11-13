from collections import deque

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
x, y = 1, 0
dice = [1, 2, 3, 4, 5, 6] # 윗면, 뒷면, 오른쪽면, 왼쪽면, 앞면, 바닥면
dice = [4, 2, 1, 6, 5, 3] # 동쪽으로 굴리기 (맨 처음)
direction = 1 # 1: 동, 2: 남, 3: 서, 4: 북 (시계방향)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
score = 0


for _ in range(k):
    if dice[5] > arr[y][x]: # 밑면이 숫자보다 크면 시계 방향
        direction += 1
        if direction > 4:
            direction -= 4
    elif dice[5] < arr[y][x]: # 아니면 반시계
        direction -= 1
        if direction <= 0:
            direction += 4

    if y + dy[direction - 1] < 0 or y + dy[direction - 1] >= n or x + dx[direction - 1] < 0 or x + dx[direction - 1] >= m: # 범위 벗어나면 반대 방향
        if direction == 1: direction = 3
        elif direction == 2: direction = 4
        elif direction == 3: direction = 1
        elif direction == 4: direction = 2

    if direction == 1: # 동쪽 굴리기
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]

    elif direction == 2: # 남쪽 굴리기
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    elif direction == 3: # 서족 굴리기
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]

    elif direction == 4: # 북 굴리기
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

    queue = deque([(x, y)]) #bfs 점수계산
    num = arr[y][x]
    visited = [[0] * m for _ in range(n)]
    visited[y][x] = 1
    count = 1

    while queue:
        a, b = queue.popleft()

        for d in range(4):
            nx, ny = a + dx[d], b + dy[d]

            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and arr[ny][nx] == num:
                queue.append((nx, ny))
                visited[ny][nx] = 1
                count += 1

    x, y = x + dx[direction - 1], y + dy[direction - 1]
    score += count * num
    # print(count, num, dice[5], direction, x, y)

print(score)