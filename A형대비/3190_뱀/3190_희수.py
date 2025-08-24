N = int(input())
K = int(input()) # 사과 개수
apple = {tuple(map(int, input().split())) for _ in range(K)}
L = int(input()) # 위치 변환 개수
move = [list(input().split()) for _ in range(L)]
# L: 왼쪽, D: 오른쪽
idx = 0 # 방향 변환 인덱스
time = 0
snake = [[1,1]]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
di = 0
crash = False

while True:
    head_x = snake[-1][0]
    head_y = snake[-1][1]
    head_x += dx[di]
    head_y += dy[di]

    if head_x > N or head_y > N or head_x <= 0 or head_y <= 0: # 보드 벗어나는지 확인
        time += 1
        break

    for x, y in snake: # 자기 몸에 부딪히는지 확인
        if head_x == x and head_y == y:
            crash = True
            time += 1
            break
    if crash: break

    if (head_y, head_x) not in apple: # 이동한 칸에 사과 없으면 꼬리 자르기
        snake.pop(0)
    else:
        apple.remove((head_y, head_x)) # 있으면 사과 먹어서 없애기

    snake.append([head_x, head_y]) # 뱀 머리 추가
    time += 1

    if idx < L and time == int(move[idx][0]): # 방향 변환 시간이면 방향 변환
        if move[idx][1] == 'D':
            di = (di + 1) % 4
        elif move[idx][1] == 'L':
            di = (di - 1) % 4
        idx += 1

print(time)
