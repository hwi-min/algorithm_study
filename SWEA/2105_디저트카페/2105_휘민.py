"""푸는중.. 넘무 어렵네요..."""

# import sys
# sys.stdin = open('input_2105.txt')
#
# # 방향 정의     우하      좌하      좌상      우
# direction = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
#
# def dfs(x, y, path_len, dir):
#     """
#     :param x: 현재 위치의 x 좌표
#     :param y: 현재 위치의 y 좌표
#     :param path_len: 현재까지 지나온 경로의 길
#     :param dir: 현재 진행중인 방향의 인덱스
#     """
#     global max_dessert, N, start_x, start_y, dessert_set, visited
#
#     # 종료 조건
#         # 모든 방향 탐색완 / 시작점으로 돌아온 경우
#     if dir == 3 and x == start_x and y == start_y:
#         # 현재까지 지나온 경로가 max_dessert보다 큰 경우 업데이트
#         if path_len > max_dessert: max_dessert = path_len
#         return # 아니라면 그냥 반환
#
#     # 가치치기 조건: 이미 dessert_set에 존재하는 디저트라면 더 이상 탐색하지 않음
#     if cafe_map[x][y] in dessert_set: return
#
#     # 종료 조건과 가지치기 조건에 해당하지 않는다면 ...
#     dessert_set.add(cafe_map[x][y]) # 현재 디저트를 추가
#     visited[x][y] = True # 방문처리
#
#     # 1. 같은 방향으로 계속 탐색하는 경우
#     same_dir_x, same_dir_y = x + direction[dir][0], y + direction[dir][1]
#
#     # map 안의 인덱스인지 확인
#     if 0 <= same_dir_x < N and 0 <= same_dir_y < N:
#         # 방문처리는 신경쓰지 않음 -> 사각형 완성을 위해 최초지점으로 돌아가는 경우일수도 있으니까
#         dfs(same_dir_x, same_dir_y, path_len+1, dir)
#
#     # 2. 다음 방향으로 전환하는 경우
#     if dir != 3: # 방향인덱스가 3이 아닌 경우
#         next_dir = dir + 1 # 다음 방향으로 가야하므로 +1
#         next_dir_x, next_dir_y = x + direction[next_dir][0], y + direction[next_dir][1]
#
#         # map안의 인덱스인지 확인
#         if 0 <= next_dir_x < N and 0 <= next_dir_y < N:
#             dfs(next_dir_x, next_dir_y, path_len+1, next_dir)
#
#     # 백트래킹: 현재 재귀가 끝나면 다른 경로를 탐색할 수 있도록 원상복귀
#     dessert_set.remove(cafe_map[x][y])
#     visited[x][y] = False
#
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     cafe_map = [list(map(int, input().strip().split())) for _ in range(N)]
#     max_dessert = -1
#
#     # 모든 점에서 시작 (시작점 설정)
#     for i in range(N-2): # 사각형을 만들려면 마지막 열 2개는 후보가 될 수 없음
#         for j in range(1, N-1): # 마찬가지로 사각형을 만들려면 인덱스 0열, 마지막 열 하나는 후보가 될 수 없음
#             start_x, start_y = i, j # 시작점 x, y 저장
#             dessert_set = set() # 각 시작점에 대한 dessert set 정의 (중복 디저트는 허용하지 않기 떄문에)
#             visited = [[False] * N for _ in range(N)] # 방문 체크
#             # DFS 탐색
#             dfs(start_x, start_y, 1, 0)
#
#     print(f"#{t} {max_dessert}")

direction = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

def dfs(x, y, path_len, dir_idx):
    """
    :param x: 현재 위치의 x 좌표
    :param y: 현재 위치의 y 좌표
    :param path_len: 현재까지 지나온 경로의 길이
    :param dir_idx: 현재 진행 중인 방향의 인덱스
    """
    global max_dessert, N, start_x, start_y, dessert_set

    # 1. 종료 조건: 마지막 방향으로 이동하던 중에 시작점에 돌아온 경우
    if dir_idx == 3 and (x + direction[3][0] == start_x) and (y + direction[3][1] == start_y):
        if path_len + 1 > max_dessert: max_dessert = path_len + 1 # 현재까지 지나온 경로가 max_dessert보다 큰 경우 업데이트
        return # 아니라면 반환

    # 2. 다음으로 이동
    # 현재 방향으로 이동 or 방향 전환 이동
    for i in range()

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cafe_map = [list(map(int, input().strip().split())) for _ in range(N)]
    max_dessert = -1

    # 모든 점에서 시작 (시작점 설정)
    for i in range(N-2): # 사각형을 만들려면 마지막 열 2개는 후보가 될 수 없음
        for j in range(1, N-1): # 마찬가지로 사각형을 만들려면 인덱스 0열, 마지막 열 하나는 후보가 될 수 없음
            start_x, start_y = i, j # 시작점 x, y 저장
            dessert_set = set() # 각 시작점에 대한 dessert set 정의 (중복 디저트는 허용하지 않기 떄문에)

            # 시작점 처리
            dessert_set.add(cafe_map[start_x][start_y])
            # DFS 탐색
            dfs(start_x, start_y, 1, 0)

    print(f"#{t} {max_dessert}")
