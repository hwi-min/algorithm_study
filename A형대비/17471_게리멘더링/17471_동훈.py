'''
    우리의 목표는 각 지역구의 인구수 차이를 가장 작게 만들어야 함.
    
    각 지역구는 지역끼리 바로 연결되어있어야 함.
    
    두 개의 선거구로 나누어야 함.
    선거구의 조건
    1. 무조건 하나 이상의 지역이 존재해야 함.
    2. 각 지역은 서로 바로 인접해 있어야 함.(인접리스트로 확인)
    
    로직 :
    dfs로 가능한 선거구의 후보를 모두 탐색함.
    이후 선거구의 조건을 만족하면 각 선거구의 인구수 차이를 계산
'''

from collections import deque

def is_this_distric(election_district):
    '''
        선거구 확인
    선거구의 조건
    1. 무조건 하나 이상의 지역이 존재해야 함.
    2. 각 지역은 서로 바로 인접해 있어야 함.(인접리스트로 확인)
    '''
    # 지역구 개수
    local_number = len(election_district)
    
    if len(election_district) < 1:
        return False
    else:
        # 지역 연결되어 있는지 확인
        # 방문확인용
        visited = set()
        queue = list()
        visited.add(election_district[0])
        queue.append(election_district[0])
        # bfs로 탐색
        while queue:
            target = queue.pop(0)
            for neighbor in villages[target]:
                if neighbor in election_district and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        # 방문한 지역과 선거구의 지역이 전부 일치하면 연결 O
        if set(election_district) == visited: return True
        else: return False
    

def fairness_election(idx, election_district, now_population):
    global mininum_diff
    '''
        idx : 현재 선택할 마을 번호
        election_district : 지금까지 선거구
        
        A의 선거구에 포함할 마을
        선거구를 지정하는 함수
    '''
    # 종료조건
    # 모든 마을이 다 정해지면
    # 선거구를 만족하는 지 확인해야함.
    if idx == N:
        B_site = all_districts_set.difference(set(election_district))
        if is_this_distric(election_district) and is_this_distric(list(B_site)):
            # 최솟값 갱신
            B_site_population = total_population-now_population
            mininum_diff = min(mininum_diff, abs(B_site_population - now_population))
            return
        else: return
    
    # 가지치기 ?
    # if (total_population-now_population) > mininum_diff: return
    
    # 재귀
    election_district.append(idx)
    fairness_election(idx + 1, election_district[:], now_population + populations[idx])
    election_district.pop() # 백트래킹
    fairness_election(idx + 1, election_district[:], now_population)

from collections import defaultdict

# 구역의 개수
N = int(input())

# 구역의 인구수
populations = list(map(int, input().split()))
total_population = sum(populations)

# 인접구역의 정보
villages = defaultdict(list)

for i in range(N):
    info = list(map(int, input().split()))
    for j in range(1, info[0]+1):
        villages[i].append(info[j]-1)

# 전체 구역 
all_districts_set = set(range(N))

mininum_diff = total_population

fairness_election(0, [], 0)

if mininum_diff == total_population: print(-1)
else: print(mininum_diff)