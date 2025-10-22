n = int(input())
children = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(n): # 증가하는 순열?? 그거 최대 값 찾고 나머지 옮기기
    dp[children[i]] = dp[children[i] - 1] + 1

answer = n - max(dp)
print(answer)