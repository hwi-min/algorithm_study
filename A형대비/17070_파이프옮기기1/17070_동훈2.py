dy = [0,1,1]
dx = [1,1,0]

# 정방행렬의 크기
N = int(input())
# 집 구조
house = [list(map(int, input().split())) for _ in range(N)]
# 값 저장할 dp
dp = [[[0] * N for _ in range(N)] for _ in range(3)]
# 초기값 설정
dp[0][0][1] = 1

# 반복문으로 테이블 채우기 (초기 파이프가 (0,1)까지 차지하므로 (0,2)부터 시작)
for r in range(N):
    for c in range(2, N):
        # 벽이 아니면 점화식에 따라 dp 테이블 채우기
        if house[r][c] == 0:
            # A. 가로 파이프
            dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]
            
            # B. 세로 파이프
            if r > 0: # r=0일 때는 세로로 올 수 없음
                dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]
            
            # C. 대각선 파이프 (벽 3개 체크 필수)
            if r > 0 and house[r-1][c] == 0 and house[r][c-1] == 0:
                dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

print(dp[0][N-1][N-1] + dp[1][N-1][N-1] + dp[2][N-1][N-1])

