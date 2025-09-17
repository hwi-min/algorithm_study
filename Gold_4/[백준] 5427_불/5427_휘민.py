"""
시간제한: 1초(1억)
w, h <= 1000 / 최대 1000000 (백만)
"""
from collections import deque
# 상하좌우 좌표
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# bfs로 돌면서 fire_time을 저장
def fire(fire_queue):
    global f_visited

    while fire_queue: # queue를 순회하면서
        current_x, current_y, current_time = fire_queue.popleft()

        for dx, dy in direction:
            nx, ny = current_x + dx, current_y + dy

            if (nx, ny) not in f_visited and 0 <= nx < h and 0 <= ny < w and building[nx][ny] != '#': # building 범위 안에 있고 아직 방문하지 않았고 불이 퍼질 수 있는 '.'이라면
                fire_queue.append((nx, ny, current_time + 1)) # 이 다음 초에 불이 붙을 거니까! queue에 넣어주고
                f_visited.add((nx, ny)) # 방문 처리
                fire_time[nx][ny] = current_time + 1


def save_sanggeun(sanggeun_queue):
    global s_visited

    while sanggeun_queue:
        current_x, current_y, current_time = sanggeun_queue.popleft()

        for dx, dy in direction:
            nx, ny = current_x + dx, current_y + dy

            # 상근이 탈출 가능
            if nx >= h or nx < 0 or ny >= w or ny < 0: return current_time + 1

            # 이미 building 그리드 안에 있는 애들만 여기로 넘어오니까 조건 굳이 안 쓰겠음
            if (nx, ny) not in s_visited and building[nx][ny] == '.' and fire_time[nx][ny] > current_time + 1: # 해당 자리에 불이 오는 시간이 이 다음 상근이 위치보다 커야 함
                sanggeun_queue.append((nx, ny, current_time + 1))
                s_visited.add((nx, ny))

    return False
                

T = int(input())
for _ in range(T):
    w, h = map(int, input().split()) # w, h는 최대 1000

    # input 이중 리스트로 정리하기
    building = [] # buildling 정보 초기화
    for _ in range(h): # 높이 h를 돌면서
        h_elem = []
        h_elems = input() # input 받고
        for elem in h_elems: # 하나씩 돌면서 h_elem에 초가
            h_elem.append(elem)
        building.append(h_elem) # 다 돌면 h_elem을 buildling에 추가
    
    s_queue = deque() # 불 리스트
    f_queue = deque() # 상근이 bfs
    fire_time = [[float('inf')] * w for _ in range(h)] # 불이 번지는 시간 리스트
    s_visited = set()
    f_visited = set()

    # 상근이랑 불 찾으러 갑시다
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@': 
                s_queue.append((i, j, 0))
                s_visited.add((i, j))

            elif building[i][j] == '*': 
                f_queue.append((i, j, 0)) # x좌표, y좌표, 시간
                f_visited.add((i, j)) # 방문했다는 것을 체크 미리해주기
                fire_time[i][j] = 0 # 이렇게 해두 대나?


    fire(f_queue) # 불 시간 기록하고
    escape_time = save_sanggeun(s_queue) # 상근이의 탈출 시간 찾기

    if escape_time: print(escape_time)
    else: print('IMPOSSIBLE')