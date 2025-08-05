# import sys
# from collections import defaultdict

# sys.stdin = open('sample_input.txt','r')

# # 정사각형 구역에 K개의 미생물 군집이 있다.
# # 이 구역은 N * N개의 동일한 크기의 정사각형 셀들로 이루어져 있다.
# # 총 크기는 (N+2) * (N+2)의 크기로 테두리에 특수 약품이 칠해져 있다.

# # 1. 미생물 군집의 위치, 2. 군집 내 미생물의 수, 3. 이동방향이 주어짐
# # 이동방향은 상하좌우의 네 방향 중 하나이다.
# # 각 군집은 1시간마다 이동방향에 있는 다음 셀로 이동한다.

# # 만약 미생물 군집이 약품이 칠해진 셀에 도착하면
# # 군집 내 미생물이 절반이 죽고, 이동방향이 반대로 바뀐다.
# # 홀수인 경우 소수점을 버리기 때문에, 한 마리가 남은 군집은 사라진다.

# # 이동 후 두 개 이상의 군집이 한 셀에 모이는 경우는 합쳐진다.
# # 미생물의 수는 두 군집의 미생물의 합이며 더 큰 군집의 이동방향을 따른다
# # PS. 군집의 수가 같은 경우는 주어지지 않는다.

# # M 시간 후에 살아남은 미생물의 총 합을 구하시오

# # 모든 미생물 군집의 변화는 모든 업데이트가 이루어진 이후에 수행해야함.
# # 군집 상태 업데이트 시 위치 정보를 저장 한 후
# # 모든 업데이트가 끝나고 난 뒤에 한 위치에 있는 군집들의 정보를 처리함.

# T = int(input()) # 총 10개의 tc

# for tc in range(1, T+1):
#     # N크기의 격자, M 시간, K개의 군집
#     N, M, K = map(int, input().split())
#     # 미생물 정보
#     # 예시) 세로위치(1), 가로위치(1), 미생물 수(7), 이동방향(상)
#     micro_organism = [list(map(int, input().split())) for _ in range(K)]

#     # M번 반복 돌면서 개체 수 만큼 업데이트
#     for _ in range(M):
#         grid = defaultdict(list)
#         # 미생물 군집 정보 업데이트
#         for i in range(len(micro_organism)):
#             # 상하좌우 업데이트
#             if micro_organism[i][3] == 1 : micro_organism[i][0] -= 1
#             elif micro_organism[i][3] == 2 : micro_organism[i][0] += 1
#             elif micro_organism[i][3] == 3 : micro_organism[i][1] -= 1
#             elif micro_organism[i][3] == 3 : micro_organism[i][1] += 1
#             # 위치가 약품 구간이면 -> 미생물 수 반 토막 냄
#             if micro_organism[i][0] in [0,6] and micro_organism[i][1] in [0,6]:
#                 micro_organism[i][2] //= 2
#             # 위치정보를 키로 갖는 인접리스트에 인덱스를 append
#             grid[micro_organism[i][0]*N + micro_organism[i][1]] = i
#         # row = micro_organism[i][0] # 세로위치
#         # col = micro_organism[i][1] # 가로위치
#         # micro_cnt = micro_organism[i][2] # 미생물의 수
#         # move_head = micro_organism[i][3] # 이동방향
#         # 인접리스트 돌면서 업데이트 처리
#         for same_position_list in grid.keys():
#             # 같은 포지션의 군집들의 번호로 접근
#             # 업데이트 해야하는 것
#             # 1. 군집의 방향
#             # 2. 군집내 미생물 수
#             max_cnt = 0
#             micro_head = 0
#             max_idx = -1
#             total_cnt = 0
#             for idx in same_position_list:
#                 total_cnt += micro_organism[idx][2]
#                 if micro_organism[idx][2] > max_cnt: 
#                     max_cnt = micro_organism[idx][2] # 크기
#                     micro_head = micro_organism[idx][3] # 방향 업데이트
#                     max_idx = idx
#             # 가장 큰 미생물 군집의 정보상태 업데이트
#             micro_organism[idx][2] = total_cnt
    
#     # 최종적으로 남은 군집의 미생물 수를 다 더해서 리턴
#     print(f'#{tc}')

import sys
from collections import defaultdict

sys.stdin = open('sample_input.txt','r')

T = int(input())

def reverse_direction(d):
    """방향을 반대로 바꾸는 함수"""
    if d == 1: return 2
    if d == 2: return 1
    if d == 3: return 4
    if d == 4: return 3

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    
    # 0:세로(row), 1:가로(col), 2:미생물 수, 3:이동방향, 4:생존플래그(1:생존, 0:사멸/흡수됨)
    micro_organisms = [list(map(int, input().split())) + [1] for _ in range(K)]

    # M 시간 동안 시뮬레이션
    for _ in range(M):
        # 1. 모든 살아있는 군집 이동 및 경계 처리
        for i in range(K):
            # 플래그를 확인하여 살아있는 군집만 처리
            if micro_organisms[i][4] == 0:
                continue
            
            # 군집 정보 받기
            row, col, count, direction, _ = micro_organisms[i]

            # 방향에 따라 위치 이동
            if direction == 1: row -= 1
            elif direction == 2: row += 1
            elif direction == 3: col -= 1
            elif direction == 4: col += 1

            # 경계에 닿았는지 확인
            if row == 0 or row == N - 1 or col == 0 or col == N - 1:
                count //= 2  # 미생물 수 절반으로 감소
                direction = reverse_direction(direction) # 방향 반대로 전환
            
            # 이동 및 경계 처리 후 군집 정보 업데이트
            micro_organisms[i] = [row, col, count, direction, 1]

        # 2. 군집 병합 처리
        # 같은 위치에 있는 군집들을 그룹화
        grid = defaultdict(list)
        for i in range(K):
            # 살아있는 군집 중 미생물이 0이 된 경우는 소멸
            if micro_organisms[i][4] == 1 and micro_organisms[i][2] == 0:
                micro_organisms[i][4] = 0
                continue
            
            # 살아있는 군집만 그룹화
            if micro_organisms[i][4] == 1:
                row, col = micro_organisms[i][0], micro_organisms[i][1]
                grid[(row, col)].append(i)

        # 군집 순회하며 병합 진행
        for pos, indices in grid.items():
            if len(indices) > 1:
                
                # 미생물 수가 가장 많은 군집을 찾기 위해 정렬
                # lambda 함수를 이용해 '미생물 수'를 기준으로 내림차순 정렬
                indices.sort(key=lambda idx: micro_organisms[idx][2], reverse=True)
                dominant_idx = indices[0]
                
                total_count = 0
                # 병합 군집 미생물 수 계산
                for idx in indices:
                    total_count += micro_organisms[idx][2]
                    # 도미넌트 제외한 군집은 흡수되므로 플래그를 0으로 변경
                    if idx != dominant_idx:
                        micro_organisms[idx][4] = 0
                
                # 도미넌트 군집 미생물 수 업데이트
                micro_organisms[dominant_idx][2] = total_count

    # 3. M시간 후 총 미생물 수 계산
    total_microbes = 0
    for i in range(K):
        # 살아있는 군집의 미생물 수만 더함
        if micro_organisms[i][4] == 1:
            total_microbes += micro_organisms[i][2]
    
    print(f'#{tc} {total_microbes}')