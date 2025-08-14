import sys
sys.stdin = open('algo1_sample_in.txt')

def dfs(idx, spent_time, selected): # 해당 재료의 idx, 지금까지의 시간 합, 선택한 재료의 개수
    global success

    if selected == cnt:  # 선택 개수가 필요한 물품 수와 같으면 ...
        if spent_time == time: # 지금까지의 시간의 합과 연성품의 시간이 동일하면
            success = value # success 값을 value로 업데이트
        return

    '''
    오류 부분:
    - 원래: idx == I-1이었음음    
    - idx == I-1을 하면 마지막 케이스를 확인하지 않고 끝나는 문제 발생
    '''
    if idx >= I: # idx가 마지막까지 돌았다면 return
        return

    dfs(idx+1, spent_time + times[idx], selected + 1) # 해당 요소를 선택하는 경우
    dfs(idx+1, spent_time, selected) # 해당 요소를 선택하지 않는 경우


T = int(input())

for t in range(1, T+1):
    N = int(input()) # 연성품 개수
    costs = [] # 연성품 리스트

    for _ in range(N): # 해당 연성품 생성에 필요한 정보 저장
        cost = list(map(int, input().strip().split())) # 물품의 개수, 필요한 시간, 상품의 가치
        costs.append(cost) # ex. [[4, 25, 3], [3, 56, 10]]

    I = int(input()) # 재료 개수
    times = list(map(int, input().strip().split())) # I개의 재료개수의 각 소요시간

    # ''가능한 연성''의 value를 저장한 리스트 초기화
    values = []

    # N개의 연성품들을 순회하며
    for elem_lst in costs: # [4, 25, 3] ...
        cnt, time, value = elem_lst[0], elem_lst[1], elem_lst[2] # 물품의 개수, 필요한 시간, 상품의 가치

        success = 0 # 가능한 value 값을 저장할 success 초기화

        dfs(0, 0, 0) # 해당 재료의 idx, 지금까지의 시간 합, 선택한 재료의 개수

        # 만약 연성품 제작이 가능하다면, value값 추가
        if success: values.append(value)

    # 가능한 연성의 value 중 가장 큰 값을 result로 저장
    result = max(values) if values else 0

    print(f"#{t} {result}")
