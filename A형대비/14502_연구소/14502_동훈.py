'''
    N x M인 직사가형의 연구소
    바이러스 - 2, 벽 - 1, 빈공간 - 0
    바이러스는 상하좌우 인접한 빈 칸으로 퍼저나갈 수 있음
    벽은 총 3개를 세울 수 있다ㅏ.
    벽을 3개 세운 후 바이러스가 퍼질 수 없는 안전 영역의 최대값을 리턴
    모든 조합을 뽑은 후 2가 격리되거나, 빈공간만 남을 수 있으면 최대값 갱신
'''
from itertools import combinations
import copy

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def isolate_virus(arr):
    '''
        매개변수 : 벽을 세울 3개의 좌표
        벽 세웠을때를 가정해서 바이러스 퍼짐을 가정 후 안전공간크기 계산
    '''
    global answer
    test = copy.deepcopy(research)
    # 벽 세우기
    for row, col in arr:
        test[row][col] = 1
    
    visited = [[False] * M for _ in range(N)]
    # 재귀, 현재 위치가 바이러스일때 dfs 호출
    def dfs(row,col,mat):
        # 방문처리 후 바이러스 퍼짐
        visited[row][col] = True
        mat[row][col] = 2
        
        # 상하좌우 이동
        for idx in range(4):
            ny, nx = row + dy[idx], col + dx[idx]
            if 0 <= ny < N and 0 <= nx < M: # 범위 안에 존재
                if visited[ny][nx] == False: # 방문하지 않았고
                    if mat[ny][nx] != 1: # 벽이 아니라면
                        dfs(ny,nx,mat)
    
    # dfs호출
    for i in range(N):
        for j in range(M):
            if test[i][j] == 2 and visited[i][j] == False:
                dfs(i,j,test)
                
    # 안전공간 계산
    safe_area = 0
    for i in range(N):
        safe_area += test[i].count(0)
    if safe_area > answer:
        answer = safe_area
                    
                    
# 연구소의 row, col
# (3 ≤ N, M ≤ 8)
N, M = map(int, input().split())
research = [list(map(int,input().split())) for _ in range(N)]

# 연구소의 빈칸위치를 담을 리스트
arr = []

for i in range(N):
    for j in range(M):
        if research[i][j] == 0:
            arr.append((i,j))

answer = 0
# 모든 조합을 돌림 최대 64개에서 3개뽑음
for comb in combinations(arr,3):
    isolate_virus(comb)
    
print(answer)