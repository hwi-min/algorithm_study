N, M, Y, X, K = map(int, input().split())
# 지도 세로 크기, 가로 크기, 주사위 좌표, 명령 개수
arr = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))
# 1: 동, 2: 서, 3: 북, 4: 남
dice = [0] * 7
# 인덱스 = 현재 주사위 상태 전개도, # 값 = 주사위에 적혀있는 값
# 예: [1] = 상단, [6] = 바닥면
answer = []

x, y = X, Y

for m in move: # 명령마다 행동
    if m == 1:
        nx, ny = x + 1, y
        if nx < 0 or nx >= M or ny < 0 or ny >= N: continue # 지도 밖으로 벗어나면 명령 무시
        # 방향에 맞게 주사위 굴려줌 => 전개도 인덱스 변경
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif m == 2:
        nx, ny = x - 1, y
        if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif m == 3:
        nx, ny = x, y - 1
        if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif m == 4:
        nx, ny = x, y + 1
        if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

    answer.append(dice[1]) # 상단에 적혀있는 값 답 리스트에 추가
    if arr[ny][nx] == 0: # 지도 값이 0이면, 지도 값에 주사위 바닥면 값 복사
        arr[ny][nx] = dice[6]
    else:
        dice[6] = arr[ny][nx] # 그 외로는 주사위 바닥면에 지도 값 복사 + 지도 값 0으로 초기화
        arr[ny][nx] = 0
    x, y = nx, ny

for a in answer:
    print(a)

            