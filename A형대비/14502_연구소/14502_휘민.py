from itertools import combinations
from collections import deque
import copy

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(comb, virus_list):
    sub_lab = copy.deepcopy(lab) # 임시 맵 생성
    
    # comb에 대한 벽 먼저 세움
    for comb_x, comb_y in comb:
        sub_lab[comb_x][comb_y] = 1

    # 원래 바이러스 위치를 그대로 큐에 삽입
    queue = deque((virus_list))

    while queue:
        x, y = queue.popleft() # 바이러스가 있는 좌표 가져옴
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and sub_lab[nx][ny] == 0: # 1이 아니면 바이러스 감염
                sub_lab[nx][ny] = 2 # 바이러스가 퍼졌음을 표시해주고
                queue.append((nx, ny)) # queue에 추가

    safe_zone = 0
    for row in sub_lab: safe_zone += row.count(0)

    return safe_zone



N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

"""
- 0인 좌표들의 모든 조합을 구함 (combinations)
- 해당 좌표들에 대한 시뮬레이션을 실행 -> 계속해서 min값을 업데이트

- bfs
    - 모든 바이러스 시작점을 담으면서 한칸씩 전파시킴
"""
# 안전영역의 최대값 초기화
max_safe_zone = 0

blank_list = []
virus_list = []
# 빈칸(0)인 좌표들, virus(2)인 좌표들만 따로 저장
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            blank_list.append((i, j))
        elif lab[i][j] == 2:
            virus_list.append((i, j))

# 모든 blank_list의 조합을 찾음
for comb in combinations(blank_list, 3):
    # 해당 comb에 대한 bfs 결과 후 안전영역의 수를 셈
    current_safe_zone = bfs(comb, virus_list) 
    # 만약 현재 comb의 max_safe_zone의 개수가 max_safe_zone보다 크다면 업데이트   
    if current_safe_zone > max_safe_zone: 
        max_safe_zone = current_safe_zone

print(max_safe_zone)
