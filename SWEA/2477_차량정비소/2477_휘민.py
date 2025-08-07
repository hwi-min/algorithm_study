import sys
sys.stdin = open('./sample_input.txt')

from collections import deque

T = int(input())
for t in range(1, T+1):
    # 접수창구개수, 정비창구개수, 방문고객수, 지갑을 두고간 고객이 이용한 접수 창고, 정비 창고
    N, M, K, A, B = map(int, input().split())
    a_times = list(map(int, input().split())) # 접수 창구가 접수하는데 리는 시간
    b_times = list(map(int, input().split())) # 정비 창구가 접수하는데 걸리는 시간
    arrivals = list(map(int, input().split())) # 고객이 도착시간 (K명)

    # 상태
    reception = [None] * N # 접수 창구 상태: (고객번호, 남은시간)
    repair = [None] * M # 정비 창구 상태: (고객번호, 남은시간)

    reception_wait = deque() # 접수 대기열 (고객 번호 저장)
    repair_wait = [] # 정비 대기열: (접수 완료 시간, 접수창고번호, 고객번호)

    # 각 고객이 사용한 접수/정비 창구 번호 기록
    reception_used = [0] * (K+1) # [고객번호] -> 접수 창구 번호
    repair_used = [0] * (K+1) # [고객번호] -> 정비 창구 번호

    # 시뮬레이션 시간
    time = 0
    # 정비까지 완료한 고객 수
    done_count = 0
    # 접수 대기열에 들어온 고객 수
    arrived_count = 0

    # 모든 고객이 정비를 끝낼 때까지 시뮬레이션
    while done_count < K:
        # 1. 현재 시간 도착 고객 접수 대기열에 추가
        for idx in range(K):
            if arrivals[idx] == time: # 도착시간이 현재 시간과 같은 고개만 추가
                reception_wait.append(idx+1) # 고객번호는 1-based 이니까
                arrived_count += 1 # 접수 대기열에 들어온 고객 수 + 1

        # 2. 접수 창구 처리 중인 고객 남은 시간 감소
        for i in range(N): # 접수창구 개수만큼 순회
            if reception[i]: # 해당 접수창구의 reception 정보가 존재하면
                cust, remain = reception[i] # 접수창구에 있는 (고객번호, 남은시간) 가져옴
                remain -= 1 # 남은 시간 -1
                if remain == 0: # 만약 남은 시간이 0이라면
                    # 접수 완료 -> 정비 대기
                    # 정비 대기열에 (완료된 현재시간, 1-based이므로 접수창고번호+1, 고객번호)
                    repair_wait.append((time, i+1, cust))
                    reception[i] = None # 접수 창구 비우기
                else:
                    reception[i] = (cust, remain)

        # 3. 정비 창구 처리 중인 고객의 남은 시간 감소
        for j in range(M):
            if repair[j]: # 정비창구에 고객이 있으면
                cust, remain = repair[j]
                remain -= 1
                if remain == 0:
                    # 정비 완료 -> 최종 종료
                    done_count += 1
                    repair[j] = None
                else:
                    repair[j] = (cust, remain)

        # 4. 접수 창구 배정
        # 규칙: (1) 대기 고객번호가 작은 순 -> deque라서 자동 보장
        #       (2) 창구 번호가 작은 순으로 배정 -> for문이 작은 번호부터 순회
        for i in range(N):
            if reception[i] is None and reception_wait:
                cust = reception_wait.popleft() # 대기열에서 고객 꺼내기
                reception_used[cust] = i+1 # 사용한 접수창구 번호 기록 (1-based이므로 +1)
                reception[i] = (cust, a_times[i]) # 처리 시작

        # 5. 정비 창구 배정
        # 규칙: (1) 먼저 기다린 순 -> 완료시간이 작은 순
        #       (2) 접수창구 번호가 작은 순
        if repair_wait:
            repair_wait.sort(key=lambda x: (x[0], x[1])) # 우선순위 정렬: 먼저 완료된 순서(x[0]) -> 접수 창고 번호(x[1]) 순으로 정렬
        for j in range(M):
            if repair[j] is None and repair_wait: # repair[j]가 비어있고, 대기고객이 있으면 ...
                _, rec_num, cust = repair_wait.pop(0) # 대기열에서 하나 꺼내기 : (접수 완료 시간, 접수창고번호, 고객번호)
                repair_used[cust] = j+1 # 사용한 정비창구 번호 기록
                repair[j] = (cust, b_times[j]) # 처리 시작

        # 다음 시간대로 이동
        time += 1

    # 6. 결과 계산
    # - 지갑 분실 고객과 같은 접수창구(A) 정비창구(B) 사용한 고객 찾기
    answer = [idx for idx in range(1, K+1) if reception_used[idx] == A and repair_used[idx] == B]
    result = sum(answer) if answer else -1
    print(f"#{t} {result}")
