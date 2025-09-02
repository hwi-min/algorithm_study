'''
    14501 퇴사

    오늘부터 N+1일째 되는 날 퇴사를 하기 위해, 남은 N일 동안 최대한 많은 상담을 하려고 함
    하루에 하나씩 서로 다른 사람의 상담을 잡아 놓음
    각각의 상담은 상담을 완료하는데 걸리는 기간Ti와 상담 시 받을 수 있는 금액 Pi로 이루어짐

    백준이가 얻을 수 있는 최대 수익을 리턴
'''

# N 퇴사 날
N = int(input())

# 1~N번째 날 까지의 상담 일정
consultant = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for day in range(N-1, -1, -1):
    # 역순으로 최대수익을 탐색
    
    # T는 걸리는 날짜, P는 해당 상담의 수익
    T, P = consultant[day][0], consultant[day][1]

    # 상담기간이 남은 날짜보다 길면 pass
    if T > N - day: dp[day] = dp[day+1]; continue
    
    # 상담 수행 가능하면 dp테이블 업데이트
    dp[day] = max(dp[day+T] + P, dp[day+1])

print(dp[0])