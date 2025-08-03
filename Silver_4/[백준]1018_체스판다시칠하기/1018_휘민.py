N, M = map(int, input().strip().split())
board = [input().strip() for _ in range(N)]

'''
- 완전탐색
1. 좌측 최상단이 흰색인 경우
2. 좌측 최상단이 검은색인 경우
'''

min_coloring = float('inf') # inf로 초기화

for i in range(N-7): # 행에서의 8 X 8 시작점  
    for j in range(M-7): # 열에서의 8 X 8 시작점

        recoloring_w = recoloring_b = 0

        for row in range(8):
            for col in range(8):
                current = board[i+row][j+col]

                # 좌상단이 'W'로 시작하는 경우
                if (row + col) % 2 == 0: # 좌상단 색과 동일한 위치
                    if current != 'W': # 좌상단 색과 동일하지 않다면
                        recoloring_w += 1 # 색칠해야 하는 칸 추가
                else: # 좌상단 색과 달라야하는 위치
                    if current != 'B': # 동일하지 않다면
                        recoloring_w += 1 # 색칠해야 하는 칸 추가
                
                # 좌상단이 'B'로 시작하는 경우
                if (row + col) % 2 == 0:
                    if current != 'B':
                        recoloring_b += 1
                else:
                    if current != 'W':
                        recoloring_b += 1

        min_coloring = min(min_coloring, recoloring_b, recoloring_w)

print(f"{min_coloring}")