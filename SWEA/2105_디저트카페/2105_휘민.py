import sys
sys.stdin = open('input_2105.txt')

direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def dfs(row, col, dir, cnt, dessert):
    global max_dessert, start_row, start_col
    # 갈 수 있는 방향 인덱스를 벗어나면 return
    if dir > 3:
        return

    # 시작점과 동일한 곳에 도착하면
    if row == start_row and col == start_col:
        if cnt > max_dessert: max_dessert = cnt # max_dessert update
        return

    # 시작점과 동일하지 않고 이미 먹은 디저트라면
    # if row != start_row and col != start_col and cafe_map[row][col] in dessert: 하면 안됨..
    if cafe_map[row][col] in dessert:
        return # 더 이상 탐색하지 않음

    # 이외의 경우는 ...
    next_dessert = dessert + [cafe_map[row][col]]     # 디저트 추가
    nx, ny = row + direction[dir][0], col + direction[dir][1] # 다음 위치 업데이트

    # 인덱스 이내에 존재하는지 확인
    if 0 <= nx < N and 0 <= ny < N:
        dfs(nx, ny, dir, cnt+1, next_dessert)
    if dir < 3:
        nx, ny = row + direction[dir+1][0], col + direction[dir+1][1] # 다음 방향에 대한 nx ,ny 업데이트
        if 0 <= nx < N and 0 <= ny < N:
            dfs(nx, ny, dir+1, cnt+1, next_dessert)
    return


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cafe_map = [list(map(int, input().strip().split())) for _ in range(N)]
    max_dessert = -1

    # 모든 점에서 시작 (가능한 시작점만)
    for i in range(N - 2):  # 사각형을 만들려면 충분한 공간이 필요
        for j in range(1, N - 1):  # 양쪽 끝은 사각형 생성이 어려움
            start_row, start_col = i, j
            dessert = []

            # 시작점의 디저트 추가
            dessert.append(cafe_map[start_row][start_col])

            # 첫 번째 방향(우하(1, 1)으로 DFS 시작
            dfs(start_row+1, start_col+1, 0, 1, dessert)

    print(f"#{t} {max_dessert}")


#
# # 우하, 좌하, 좌상, 우상 (시계방향)
# direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
#
# def dfs(row, col, path_len, dir_idx, direction_changes):
#     """
#     Parameter
#     - row: 현재 위치의 행
#     - col: 현재 위치의 열
#     - path_len: 현재까지 지나온 경로의 길이
#     - dir_idx: 현재 진행 중인 방향의 인덱스
#     - direction_changes: 방향 전환 횟수
#     """
#     global max_dessert, N, start_row, start_col, dessert_set
#
#     # 종료 조건
#     # 출발점에 도달했는지 체크 (최소 4개의 카페를 거쳐야 하고, 정확히 3번 방향전환 해야 함)
#     # 출발점에 도착했고, 이동을 2번 이상해야함
#     if row == start_row and col == start_col and path_len > 1:
#         # 방향 전환을 정확히 3번 하고, path_len이 최소 4 이상이여야함
#         if direction_changes == 3 and path_len >= 4:
#             if path_len > max_dessert: max_dessert = path_len # 그렇다면 max_dessert 업데이트
#         return
#
#     # 가지치기: 방향 전환이 3번을 초과하면 더 이상 진행하지 않음
#     if direction_changes > 3:
#         return
#
#     # 현재 방향으로 계속 이동
#     next_row = row + direction[dir_idx][0]
#     next_col = col + direction[dir_idx][1]
#
#     # 진행하려는 방향으로 갈 수 있고
#     if (0 <= next_row < N and 0 <= next_col < N and
#             # 진행하려는 곳이 시작점이 아니거나 path_len가 4이상인 경우
#             (not (next_row == start_row and next_col == start_col) or path_len >= 4)):
#
#             # (next_row != start_row or next_col != start_col or path_len >= 4)):
#
#         # 출발점이 아니라면 디저트 중복 체크
#
#             # 인덱스를 벗어나지 않고 path_len이 4 인 경우
#         if next_row == start_row and next_col == start_col:
#             # 출발점 복귀 시도
#             if direction_changes == 3 and path_len >= 4:
#                 if path_len > max_dessert: max_dessert = path_len
#             # 인덱스를 벗어나지 않고 도착점이 아닌 경우 -> 계속 진행방향으로 이동
#         elif cafe_map[next_row][next_col] not in dessert_set: # 이미 먹은 디저트가 아니라면
#             # 새로운 디저트 카페 방문
#             dessert_set.add(cafe_map[next_row][next_col])
#             # 같은 방향 이동이므로 dir_idx,direction_changes는 그대로 유지
#             dfs(next_row, next_col, path_len + 1, dir_idx, direction_changes)
#             # backtracking
#             dessert_set.remove(cafe_map[next_row][next_col])
#
#     # 방향 전환 (다음 방향으로만 전환 가능, 시계방향)
#     if direction_changes < 3: # 아직 마지막 방향이 아니라면
#         next_dir_idx = dir_idx + 1 # 다음 방향으로 전환
#         next_row = row + direction[next_dir_idx][0] # 다음 방향 row
#         next_col = col + direction[next_dir_idx][1] # 다음 col 업데이트
#
#         # 인덱스 이내에 존재하고
#         if (0 <= next_row < N and 0 <= next_col < N and
#                 # 진행하려는 곳이 시작점이 아니거나 path_len가 4이상인 경우
#                 (not (next_row == start_row and next_col == start_col) or path_len >= 4)):
#
#             # path_len이 4 이상인 경우 중 출발점과 같은 경우
#             if next_row == start_row and next_col == start_col:
#                 # 출발점 복귀 시도 (방향 전환할거니까 directon_changes + 1)
#                 if direction_changes + 1 == 3 and path_len >= 4:
#                     if path_len > max_dessert: max_dessert = path_len
#
#             elif cafe_map[next_row][next_col] not in dessert_set:
#                 # 새로운 디저트 카페 방문
#                 dessert_set.add(cafe_map[next_row][next_col])
#                 dfs(next_row, next_col, path_len + 1, next_dir_idx, direction_changes + 1)
#                 dessert_set.remove(cafe_map[next_row][next_col])
#
#
# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     cafe_map = [list(map(int, input().strip().split())) for _ in range(N)]
#     max_dessert = -1
#
#     # 모든 점에서 시작 (가능한 시작점만)
#     for i in range(N - 2):  # 사각형을 만들려면 충분한 공간이 필요
#         for j in range(1, N - 1):  # 양쪽 끝은 사각형 생성이 어려움
#             start_row, start_col = i, j
#             dessert_set = set()
#
#             # 시작점의 디저트 추가
#             dessert_set.add(cafe_map[start_row][start_col])
#
#             # 첫 번째 방향(우하)으로 DFS 시작
#             dfs(start_row, start_col, 1, 0, 0)
#
#     print(f"#{t} {max_dessert}")
