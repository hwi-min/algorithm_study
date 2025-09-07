"""
시간제한 1초(1억)
N이 최대 20이므로 ...
- 최악의 경우 (N=20) 
    가능한 모든 조합(Combinations) C(20, 10) 사용시 184576 (18만)
- 최악의 경우 (N//2 == 10)
    한 팀 내에서의 가능한 모든 조합(Combinations) C(10, 2) 사용시 45
-> 184576 * 45 : 8,314,020 (8백만) ---> 가능!
"""
from itertools import combinations

def cal_team_ability(team): # 1, 2, 4, 6
    score = 0
    for i, j in combinations(team, 2):
        score += S[i][j] + S[j][i]
    return score

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
min_diff = 99

for comb in combinations(range(N), N//2):
    team1 = list(comb)
    team2 = list(set(range(N)) - set(comb)) # 1, 2, 4, 6

    # 능력치 계산
    team1_ability = cal_team_ability(team1)
    team2_ability = cal_team_ability(team2)

    min_diff = min(min_diff, abs(team1_ability - team2_ability))

print(min_diff)
