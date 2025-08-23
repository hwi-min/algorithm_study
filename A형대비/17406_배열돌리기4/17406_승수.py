# 배열 A의 값 = 각 행에 있는 모든 수의 합 중 최솟값
# 회전 연산 (r, c, s)
# r: 행 값, c: 열 값, s: 회전하고자 하는 배열 범위

# 회전 연산을 수행하였을 때, 배열 A의 값의 최솟값 구하기
from itertools import permutations


def rotate_calc(start_row, start_col, rotate_range):
    # 주어진 조건에 의해 배열 밖으로 나갈 일은 없음
    # 따라서 idx 검사 할 필요 X
    for i in range(1, rotate_range + 1):
        nrow = start_row - i    # 시작 위치의 왼쪽 끝부터 시작
        ncol = start_col
        temp = 0
        for _ in range(i):  # 위로 올라가면서 값 바꾸기
            nrow -= 1
            temp = A[nrow][ncol]
            A[nrow][ncol] = A[nrow + 1][ncol]
        ncol += 1
        A[nrow][ncol] = temp

        for _ in range(i*2 - 1):
            ncol += 1
            temp =



# N: 배열 A의 행 수, M: 배열 A의 열 수, K: 회전 연산의 개수
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

for _ in range(K):  # 회전 연산의 개수만큼 반복
    r, c, s = map(int, input().split())
    minimum_res = 100 * M   # 가능한 최댓값으로 초기화

    for perm in permutations(range(K), K):
        rotate_calc(r, c, s)   # 회전 연산 수행

    # 회전 연산 후 각 행의 합을 계산하며 최솟값 갱신
    for row in A:
        minimum_res = min(minimum_res, sum(row)) # 최솟값 갱신

print(minimum_res)
