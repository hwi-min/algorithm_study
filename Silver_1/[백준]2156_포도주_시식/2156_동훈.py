'''
    1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야하고 원래 위치에 놓기
    2. 연속으로 놓여 있는 세잔을 모두 마실순 없다.
    
    dp[idx][0] = idx번째 포도주를 안마셨을때 최댓값
    dp[idx][1] = idx번째 포도주만 마셨을때 최댓값
    dp[idx][2] = 이전거 + 마셨을때 최댓값
    
    
'''

n = int(input())
grape = [int(input()) for _ in range(n)]
dp = [[0] * 3 for _ in range(n+1)]

for i in range(1, n+1):
    # 이전거 에서 맥스
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    # 이번거 먹으려면 이전단계에서 2개 먹으면 안됨
    dp[i][1] = dp[i-1][0] + grape[i-1]
    # 이전거 하나 먹음 고려
    dp[i][2] = dp[i-1][1] + grape[i-1]

print(max(dp[n]))