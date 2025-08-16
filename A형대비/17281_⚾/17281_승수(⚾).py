# from itertools import permutations
#
#
# def in_play(inning_res, batting_order):
#     total_score = 0
#     current_batter = 0  # 현재 타자 idx
#
#     for inning in inning_res:   # 모든 이닝에 대해서
#         score = 0
#         base_status = [False] * 3   # 1, 2, 3루 상태 (False: 주자없음, True: 주자있음)
#         out_count = 0
#
#         while out_count < 3:    # 3아웃 되기 전까지 반복
#             player_idx = batting_order[current_batter]  # 현재 타자 idx
#             result = inning[player_idx] # 현재 타자의 예상 점수
#
#             if result == 0:  # 아웃
#                 out_count += 1
#             elif result == 1:  # 안타
#                 # 3루 주자 홈인
#                 if base_status[2]:
#                     score += 1
#                     base_status[2] = False
#                 # 주자들 한 베이스씩 진루
#                 base_status[2] = base_status[1]
#                 base_status[1] = base_status[0]
#                 base_status[0] = True
#
#             elif result == 2:  # 2루타
#                 # 2, 3루 주자 홈인
#                 if base_status[2]:
#                     score += 1
#                 if base_status[1]:
#                     score += 1
#                 # 1루 주자는 3루로, 타자는 2루로
#                 base_status[2] = base_status[0]
#                 base_status[1] = True
#                 base_status[0] = False
#
#             elif result == 3:  # 3루타
#                 # 모든 주자 홈인
#                 score += sum(base_status)
#                 # 타자는 3루로
#                 base_status = [False, False, True]
#
#             elif result == 4:  # 홈런
#                 # 모든 주자 + 타자 홈인
#                 score += sum(base_status) + 1
#                 base_status = [False] * 3
#
#             # 9번 타자까지 치면 다시 1번 타자로 되돌아오기
#             current_batter = (current_batter + 1) % 9
#
#         # 3아웃 되면 이닝 종료 및 점수 갱신
#         total_score += score
#     return total_score
#
#
# inning = int(input())   # 이닝 수
# # 각 이닝 당 선수들이 낼 수 있는 점수
# inning_result = [list(map(int, input().split())) for _ in range(inning)]
# max_total_score = 0
#
# # 1번 선수 (4번 타자) 제외 permutation 돌리기 위한 list
# other_players = list(range(1, 9))
# for perm in permutations(other_players): # 모든 순열에 대해서
#     # 4번 타자 제외 나머지를 구한 순열로 채우기
#     order = list(perm[:3]) + [0] + list(perm[3:])
#
#     score = in_play(inning_result, order)   # 이닝 시작
#     max_total_score = max(max_total_score, score)   # 최댓값 갱신
#
# print(max_total_score)







# def simulate_game(innings_data, batting_order):
#     total_score = 0
#     current_batter = 0
#
#     for inning in innings_data:
#         score = 0
#         base = 0  # bit 0=1루, bit 1=2루, bit 2=3루
#         out_count = 0
#
#         while out_count < 3:
#             player_idx = batting_order[current_batter]
#             result = inning[player_idx]
#
#             if result == 0:  # 아웃
#                 out_count += 1
#             elif result == 1:  # 안타
#                 score += (base >> 2) & 1  # 3루 주자 득점
#                 base = ((base << 1) & 0b110) | 1  # 모든 주자 진루 + 타자 1루
#             elif result == 2:  # 2루타
#                 score += (base >> 1) & 0b11  # 2,3루 주자 득점 (bin(base >> 1)의 하위 2비트)
#                 base = ((base & 1) << 2) | 0b10  # 1루→3루, 타자→2루
#             elif result == 3:  # 3루타
#                 score += bin(base).count('1')  # 모든 주자 득점
#                 base = 0b100  # 타자만 3루
#             else:  # 홈런 (result == 4)
#                 score += bin(base).count('1') + 1  # 모든 주자 + 타자 득점
#                 base = 0  # 모든 베이스 클리어
#
#             current_batter = (current_batter + 1) % 9
#
#         total_score += score
#
#     return total_score
#
#
# def solve_with_bitmask():
#     N = int(input())
#     innings_data = []
#     for _ in range(N):
#         innings_data.append(list(map(int, input().split())))
#
#     max_score = 0
#
#     def generate_permutation(mask, order, pos):
#         nonlocal max_score
#
#         # 모든 자리가 채워졌으면 게임 시뮬레이션
#         if pos == 9:
#             score = simulate_game(innings_data, order)
#             max_score = max(max_score, score)
#             return
#
#         # 4번 타자(인덱스 3)는 1번 선수(0번)로 고정
#         if pos == 3:
#             order[pos] = 0
#             generate_permutation(mask | 1, order, pos + 1)  # 0번 선수 사용 표시
#             return
#
#         # 1번부터 8번 선수(인덱스 1~8) 중에서 선택
#         for player in range(1, 9):
#             # 해당 선수가 아직 사용되지 않았다면
#             if not (mask & (1 << player)):
#                 order[pos] = player
#                 # 해당 선수를 사용했다고 표시하고 다음 위치로
#                 generate_permutation(mask | (1 << player), order, pos + 1)
#
#     order = [0] * 9
#     # 초기 마스크는 1 (0번 선수는 이미 4번 타자로 예약됨)
#     generate_permutation(1, order, 0)
#
#     return max_score
#
# print(solve_with_bitmask())





import sys
from itertools import permutations

N = int(sys.stdin.readline())
game = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

order = [i for i in range(1, 9)]  # 고정된 4번타자 제외하고 순서를 정해주자.
result = 0

for x in permutations(order, 8):  # 8명 순열 돌리기
    x = list(x)
    batter = x[:3] + [0] + x[3:]  # 1~3번 타자(랜덤 3명) / 4번 타자 (고정) / 4~8번 타자(랜덤 5명)
    number, point = 0, 0  # 타수와 점수
    for i in range(N):  # 각 이닝에 대해
        out = 0  # 이닝이 돌면 out은 0으로 초기화
        p1 = p2 = p3 = 0  # 1~3루의 현재 상태
        while out < 3:  # 쓰리아웃 전까지 반복
            # 각 안타에 맞게 루 세팅
            if game[i][batter[number]] == 0:
                out += 1
            elif game[i][batter[number]] == 1:
                point += p3
                p1, p2, p3 = 1, p1, p2
            elif game[i][batter[number]] == 2:
                point += p2 + p3
                p1, p2, p3 = 0, 1, p1
            elif game[i][batter[number]] == 3:
                point += p1 + p2 + p3
                p1, p2, p3 = 0, 0, 1
            elif game[i][batter[number]] == 4:
                point += p1 + p2 + p3 + 1
                p1, p2, p3 = 0, 0, 0

            number += 1  # 타순 증가
            if number == 9:  # 타순이 9가 되면
                number = 0  # 다시 0으로 초기화
    result = max(result, point)

print(result)