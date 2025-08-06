t = int(input())
for tc in range(1, t+1) :
    k, n, m = map(int, input().split())
    # n : 정류장 개수, k : 한 번 충전으로 가는 양, m : 충전소 개수
    chargers = list(map(int, input().split()))
    # 충전소 정류장 번호들
    now = 0
    # 현재 내 위치
    count = 0
    # 충전 횟수

    chargers.append(n)
    # for문으로 한 번에 돌고 싶기 때문에 종점 n을 정류장(목적지) 목록 맨 뒤에 추가

    for i in range(1, len(chargers)):
        if i > 0 and chargers[i] - chargers[i-1] > k :
            count = 0
            break
        # 충전기 설치 잘못된 경우 0 저장, 탈출

        if now + k < chargers[i]:
            now = chargers[i-1]
            count += 1
        # i번째 충전소까지 갈 여력이 없으면 i-1번째 충전소에서 충전
        # for문 1부터 돌기 때문에 i-1 인덱스 가능
        
    print(f'#{tc} {count}')