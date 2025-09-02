'''
    14501 퇴사

    오늘부터 N+1일째 되는 날 퇴사를 하기 위해, 남은 N일 동안 최대한 많은 상담을 하려고 함
    하루에 하나씩 서로 다른 사람의 상담을 잡아 놓음
    각각의 상담은 상담을 완료하는데 걸리는 기간Ti와 상담 시 받을 수 있는 금액 Pi로 이루어짐

    백준이가 얻을 수 있는 최대 수익을 리턴
'''

'''
    일단 가장 큰 금액을 선택하는게 이득
    하지만, 상담을 못할 가능성이 존재함.

    -> 가장 마지막날 부터 상담을 배치하며 최대 수익을 고려함.
    뒤에서 부터 고려하며 N번째 날의 상담을 고려했을시에 최대수익을 갱신함

    N이 7이라고 가정함
    7일차 상담을 고려함
    - 만약 남은 날짜안에 수행 가능하면 채택
    6일차 상담을 고려함
    - 만약 남은 날짜안에 수행 가능하면
        - 가장 마지막에 선택한 날짜와 겹치는지 확인하고
        - 겹치면 날짜가 겹치지 않을 때 까지 상담을 취소 후 현재 상담을 진행 시 얻게 되는 금액을 비교
        - 겹치지 않으면 상담추가
    5일차 상담고려..
    - 위를 반복함.
'''
# N 퇴사 날
N = int(input())

# 1~N번째 날 까지의 상담 일정
consultant = [list(map(int, input().split())) for _ in range(N)]

# 날짜 기록 배열
days = [-1] * N

# 가장 마지막 날 부터 고려함.
for i in range(N-1, -1, -1):
    # 해당 날짜에 배정된 상담을 N일 안에 완료할 수 있다면
    if consultant[i][0] <= N-i:
        # 이전에 잡았던 상담과 겹치는지 확인함.
        before_job = set()
        conflict_profit = 0
        for day in range(i, i+consultant[i][0]):
            if days[day] != -1:
                before_job.add(days[day])

        # print('현재 날짜', i, '이전 상담들', before_job)

        if len(before_job) == 0: # 겹치지 않음
            for day in range(i, i+consultant[i][0]): days[day] = i
        else: # 겹침
            for conflict_job in before_job: # 현재 직업과 겹치는 직업의 기대수익을 비교
                conflict_profit += consultant[conflict_job][1]
            # print('이전수익', conflict_profit, '이번 기대수익', consultant[i][1])
            if conflict_profit >= consultant[i][1]: # 이전 수익이 크거나 같으면
                continue
            else: # 이번 상담의 기대수익이 더 크다면, 이전 작업들을 취소
                for new in range(i, i+consultant[i][0]):
                    days[new] = i
                for idx in range(N):
                    if days[idx] in before_job: days[idx] = -1
    # print(f'{i+1}번째 상담계획', days)
    # print()

answer = 0
result = set(days)
# print(result)
for idx in result:
    if idx != -1: answer += consultant[idx][1]

print(answer)