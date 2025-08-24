def square(row,col):
    global answer
    if row + 1 < N and col + 1 < M:
        prefix_sum = paper[row][col] + paper[row][col+1] + paper[row+1][col] + paper[row+1][col+1]
        answer = max(answer, prefix_sum)


def stick(row, col):
    global answer
    # 가로 막대를 놓을 공간이 있는지 독립적으로 확인
    if col + 3 < M:
        prefix_sum = paper[row][col] + paper[row][col+1] + paper[row][col+2] + paper[row][col+3]
        answer = max(answer, prefix_sum)
    # 세로 막대를 놓을 공간이 있는지 독립적으로 확인
    if row + 3 < N:
        prefix_sum = paper[row][col] + paper[row+1][col] + paper[row+2][col] + paper[row+3][col]
        answer = max(answer, prefix_sum)


def fxxx(row, col):
    global answer
    # 'ㅏ', 'ㅓ' 모양 (세로가 긴 3x2 공간 필요)
    if row + 2 < N and col + 1 < M:
        # 'ㅏ' 모양
        s1 = paper[row][col] + paper[row+1][col] + paper[row+2][col] + paper[row+1][col+1]
        # 'ㅓ' 모양
        s2 = paper[row][col+1] + paper[row+1][col+1] + paper[row+2][col+1] + paper[row+1][col]
        answer = max(answer, s1, s2)
        
    # 'ㅗ', 'ㅜ' 모양 (가로가 긴 2x3 공간 필요)
    if row + 1 < N and col + 2 < M:
        # 'ㅜ' 모양
        s3 = paper[row][col] + paper[row][col+1] + paper[row][col+2] + paper[row+1][col+1]
        # 'ㅗ' 모양
        s4 = paper[row+1][col] + paper[row+1][col+1] + paper[row+1][col+2] + paper[row][col+1]
        answer = max(answer, s3, s4)

def s_shape(row,col):
    global answer
    global answer
    # 세워진 'S', 'Z' 모양 (3x2 공간 필요)
    if row + 2 < N and col + 1 < M:
        # S 모양
        s1 = paper[row][col+1] + paper[row+1][col+1] + paper[row+1][col] + paper[row+2][col]
        # Z 모양 (S의 대칭)
        s2 = paper[row][col] + paper[row+1][col] + paper[row+1][col+1] + paper[row+2][col+1]
        answer = max(answer, s1, s2)

    # 누운 'S', 'Z' 모양 (2x3 공간 필요)
    if row + 1 < N and col + 2 < M:
        # S 모양
        s3 = paper[row][col] + paper[row][col+1] + paper[row+1][col+1] + paper[row+1][col+2]
        # Z 모양 (S의 대칭)
        s4 = paper[row+1][col] + paper[row+1][col+1] + paper[row][col+1] + paper[row][col+2]
        answer = max(answer, s3, s4)

def l_shape(row, col):
    global answer
    # 세로가 긴 모양들 (3x2 공간 필요)
    if row + 2 < N and col + 1 < M:
        # L 모양 4가지
        s1 = paper[row][col] + paper[row+1][col] + paper[row+2][col] + paper[row+2][col+1]
        s2 = paper[row][col+1] + paper[row+1][col+1] + paper[row+2][col+1] + paper[row+2][col]
        s3 = paper[row][col] + paper[row][col+1] + paper[row+1][col+1] + paper[row+2][col+1]
        s4 = paper[row][col] + paper[row+1][col] + paper[row+2][col] + paper[row][col+1]
        answer = max(answer, s1, s2, s3, s4)
    
    # 가로가 긴 모양들 (2x3 공간 필요)
    if row + 1 < N and col + 2 < M:
        # L 모양 4가지
        s5 = paper[row][col] + paper[row+1][col] + paper[row+1][col+1] + paper[row+1][col+2]
        s6 = paper[row][col] + paper[row][col+1] + paper[row][col+2] + paper[row+1][col+2]
        s7 = paper[row][col+2] + paper[row+1][col] + paper[row+1][col+1] + paper[row+1][col+2]
        s8 = paper[row][col] + paper[row+1][col] + paper[row][col+1] + paper[row][col+2]
        answer = max(answer, s5, s6, s7, s8)
        
        
def tetromino(N, M):
    '''
        500 x 500 x 19번 = 5,000,000번 이하 -> 완탐 가능
        모든 가능한 시작점에서 19개의 경우를 다 돌려본다
    '''
    for row in range(N):
        for col in range(M):
            # 다섯가지 모양의 함수 호출
            square(row, col)
            stick(row,col)
            fxxx(row,col)
            s_shape(row,col)
            l_shape(row,col)
    

# 종이의 세로 크기 N, 가로 크기 M
N, M = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(N)]

answer = 0
tetromino(N,M)
print(answer)