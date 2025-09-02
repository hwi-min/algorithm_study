'''
    14889_스타트와링크  

    스타트링크에 다니는 사람들이 모여서 축구를 한다.
    축구를 하기 위해 짝수 N명이 모임.

    Sij는 i번째 사람과 j번째 사람이 같은 팀에 모였을 때 팀에 더해지는 능력치이다.

    각 팀의 능력치 차이가 가장 적을때의 최솟값을 출력함.
'''

'''
    단순히 N개를 2개의 그룹으로 나누는 것이 아니라. 두 그룹의 인원수가 같게 만들어야 함.

    조합?
    최대 -> 20C10 = 184756
    Combination을 이용해서 N/2개를 뽑고, 나머지 N/2개를 뽑아서 능력치 차이를 구함.
'''

from itertools import combinations

# N명
N = int(input())

# 시너지정보
score = [list(map(int, input().split())) for _ in range(N)]

team_diff = float('inf')

for comb in combinations(range(N),N//2):
    start = 0
    link = 0
    for i in range(N):
        for j in range(N):
            if i in comb and j in comb: # 두명이 전부 조합에 포함되면
                start += score[i][j]
                start += score[j][i]
            elif i not in comb and j not in comb: # 그렇지 않으면
                link += score[i][j]
                link += score[j][i]
    team_diff = min(team_diff, abs(start-link)//2)    
print(team_diff)
                