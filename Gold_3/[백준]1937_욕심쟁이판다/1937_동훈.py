'''
    판다는 대나무를 먹기 시작하는데 그 지역의 대나무를 다 먹으면
    상하좌우중 한 곳으로 이동해서 대나무를 먹음
    
    욕심이 매우 많기 때문에 대나무를 먹고 자리를 옮길 때,
    전에 위치했던 지역보다 대나무가 많이 있어야 함.
    
    이런 판다를 대나무 숲에 풀어 놓아햐 하는데,
    어떤 지점에 처음 풀어 놓아햐 하고, 어떤 곳으로 이동을 시켜야
    최대한 많은 칸을 방문할 수 있는지
    
    즉 n x n의 대나무 숲이 주어질 때, 판다가 최대한 많은 칸을 이동하려면
    어떠한 경로를 통하여 움직여야 하는지 구하시오
'''

'''
    n은 최대 500개
    시작지점 2500개
    2500개의 시작지점에서 다익스트라 수행
'''

'''
    해당 칸에 도달 할 때 최대 값을 저장함.
    최댓값이 갱신되면 그 지점에서 다시 탐색함.
    
    해당 위치의 도착했을 때 지나온 총 지역 개수를 distance에 저장함.
    
    r,c의 위치에서 출발 했을 때의 거리를 이미 계산했다면
    그냥 그거 더하면 됨
'''
import sys
sys.setrecursionlimit(10**6)

n = int(input())
woods = list(list(map(int, input().split())) for _ in range(n))
distance = [[0] * n for _ in range(n)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(r, c):
    if distance[r][c] != 0:
        return distance[r][c] # 이미 계산한 값은 그대로 사용함.

    distance[r][c] = 1  # for문 안 돌아가는 경우 : 갈 수 없는 곳은 1칸으로 리턴하기 위해 
    
    for i in range(4):
        nr, nc = r + dy[i], c + dx[i]
        if 0 <= nr < n and 0 <= nc < n:
            if woods[nr][nc] > woods[r][c]:
                # 끝까지 갔다가 역순으로 하나씩 더하며 현재 위치에서 최대 방문할 수 있는 지역 저장
                distance[r][c] = max(distance[r][c], dfs(nr, nc) + 1) 
    return distance[r][c]
    
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
print(ans)