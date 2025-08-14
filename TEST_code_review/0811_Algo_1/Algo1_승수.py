def make_thing():
    global max_value
    for i in range(N):  # 모든 물품에 대해서
        for j in range(1, 1 << I):  # 공집합을 제외한 모든 부분집합 탐색
            temp_list = []
            for k in range(I):  # 총 재료의 개수만큼 반복
                if j & (1 << k):    # 현재 요소를 넣을 것인가?
                    temp_list.append(J[k])  # 넣는다
                    if len(temp_list) > M[i][0]: break # 연성에 필요한 물건 개수를 넘으면 그만

            # 연성에 필요한 물건 개수와 현재 들어간 list 의 개수가 같고, 연성에 필요한 시간과 현재 들어간 list 의 시간의 합과 같다면
            if (len(temp_list) == M[i][0]) and (sum(temp_list) == M[i][1]):
                max_value = max(max_value, M[i][2]) # value 갱신


T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # 물품의 종류
    M = [list(map(int, input().split())) for _ in range(N)] # [연성에 필요한 물건 개수, 연성에 필요한 시간, 상품의 가치]
    I = int(input())    # 총 재료의 개수
    J = list(map(int, input().split())) # 재료 별 소요시간
    max_value = 0   # 만들 수 있는 물품의 최대 가치

    make_thing()    # 연성 시작
    print(f'#{tc} {max_value}')