t = int(input())
for tc in range(1, t+1):
    n = int(input())
    costs = list(input())
    real_costs = []
    for i in range(len(costs)):
        if costs[i] != ' ' and costs[i] != ',': # 리스트로 받고 나서 불필요한 공백, 쉼표 제거
            real_costs.append(costs[i])

    depth = 0
    total_cost = [] # 각 유지 보수 비용 담을 리스트
    for i in range(len(real_costs)): # 문자 하나씩 탐색
        if real_costs[i] == '[': # 괄호 열면 깊이 하나 추가
            depth += 1
        elif real_costs[i] == ']': # 괄호 닫으면 깊이 하나 빼기
            depth -= 1
        else: # 괄호 아닌 경우 (= 숫자인 경우)
            total_cost.append(int(real_costs[i]) * depth) # (숫자 * 현재 깊이)를 total_cost에 추가

    print(f'#{tc} {sum(total_cost)}')


