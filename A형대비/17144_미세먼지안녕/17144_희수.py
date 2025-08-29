import copy


r, c, t = map(int, input().split()) # 행, 열, 시간
room = [list(map(int, input().split())) for _ in range(r)]
cleaner = []

# 공기청정기 위치 찾기
for i in range(r):
    if room[i][0] == -1:
        cleaner.append(i)
        cleaner.append(i+1)
        break
time = 0
while time < t:
    # 미세먼지 확산
    spread = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0: # 먼지가 있으면
                dust = room[i][j] // 5 # 확산된 먼지양
                cnt = 0
                for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)): # 사방으로 먼지 확산
                    ni, nj = i+dx, j+dy
                    if 0 <= ni < r and 0 <= nj < c and room[ni][nj] != -1:
                        spread[ni][nj] += dust
                        cnt += 1
                room[i][j] -= dust * cnt # 확산된 먼지만큼 감소

    for i in range(r): # 확산된 먼지 더해주기
        for j in range(c):
            room[i][j] += spread[i][j]

    # 바람 순환 (위, 반시계)
    sub_room = copy.deepcopy(room)
    sub_room[cleaner[0]][1] = 0 # 공기청정기 바로 옆은 0
    sub_room[cleaner[0]][2 : c] = room[cleaner[0]][1 : c-1] # 공기청정기 윗줄
    sub_room[0][0 : c-1] = room[0][1 : c] # 맨 윗줄
    for i in range(cleaner[0] - 1): # 왼쪽
        sub_room[i + 1][0] = room[i][0] # 아래로
    for i in range(cleaner[0]): # 오른쪽
        sub_room[i][c-1] = room[i+1][c-1] # 위로

    # 바람 순환 (아래 , 시계)
    sub_room[cleaner[1]][1] = 0 # 공기청정기 바로 옆은 0
    sub_room[cleaner[1]][2: c] = room[cleaner[1]][1: c - 1] # 공기청정기 아랫줄
    sub_room[r-1][0: c - 1] = room[r-1][1: c] # 맨 아랫줄
    for i in range(cleaner[1] + 2, r): # 왼쪽
        sub_room[i - 1][0] = room[i][0] # 위로
    for i in range(cleaner[1] + 1, r): # 오른쪽
        sub_room[i][c-1] = room[i - 1][c-1] # 아래로
    time += 1 # 시간 증가
    room = copy.deepcopy(sub_room) # 방 상태 갱신

# 남아있는 미세먼지 양 계산
answer = 0
for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
           answer += room[i][j] 

print(answer)

