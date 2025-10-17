n = int(input())
days = [((a * 100) + b, (c * 100) + d) for a, b, c, d in (map(int, input().split()) for _ in range(n))]
# [(시작월일 : 0000, 종료월일 : 0000)] 형식으로 저장
days.sort() # 시작일 기준 오름차순으로 정렬
# print(days)
flower_count = 0 # 꽃 개수 셀 거
start_point = 301 # 시작 날짜 3월 1일
end_point = 0
yes = False

if days[0][0] <= 301: # 가장 빠른 시작일이 3월 1일 이전인 경우에만
    flower_count += 1 # 가장 빠른 시작일 꽃 하나 세고 시작

    for day in days:
        start, end = day # 시작일 0000, 종료일 0000

        if start <= start_point: # 시작일이 시작 포인트보다 작으면 
            end_point = max(end_point, end) # 엔드 포인트 최대값으로 업데이트
            # print(end_point)

        else: # 시작일이 시작 포인트보다 크면
            # print(end_point)
            start_point = end_point # 시작일 업데이트 (새로운 꽃 뽑았다는 뜻)
            if start <= start_point: # 이제 다시 시작 포인트보다 시작일이 작으면
                flower_count += 1 # 꽃 개수 하나 추가
                end_point = max(end_point, end) # 엔드 포인트 최대값으로 업데이트

        if end_point > 1130: # 만약 꽃 종료일이 11월 30일 이후이면
            yes = True # 예스 트루
            break

if yes: # 예스 트루면
    print(flower_count)
else: # 아니면
    print(0)
