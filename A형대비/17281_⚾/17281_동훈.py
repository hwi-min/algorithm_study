'''
    1번 선수는 무조건 4번 타자를 수행함
    1번 선수의 타석은 고정되고, 나머지 선수들의 타석 순서를 조정하여
    주어진 이닝에서 얻을 수 있는 최대 점수를 찾아야 함.
    
    타순이 한 번 정해지면 이닝이 변경되어도 순서를 바꿀 수 없다.
    
    결국엔 주어진 이닝을 전부 고려해야 최대값을 얻을 수 있음
'''
from itertools import permutations

def baseball_simulation(batting_order):
    global N
    global max_score
    '''
        주어진 이닝에서 현재 타순으로 얻어지는 점수를 리턴함.
        주어지는 타석 순서는 permutation 함수로 주어진 타석순서이다.
        ex -> (1,2,3,4,5,6,7,8)
    '''
    # 항상 1번(0번)선수가 4번타자임
    score = 0
    batting_order = list(batting_order)
    batting_order.insert(3,0)
    base = list()
    
    # 현재 이닝과 타석에 들어선 선수 
    now_innings = 0
    idx = 0
    
    while now_innings < N:
        # 이닝마다 아웃카운트 초기화, base 초기화
        base.clear()
        outcount = 0
        while outcount < 3:
            
            # N번째 이닝에서 idx번째 선수의 배팅포인트
            batting = record[now_innings][batting_order[idx]]
            
            if batting == 0: # 해당선수 아웃
                outcount += 1
            else: # 1루타 이상이면
                # 모든 주자 진루
                for i in range(len(base)): base[i] = base[i] + batting
                # 타자 진루
                base.append(batting)
                # 앞에서부터 홈 지난 선수들 뺌
                while base:
                    if base[0] >= 4:
                        base.pop(0)
                        score += 1
                    else: break   
            idx = (idx + 1) % 9
        # 이닝 끝
        now_innings += 1

    # 최대점수와 비교
    max_score = max(max_score, score)

# 총 이닝 수
N = int(input())

# 이닝 별 루타 기록
# 안타, 1, 2, 3루타, 홈런 : 1 ~ 4
# 아웃 : 0
max_score = 0
record = [list(map(int, input().split())) for _ in range(N)]
for order in permutations(range(1, 9), 8):
    baseball_simulation(order)
print(max_score)