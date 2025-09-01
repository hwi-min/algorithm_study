#     상  하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dictionary = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z'
}


def paint_like_picasso():
    global row, col
    queue = [[] for _ in range(K)]  # 세균 수 만큼 만들어놓자

    for _ in range(max(spread_count)):  # 최대 번식 횟수만큼
        for dic in range(K):   # 세균 종류 개수만큼
            if spread_count[dic] == 0: continue # 정해진 번식 횟수가 끝나면 다음 세균으로

            char = dictionary[dic]      # 일단 세균(알파벳) 가져와라

            # matrix 돌면서 해당 세균이 있는 위치 찾기
            for i in range(row):
                for j in range(col):
                    if matrix[i][j] == char:
                        queue[dic].append((i, j))

            for _ in range(len(queue[dic])):    # 현재 저장되어있는 위치 개수 만큼 반복
                x, y = queue[dic].pop(0)    # 세균이 있는 좌표 꺼내기

                # 델타 탐색
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 벽에 안부딪히고, 해당 위치가 다른 세균이 아닌 '.' 이라면
                    if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] == '.':
                        queue[dic].append((nx, ny)) # 번식된 좌표 넣어두고
                        matrix[nx][ny] = char   # 해당 좌표에 세균 삽입

            spread_count[dic] -= 1  # 번식 횟수 줄이기


T = int(input())
for tc in range(1, T + 1):
    col, row = map(int, input().split())    # col: 가로 길이, row: 세로 길이
    K = int(input())    # 세균의 종류
    spread_count = list(map(int, input().split()))  # 각 세균의 번식 횟수

    matrix = [list(input().split()) for _ in range(row)]    # 현재 세균 정보

    paint_like_picasso()    # 세균 번식 시작

    # 출력 형식에 맞게 출력
    print(f'#{tc}')
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end=' ')
        print()
