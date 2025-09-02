'''
    N x N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있음
    아기상어와 물고기는 모두 자연수의 크기를 가진다.

    가장 처음에 상어는 2의 크기를 가지고 아기상어는
    1초에 상하좌우로 인접한 한 칸씩 이동한다.

    자신보다 큰 물고기가 있는 칸은 지나갈 수 없다.
    자신보다 작은 물고기만 먹을 수 있다.
    크기가 같은 물고기는 먹을 순 없지만, 지나갈 순 있다.

    상어의 이동방법은 다음과 같다.
    - 더 이상 먹을 수 있는 물고기가 없다면 엄마에게 도움을 요청함
    - 먹을 수 있는 물고기가 1마리라면 그 물고기를 먹으러 감
    - 1개 이상이라면 거리가 가장 가까운 물고기를 먹으러 감.
        - 거리가 가까운 물고기가 여러개라면, 가장 위, 좌측에 있는 물고기를 먹는다.
    
    아기상어는 자신의 크기 만큼의 물고기를 먹을 때 크기가 1 증가함.
    초기 상태에선 2마리를 먹으면 1증가해 3이 됨.

    -> 공간의 상태가 주어졌을 때, 아기상어가 몇 초 동안 도움을 요청하지 않는지 리턴

    공간의 상태:
        0: 빈 칸
        1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
        9: 아기 상어의 위치
'''

'''
    도움을 요청 할 조건 -> 더 이상 먹을 수 있는 물고기가 없을때
    즉, 공간안에 내 몸 보다 작은 물고기가 없을때.

    초기의 상어 상태는 2이다.
    공간에서 빈칸이 아닌 모든 좌표들을 찾고 물고기의 크기와 좌표값을 저장함.
    물고기의 크기 순으로 정렬해서 현재 상어의 크기와 작으면 먹으러 이동함.
    먹으면서 상어의 크기를 증가시키며 진행하다가 더 이상 먹을 수 없으면 종료

    heap으로 공간 상태를 관리함. (크기, 행, 열)로 관리하면 자동으로 다음 먹이가 주어짐

    이동 방법?
    가장 최단거리로 이동함. 상어는 자기보다 큰 물고기를 만나면 돌아가야 함.
'''
import heapq
import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def baby_shark_move(row, col, shark_row, shark_col, cur_time):
    '''
        bfs를 사용하여 이동
    '''
    queue = deque()

    if shark_row == row and shark_col == col: # 물고기 만나면 break
        choidan_distance = min(choidan_distance, cur_time)
        return

    for i in range(4):
        ny, nx = shark_row + dy[i], shark_col + dx[i]
        if 0 <= ny < N and 0 <= ny < N:
            if grid[ny][nx] <= baby_shark[0][0]: # 아기상어보다 작거나 같으면
                baby_shark_move(row, col, ny, nx, cur_time+1)

# 공간의 크기 N
N = int(input())

# 공간의 상태
grid = [list(map(int, input().split())) for _ in range(N)]

heap = []
baby_shark = []
eat_count = 0
timer = 0

for i in range(N):
    for j in range(N):
        if grid[i][j] != 0 and grid[i][j] != 9: # 물고기를 만나면 (크기, 행, 열) 순으로 기록함.
            heapq.heappush(heap, (grid[i][j], i, j))
        elif grid[i][j] == 9: # 아기상어 만남
            baby_shark.append((2,i,j))

while heap:
    size, row, col = heapq.heappop(heap) # 가장 작고 좌상단에 있는 물고기

    print(size, baby_shark)
    if size > baby_shark[0][0]: # 현재 가장 작은 물고기가 상어보다 크면 종료
        break
    
    choidan_distance = float('inf') # 최단거리
    # 상어 이동 로직 함수로 이동 거리 구함.
    baby_shark_move(row, col, baby_shark[0][1], baby_shark[0][2], 0)
    # dfs 완료하면 하나 먹은거
    eat_count += 1
    # 최단거리 만큼 시간 초 추가
    timer += choidan_distance
    # 상어 몸 만큼 먹으면 상어 크기 증가, eat횟수 초기화
    if eat_count == baby_shark[0][0]: baby_shark[0][0] += 1; eat_count = 0
    # 다시 다음 물고기로 이동.

print(timer)