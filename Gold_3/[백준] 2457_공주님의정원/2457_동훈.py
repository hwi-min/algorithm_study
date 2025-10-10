N = int(input())
flower = [list(map(int, input().split())) for _ in range(N)]

# 1️⃣ 피는날 → 2️⃣ 지는날 기준으로 정렬
flower.sort(key=lambda x: (x[0], x[1], x[2], x[3]))

front_month, front_day = 3, 1
back_month, back_day = 11, 30

answer = 0
max_end = (0, 0)  # 가장 늦게 지는 꽃의 (month, day)
idx = 0
found = False

while (front_month < back_month) or (front_month == back_month and front_day <= back_day):
    updated = False

    # 현재 front 기준에서 피어있는 꽃들 중 가장 늦게 지는 꽃 찾기
    while idx < N:
        s_month, s_day, e_month, e_day = flower[idx]

        # 아직 피지 않은 꽃이면 break
        if (s_month > front_month) or (s_month == front_month and s_day > front_day):
            break

        # front 시점에 이미 피어 있는 꽃이면, 가장 늦게 지는 후보로 갱신
        if (e_month > max_end[0]) or (e_month == max_end[0] and e_day > max_end[1]):
            max_end = (e_month, e_day)
            updated = True

        idx += 1

    # 현재 front 시점에 피어 있는 꽃이 없으면 중단 (공백 발생)
    if not updated:
        found = False
        break

    # 선택한 꽃을 결과에 추가하고, front를 갱신
    answer += 1
    front_month, front_day = max_end

    # 11/30 이후까지 덮었으면 성공
    if (front_month > back_month) or (front_month == back_month and front_day > back_day):
        found = True
        break

# 출력
print(answer if found else 0)