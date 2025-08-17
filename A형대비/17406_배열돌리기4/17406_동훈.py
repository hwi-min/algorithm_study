from itertools import permutations
import copy

def rotate_matrixt(matrix, r, c, s):
    '''
        회전연산 (r-s, c-s) ~ (r+s, c+s)
        여기선 1,1이 시작지점이기 때문에 r-s-1, c-s-1로 idx 조정해주어야 함.
        s만큼 반복문을 돌며 진행
    '''
    
    for idx in range(s):
        lefttop = matrix[r-s-1+idx][c-s-1+idx]
        
        # 회전할 배열의 lefttop 바로 아래 좌표
        ny , nx = r-s-1+idx, c-s-1+idx
        # 총 네개의 while문 돌기
        # 아래로 이동
        while ny < (r+s-1-idx):
            matrix[ny][nx] = matrix[ny+1][nx]
            ny += 1
        # 오른쪽으로 이동
        while nx < (c+s-1-idx):
            matrix[ny][nx] = matrix[ny][nx+1]
            nx += 1
        # 위로 이동
        while ny > (r-s-1+idx):
            matrix[ny][nx] = matrix[ny-1][nx]
            ny -= 1
        # 왼쪽으로 이동
        while nx > (c-s-1+idx):
            matrix[ny][nx] = matrix[ny][nx-1]
            nx -= 1
        matrix[r-s-1+idx][c-s-1+idx + 1] = lefttop
        


# 배열 크기 N, M 회전 연산의 개수 K
N, M, K = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
# 연산 저장 (r, c, s)
rotate_operatior = [list(map(int, input().split())) for _ in range(K)]

min_sum = float('inf')

for perm in permutations(range(K), K):    
    copy_mat = copy.deepcopy(matrix)
    # 가능한 순열 순서대로 배열 회전 수행
    for i in perm:
        rotate_matrixt(copy_mat, rotate_operatior[i][0], rotate_operatior[i][1], rotate_operatior[i][2])
    
    for row in copy_mat:
        min_sum = min(min_sum, sum(row))
        
print(min_sum)