'''
    크기가 NxM인 지도가 존재
    가장 왼쪽 위에 있는 칸의 좌표는 (1,1)이고,
    오른쪽 아래에 있는 좌표는 (N,M)이다.
    
    주사위의 각 면에는 1보다 크거나 같고, 6보다 작거나 같은 정수가 있다.
    
    주사위는 지도 위에 윗 면이 1이고, 동쪽으로 바라보는 방향이 3인 상태로
    놓여져 있고, 가장 처음에 주사위의 이동 방향은 동쪽이다.
    다음은 주사위의 이동 방식이다.
    
    1. 주사위가 이동 방향으로 굴러가는데, 그 방향으로 갈 수 없다면
    반대로 한 칸 굴러감
    2. 주사위가 도착한 칸에 대한 점수를 획득함
    3. 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸의 정수 B
    를 비교해 이동 방향을 결정함
    A > B인 경우 이동 방향을 90도 시계방향으로 회전
    A < B인 경우 이동 방향을 90도 반시계방향으로 회전
    A = B인 경우 이동 방향에 변화는 없음.
    
    (x,y)에 있는 정수를 B라고 했을 때, (x,y)에서 동서남북
    방향으로 연속해서 이동할 수 있는 칸의 수 C를 모두 구함.
    
    주사위 이동 규칙으로 1,1 에서 K번 만큼 주사위를 이동한 후
    그 위치에 있는 정수와 주변에 연결된 같은 정수를 가진 칸 수를
    곱한 것이 점수
    
    동서남북 네 방향으로 이동하면 주사위의 숫자가 어떻게 바뀌는지
    K번이 주어지면 각 이동 횟수에서 주어진 점수를 모두 더해야 함.
'''

'''
    K번 반복하며 해당 숫자가 이미 도달했던 숫자면 사용하고
    그렇지 않으면 bfs로 칸수 계산해서 table에 저장함.
'''
from collections import deque

N,M,K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
table = [[0] * M for _ in range(N)]
# 위, 아래, 동, 서, 남, 북에 적혀있는 숫자
# 0,  1,  2,  3, 4,  5
dice = [1,6,3,4,2,5]
last_pos = [0,0]
# 동 남 서 북
dr = [(0,1),(1,0),(0,-1),(-1,0)]
# 동 남 서 북의 반대
# 서 북 동 남
op_dr = [2,3,0,1]
ans = 0
# 동, 남, 서, 북
# 0, 1, 2, 3
now_dr = 0

def bfs(r,c,num) -> int:
    '''
    row,col,숫자가 주어지면 해당 좌표에서 인접한 같은 숫자의 칸을 리턴함
    '''
    total = 1
    q = deque()
    q.append((r,c))
    visited = set()
    visited.add((r,c))
    while q:
        row,col = q.popleft()
        for i in range(4):
            nr,nc = row+dr[i][0], col+dr[i][1]
            if 0<=nr<N and 0<=nc<M and grid[nr][nc] == num and (nr,nc) not in visited:
                q.append((nr,nc))
                visited.add((nr,nc))
                total += 1
    for row, col in visited:
        table[row][col] = total * num
    
            
for _ in range(K):
    # K번 만큼 주사위를 굴려서 점수를 구함.
    
    # 현재 방향으로 이동 가능하면 이동
    # 아니면 이동 방향의 반대로 가야함.
    if 0 <=last_pos[0]+dr[now_dr][0]< N and 0<=last_pos[1]+dr[now_dr][1]<M:
        last_pos[0], last_pos[1] = last_pos[0] + dr[now_dr][0], last_pos[1] + dr[now_dr][1]
    else:
        now_dr = op_dr[now_dr]
        last_pos[0], last_pos[1] = last_pos[0] + dr[now_dr][0], last_pos[1] + dr[now_dr][1]
        
    # 주사위 상태 변경
    if now_dr == 0:  # 동쪽
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
    elif now_dr == 2:  # 서쪽
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
    elif now_dr == 1:  # 남쪽
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
    elif now_dr == 3:  # 북쪽
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
        
    # 현재 위치의 점수를 계산
    if table[last_pos[0]][last_pos[1]] != 0:
        ans += table[last_pos[0]][last_pos[1]]
    else:
        bfs(last_pos[0],last_pos[1],grid[last_pos[0]][last_pos[1]])
        ans += table[last_pos[0]][last_pos[1]]
    
    # 주사위 굴린 후 다음 방향을 정함.
    if dice[1] > grid[last_pos[0]][last_pos[1]]:
        # 현재 방향에서 오른쪽으로
        now_dr = (now_dr + 1) % 4
    elif dice[1] < grid[last_pos[0]][last_pos[1]]:
        # 현재 방향에서 왼쪽으로
        if now_dr - 1 < 0:
            now_dr = 3
        else:
            now_dr = (now_dr - 1) % 4
    
print(ans)