'''
    최대 M개의 치킨집을 골랐을 때, 가장 치킨거리를 작게 만들어야 함.
    즉, 주어진 N개의 치킨 집 중 M개를 골라서 치킨거리가 가장 거리를 리턴함
    N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)
    -> N은 정사각형 도시의 크기, M은 살아남은 치킨집
    0은 빈칸, 1은 집, 2는 치킨집. 치킨집이 몇개 있을지 모름
    dfs로 가야함? 일단 조합으로 ㄱㄱ
'''
from itertools import combinations

# N 도시의 크기, M 폐업시키지 않을 도시의 개수
N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

chickenzip = []
house = []

# 치킨집 좌표
for i in range(N):
    for j in range(N):
        # 각각 행열 순으로 넣어줌
        if city[i][j] == 2: chickenzip.append((i,j))
        if city[i][j] == 1: house.append((i,j))

# min_distance = N + N
answer = []
# 조합 생성
for comb in combinations(chickenzip, M):
    # print(comb)
    total_dis = 0
    # 각각의 집 마다 가장 가까운 치킨집을 찾아야 함.
    for y, x in house: # 집 좌표
        small_dis = N + N
        for row, col in comb: # 살아남은 치킨집 좌표
            # l1norm계산
            dis = abs(y-row) + abs(x-col)
            small_dis = min(small_dis, dis)
        total_dis += small_dis
    
    # print('total dis',total_dis)
    answer.append(total_dis)
    # 최솟값 갱신
    # min_distance = min(min_distance, total_dis)
    

print(min(answer))