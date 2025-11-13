n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort(key=lambda x : (x[0], -x[1]))
cnt = 1
ends = ([times[0][1]])

for i in range(1, n):
    checked = False
    s, e = times[i]
    ends.sort()
    for j in range(cnt):
        if ends[j] <= s:
            ends[j] = e
            checked = True
            break

    if not checked:
        cnt += 1
        ends.append(e)

print(cnt)