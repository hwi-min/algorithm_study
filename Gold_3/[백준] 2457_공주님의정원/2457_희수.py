n = int(input())
days = [((a * 100) + b, (c * 100) + d) for a, b, c, d in (map(int, input().split()) for _ in range(n))]
days.sort()
# print(days)
flower_count = 0
start_point = 301
end_point = 0
yes = False

if days[0][0] <= 301:
    flower_count += 1

    for day in days:
        start, end = day

        if start <= start_point:
            end_point = max(end_point, end)
            # print(end_point)

        else:
            # print(end_point)
            start_point = end_point
            if start <= start_point:
                flower_count += 1
                end_point = max(end_point, end)

        if end_point > 1130:
            yes = True
            break

if yes:
    print(flower_count)
else:
    print(0)
