# N X N 정사각 보드 위에서 게임 진행, 벽은 보드의 상하좌우 끝부분
# 게임 시작 시 뱀은 최상단좌측에 위치, 길이는 1, 처음에 오른쪽을 향함

# 뱀은 매 초마다 다음과 같은 규칙에 따라 이동
# 1. 몸길이를 늘려 다음 칸에 위치시킴.
# 2. 다음 칸이 벽이나 자기자신이라면 게임 끝
# 3. 이동한 칸이 사과라면 사과는 없어지고 꼬리는 그대로
# 4. 이동한 칸에 사과가 없으면 꼬리가 있던 칸 비우기

# 사과의 위치(K개, 행과 열로 주어짐, 사과의 위치는 모두 다르고, 1행 1열에는 사과가 없음)
# 뱀의 이동경로(정수 X와 문자 C: 시작 후 X초가 끝난 뒤 왼쪽('L') 또는 오른쪽('D')으로 90도 방향 회전)가 주어질 때
# 이 게임이 몇 초에 끝나냐

# def change_dir(r, c, direction):
#     if direction == 'L':    # 반시계 방향이다?
#         if r == 0 and c == 1:       # 오른쪽으로 가고 있었다면
#             r, c = -1, 0             # 위로 가게
#         elif r == -1 and c == 0:    # 위로 가고 있었다면
#             r, c = 0, -1             # 왼쪽으로 가게
#         elif r == 0 and c == -1 :   # 왼쪽으로 가고 있었다면
#             r, c = 1, 0              # 아래로 가게
#         else:                       # 아래로 가고 있었다면
#             r, c = 0, 1              # 오른쪽으로 가게
#
#     else:   # 시계 방향이다?
#         if r == 0 and c == 1:       # 오른쪽으로 가고 있었다면
#             r, c = 1, 0              # 아래로 가게
#         elif r == 1 and c == 0:     # 아래로 가고 있었다면
#             r, c = 0, -1             # 왼쪽으로 가게
#         elif r == 0 and c == -1:    # 왼쪽으로 가고 있었다면
#             r, c = -1, 0             # 위로 가게
#         else:                       # 위로 가고 있었다면
#             r, c = 0, 1              # 오른쪽으로 가게
#
#     return r, c

def change_dir(dr, dc, direction):
    if direction == 'L':  # 반시계: (x,y) -> (-y,x)
        return -dc, dr
    else:                 # 시계:   (x,y) -> (y,-x)
        return dc, -dr


from collections import deque

board_width = int(input())  # 보드의 크기 (2 <= 크기 <= 100)

# 현재 뱀이 차지하고 있는 보드(1-based 이므로 1 더해주기)
# snake_range = [[False] * (board_width + 1) for _ in range(board_width + 1)]
# nr, nc = 1, 1   # 시작 위치 (1, 1)
# snake_range[nr][nc] = True

# 뱀의 몸을 저장하는 덱 (머리가 앞(left), 꼬리가 뒤(right))
snake_body = deque([(1, 1)])
# 현재 뱀이 차지하고 있는 보드 (1-based 이므로 시작은 (1, 1))
snake_range = {(1, 1)}

apples = int(input())   # 사과의 개수 (0 <= 개수 <= 100)
apples_pos = set()  # 사과 위치 저장할 set

for _ in range(apples): # 사과 개수만큼 입력 받기
    r, c = map(int, input().split())
    apples_pos.add((r, c))

switch_count = int(input()) # 방향 전환 횟수
snake_direction_change = [] # 방향 전환 정보 저장 리스트

for _ in range(switch_count):   # 방향 전환 횟수만큼 입력 받기
    snake_direction_change.append(list(input().split()))

second = 0  # 게임이 끝나는 시간
switch_idx = 0  # 현재까지 방향 전환 횟수
# 처음엔 오른쪽으로
dr, dc = 0, 1

while True:
    # 방향 전환 시간과 방향 저장
    if switch_idx < switch_count:
        time_to_change, direction = snake_direction_change[switch_idx]
        # 방향을 전환할 시간이 됐다면
        if second == int(time_to_change):
            dr, dc = change_dir(dr, dc, direction)
            switch_idx += 1

    second += 1  # 1초 경과

    head_r, head_c = snake_body[0]  # 뱀의 머리 위치
    nr, nc = head_r + dr, head_c + dc   # 다음 머리 위치

    # # 벽에 꿍하지 않았다면
    # if 1 <= nr <= board_width and 1 <= nc <= board_width:
    #     if not snake_range[nr][nc]: # 나와 부딪히지도 않는다면
    #         snake_range[nr][nc] = True  # 나 들어간다잉
    #         if [nr, nc] not in apples_pos:  # 그 곳에 사과가 없다면
    #             snake_range[nr - dr][nc - dc] = False   # 이전 칸 꼬리 자르기
    #             continue
    #         else: continue  # 사과 있었으면 꼬리 안자르고 다음 시간으로
    # # 벽에 부딪혔거나 나와 부딪혔다면 종료
    # break

    # 벽에 꿍했다면 종료
    if not (1 <= nr <= board_width and 1 <= nc <= board_width): break

    # 나와 충돌했다면 종료
    if (nr, nc) in snake_range: break

    # 새 머리 위치 추가
    snake_body.appendleft((nr, nc))
    snake_range.add((nr, nc))

    if (nr, nc) in apples_pos:  # 머리 위치에 사과가 있다면
        apples_pos.remove((nr, nc)) # 꼬리는 자르지 않고 사과만 제거
    else:   # 사과가 없다면
        tail_r, tail_c = snake_body.pop()   # 꼬리 자르고
        snake_range.remove((tail_r, tail_c))    # 뱀이 차지하고 있는 보드에서도 제거

print(second)
