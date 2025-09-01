'''
    문제 2 : 나는 랩실의 피카소
    세균들이 종류에 따라 서로 다른 속도로 증식함.
    이 특징으로 그림을 그려보자

    세균의 특징은 다음과 같음
    1. 각 세균은 시작 지점에서 최대로 퍼져 나갈 수 있는 크기가 정해짐.
    2. 본인 자리에서 인접한 상하좌우 방향으로만 증식 가능
    3. 증식하려는 자리에 이미 다른 세균이 존재하면, 증식 불가능
    4. 세균 통(범위)를 벗어날 수 없음
    5. A부터 Z까지 세균이 있을 때, 동일 시간에 퍼진다면 알파벳이 우선순위
    6. 세균의 종류는 항상 A부터 시작하고 건너뛰지 않고 순서대로 사용함.

    베지의 범위와 세균의 최초 배치 정보가 주어짐.
    최종 증식 후 세균이 증식된 모습을 출력
'''

'''
    동일 시간대에서는 우선순위가 존재함 
    -> heapq를 사용해 알파벳별 우선순위대로 튀어나오게 수행함.
    또한 최대 증식 가능 크기가 있으므로 해당 알파벳이 지금까지 얼만큼 증식했는지 기록 필요함.
    -> heapq에 넣을 때, (현재 시간, 알파벳 순서, 알파벳 기호)로 집어넣으면 자동 정렬 가능
    bfs를 이용

    bfs(grid)
    heap에 현재 존재하는 세균 위치 정보 전부 집어 넣음.
    우선순위에 따라 pop된 정보를 기반으로 아래 로직을 수행함.
    while heap{
        상하좌우로 이동함.
        만약 이동 위치가 범위 안 and 다른 세균이 존재하지 않으면
            (시간+1, 알파벳 순서, 알파벳 기호)를 우선순위 큐에 삽입
    }
'''    
import heapq

T = int(input())

# 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def im_piccaso(grid):
    
    while heap:
        curr_time, cell_type, y, x = heapq.heappop(heap)
        
        # 최대 증식 크기 벗어나면 continue
        if curr_time == A[cell_type%65]: continue
        # 상하좌우로 증식
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            # print(ny,nx)
            # 범위 안이면서, 다른 세균이 존재하지 않으면
            if 0 <= ny < row and 0 <= nx < col:
                # print(grid[ny][nx])
                if grid[ny][nx] == '.':
                    grid[ny][nx] = chr(cell_type) # 세균 증식
                    heapq.heappush(heap, (curr_time + 1, cell_type, ny, nx)) # heap에 넣음
    return grid

for tc in range(1,T+1):

    # 베지의 가로크기 col, 세로크기 row
    col, row = map(int, input().split())

    # 세균 종류 K
    K = int(input())

    # 세균 별 최대 증식 가능 크기
    A = list(map(int, input().split()))

    # 배지 정보
    grid = [list(input().split()) for _ in range(row)]

    # for row in grid:
    #     print(row)    

    heap = []
    for i in range(row):
        for j in range(col):
            # 세균 위치 정보 찾음
            if grid[i][j] != '.':
                # 현재 시간, 알파벳 우선 순위, 기호, row, cll
                heapq.heappush(heap, (0, ord(grid[i][j]), i, j))
    
    im_piccaso(grid)
    
    print(f'#{tc}')
    for row in grid:
        print(*row)