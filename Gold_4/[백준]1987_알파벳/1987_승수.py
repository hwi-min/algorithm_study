# 세로 R칸, 가로 C칸 으로 된 표 모양의 보드
# 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸에는 말이 놓임
# 말은 상하좌우 인접 네 칸 중 한 칸으로 이동, 해당 칸에는 지금까지 지나온 알파벳과는 달라야 함
# 좌측 상단에서 시작하여, 말이 최대 몇 칸을 지날 수 있는지? (좌측 상단의 칸도 포함)

#     상  하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def move(r, c, count):
    global max_count

    max_count = max(max_count, count)   # 최대 count 갱신

    for d in range(4):  # 인접한 네 칸 중 하나로 이동
        nr, nc = r + dr[d], c + dc[d]

        # 보드판을 벗어나지 않고, 사용된 알파벳이 아니라면
        if 0 <= nr < R and 0 <= nc < C:
            idx = ord(board[nr][nc]) - 65

            if not used_alphabet[idx]:
                used_alphabet[idx] = True   # 알파벳 사용
                move(nr, nc, count + 1)     # count 1 증가 시키고 재귀호출
                used_alphabet[idx] = False  # 백트래킹


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

start_r, start_c = 0, 0 # 시작 위치
max_count = 0           # 지날 수 있는 최대 칸 수 (0으로 초기화)

# used_alphabet = set()   # 지나간 알파벳 저장
used_alphabet = [False] * 26

used_alphabet[ord(board[start_r][start_c]) - 65] = True  # 시작 위치 알파벳 저장

move(start_r, start_c, 1)   # 시작위치부터 dfs 수행
print(max_count)
