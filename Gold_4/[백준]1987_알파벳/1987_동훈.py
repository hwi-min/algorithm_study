'''
    세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다.
    보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단에는 (1,1)
    말이 놓여 있다.
    
    말은 인접한 네 칸 중의 한 칸으로 이동 가능함.
    새로 이동한 칸에 적혀있는 알파벳은 지금까지 지나온 모든 칸에
    적혀 잇는 알파벳과는 달라야 한다.
    
    말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램
'''

'''
    최대 20 x 20 보드판
'''
'''
    copy에서 시간초과
'''
from collections import deque

dr = [(-1,0),(1,0),(0,-1),(0,1)]
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

visited_alpha = [False] * 26 # 알파벳 방문 배열
total = 1

def dfs(r,c,cnt):
    global total
    
    total = max(total, cnt)
        
    for i in range(4):
        nr, nc = r + dr[i][0], c + dr[i][1]
        if 0 <= nr < R and 0 <= nc < C:
            # 방문하지 않은 알파벳이면
            if not visited_alpha[ord(board[nr][nc])-ord('A')]:
                # 방문처리 하고 dfs 호출
                visited_alpha[ord(board[nr][nc])-ord('A')] = True
                dfs(nr, nc, cnt+1)
                # 백트래킹
                visited_alpha[ord(board[nr][nc])-ord('A')] = False
            
visited_alpha[ord(board[0][0])-ord('A')] = True
dfs(0,0,1)
print(total)