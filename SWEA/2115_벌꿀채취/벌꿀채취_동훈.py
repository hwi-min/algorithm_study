# M개 벌통에서 용량 C 내의 최대 이익을 계산하는 함수
def get_profit_from_block(block):
    max_p = 0

    # 재귀로 M개 벌통의 모든 채취 조합을 탐색
    def find_subsets(index, honey_sum, profit_sum):
        nonlocal max_p
        
        # M개의 벌통을 모두 고려했다면 재귀 종료
        if index == M:
            max_p = max(max_p, profit_sum)
            return

        # 현재 벌통을 채취하는 경우
        if honey_sum + block[index] <= C:
            find_subsets(index + 1, honey_sum + block[index], profit_sum + block[index]**2)

        # 현재 벌통을 채취하지 않는 경우
        find_subsets(index + 1, honey_sum, profit_sum)

    find_subsets(0, 0, 0)
    return max_p


T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    honeycomb = [list(map(int, input().split())) for _ in range(N)]
    
    # 모든 위치별 최대 이익을 미리 계산 메모이제이션 이용
    # 중복 계산을 방지하여 효율을 높임
    max_profit_memo = [[0] * (N - M + 1) for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            selected_block = honeycomb[i][j:j+M]
            max_profit_memo[i][j] = get_profit_from_block(selected_block)

    # 두 일꾼의 위치 조합을 탐색하여 최대 이익 합산
    total_max_profit = 0
    
    # 일꾼 A와 B의 모든 위치 조합을 완전탐색
    for r1 in range(N):
        for c1 in range(N - M + 1):
            profit_A = max_profit_memo[r1][c1]
            
            # A와 겹치지 않는 B의 위치 탐색
            # 1. A와 같은 행에 위치
            for c2 in range(c1 + M, N - M + 1):
                profit_B = max_profit_memo[r1][c2]
                total_max_profit = max(total_max_profit, profit_A + profit_B)
            
            # 2. A의 다음 행부터 위치
            for r2 in range(r1 + 1, N):
                for c2 in range(N - M + 1):
                    profit_B = max_profit_memo[r2][c2]
                    total_max_profit = max(total_max_profit, profit_A + profit_B)

    print(f"#{test_case} {total_max_profit}")