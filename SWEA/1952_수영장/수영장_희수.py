def dfs(month_idx, current_cost):
    global min_cost #최소 가격 저장할 변수

    if month_idx >= 12 : # month_idx : 0 ~ 11
        min_cost = min(min_cost, current_cost)
        return

    dfs(12, year) # 1년 요금
    dfs(month_idx + 3, current_cost + three_month) # 3개월 요금
    dfs(month_idx + 1, current_cost + one_month) # 1개월 요금
    dfs(month_idx + 1, current_cost + day * plans[month_idx]) # 1일 요금으로 한 달치

t = int(input())
for tc in range(1, t+1) :
    day, one_month, three_month, year = map(int, input().split())
    plans = list(map(int, input().split()))
    min_cost = day * 365 # 최대 값 저장

    dfs(0, 0)
    print(f'#{tc} {min_cost}')
