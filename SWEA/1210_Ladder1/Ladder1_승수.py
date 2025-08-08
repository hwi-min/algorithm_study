import sys
sys.stdin = open('input.txt')

def path(ladder):
    direction = 0     # 현재 이동중인 방향 저장할 변수
    # 사다리에서 2인 곳을 찾아서 해당 인덱스를 idx에 저장 (목적지에서 출발지로 찾아 올라갈 예정)
    for i, row in enumerate(ladder):
        for j, value in enumerate(row):
            if value == 2:
                idx = (i, j)
    i, j = idx

    # idx에서 거꾸로 올라가기
    while i != 0:
        if j > 0 and ladder[i][j - 1] == 1 and direction != 2:   # 왼쪽에 1이 있다면 인덱스를 왼쪽으로
            j -= 1
            direction = 1     # 현재 왼쪽으로 이동 중..
        elif j < 99 and ladder[i][j + 1] == 1 and direction != 1: # 오른쪽에 1이 있다면 인덱스를 오른쪽으로
            j += 1
            direction = 2     # 현재 오른쪽으로 이동 중..
        else:   # 둘 다 없으면 인덱스를 위로
            i -= 1
            direction = 0     # 현재 위쪽으로 이동 중..

    col = j
    return col

for _ in range(10):
    tc = int(input())   # 테케 입력

    ladder = [list(map(int, input().split())) for _ in range(100)]  # 사다리 입력

    start = path(ladder)    # 사다리 타기 시작
    print(f'#{tc} {start}')