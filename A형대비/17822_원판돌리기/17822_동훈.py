from collections import deque

# N 반지름의 크기, M 정수의 개수, T 회전 횟수
N, M, T = map(int, input().split())

# 원판들
circles = [deque(map(int, input().split())) for _ in range(N)]

# 회전정보
rotate_info = [list(map(int, input().split())) for _ in range(T)]

# x 배수, d 회전 방향, k 돌리는 정도
for x, d, k in rotate_info:
    if d == 0 : d = 1
    elif d == 1 : d = -1
    
    for idx in range(N):
        # x의 배수이면 주어진 방향으로 rotate
        if (idx + 1) % x == 0:
            circles[idx].rotate(d*k)
    
    # 지울 인덱스 저장
    erase_list = set()
    
    # 원판에 수가 남아있으면, 인접하면서 수가 같은것을 찾음
    for circle in circles:
        if sum(list(circle)) > 0:
            for row in range(N):
                for col in range(M):
                    if circles[row][col] == 0: continue
                    # 인접한지 확인
                    # 양옆
                    if circles[row][col] == circles[row][(col-1)%M] or circles[row][col] == circles[row][(col+1)%M]:
                        erase_list.add((row,col))
                    #위 아래 (첫번째 마지막 뺴고)
                    if 0 < row < N-1:
                        if circles[row][col] == circles[(row+1)%N][col] or circles[row][col] == circles[(row-1)%N][col]:
                            erase_list.add((row,col))
                    elif row == 0:
                        if circles[row][col] == circles[(row+1)%N][col]:
                            erase_list.add((row,col))
                    elif row == N-1:
                        if circles[row][col] == circles[(row-1)%N][col]:
                            erase_list.add((row,col))

    # 지울거 지움
    for row, col in erase_list:
        circles[row][col] = 0
        
    # 인접하면서 수가 같은 것이 없는지 확인
    if not erase_list:
        total_sum, total_count = 0, 0

        # 1. 모든 원판을 순회하며 총합과 개수 계산
        for r in range(N):
            for c in range(M):
                if circles[r][c] > 0:
                    total_sum += circles[r][c]
                    total_count += 1

        # 2. 평균을 계산 (0으로 나누는 오류 방지)
        if total_count > 0: average = total_sum / total_count
            
        # 3. 평균과 비교하여 값 조정
        for r in range(N):
            for c in range(M):
                if circles[r][c] > 0:
                    if circles[r][c] < average: circles[r][c] += 1
                    elif circles[r][c] > average: circles[r][c] -= 1
                        
answer = 0
for i in range(N):
    for j in range(M):
        answer += circles[i][j]
        
print(answer)