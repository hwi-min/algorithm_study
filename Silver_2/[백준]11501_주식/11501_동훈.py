t = int(input())

for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    profit = 0
    
    max_value = price[-1]
    for i in range(n-2, -1, -1):
        if price[i] <= max_value:
            profit += max_value - price[i]
        else:
            max_value = price[i]
    print(profit)