def dfs(month_idx, current_cost):
    global min_cost

    if month_idx >= 12 :
        min_cost = min(min_cost, current_cost)
        return

    dfs(12, year)
    dfs(month_idx + 3, current_cost + three_month)
    dfs(month_idx + 1, current_cost + one_month)
    dfs(month_idx + 1, current_cost + day * plans[month_idx])

t = int(input())
for tc in range(1, t+1) :
    day, one_month, three_month, year = map(int, input().split())
    plans = list(map(int, input().split()))
    min_cost = 10 * 365

    dfs(0, 0)
    print(f'#{tc} {min_cost}')
