import sys
sys.stdin = open('input.txt')

    # 우하 좌하 좌상 우상
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

def search(x, y):
    global result
    # 2. 한 자리 맴돌기 안된다.
    # : 한 방향으로 최소, 1칸은 이동해야한다.
    # : 한 방향으로 최대 N-1칸 까지만 이동가능하다.
    for a in range(1, N):
        for b in range(1, N):
            '''
                1 1
                1 2
                1 3
                2 1
                2 2
                2 3 ....
                # : (우하, 좌상), (좌하, 우상)은 각각 같은 크기만큼 이동해야함
            '''
            # 위치 이동은 조사 시작한 (x, y) 기준으로 조사하는데,
            # 이번 경우의 수에서만 이동하는 것이고,
            # 다음 경우의 수에는 x, y가 함부로 바뀌면 안된다.
            now_x, now_y = x, y # 이번 경우의 시작할때 첫 조사 위치
            # 이번 경우의수의 여정동안 모은 디저트의 종류들
            dessert = []
            moves = [a, b, a, b]    # 현재 방향으로 최대 이동할 거리
            # 조사 계속 할 수 있는지 검증용 변수
            is_valid = True
            # 4방향에 대해 조사
            for k in range(4):
                # 정해진 k 방향으로 a or b 만큼 한칸씩 누적해서 이동하면서 조사
                # 내 첫 위치 x, y 부터 한칸씩 증가하면서 조사
                for _ in range(moves[k]):
                    now_x += dx[k]  # 내 현재 위치 기준으로 누적해서 더하기
                    now_y += dy[k]

                    # 범위를 벗어나지 않아야 한다.
                    if 0 <= now_x < N and 0 <= now_y < N:
                        # 이미 먹은거면 안먹고 조사 종료
                        if data[now_x][now_y] in dessert:
                            is_valid = False    # 더 이상 유망성 없음!
                            break
                        # 그 디저트를 먹는다!
                        dessert.append(data[now_x][now_y])
                    else:
                        is_valid = False
                # 여기도 어떤 조건에 의해서 종료가 되길바람
                # 안쪽에서 조사하다가 이미 먹은 디저트가 나와서 종료가 됐으면 나도종료
                if not is_valid:    # 다음 방향 갈 필요 없이 종료
                    break
            # 이번 경우의 수에서 4방향에 대한 모든 조사가 완료 되었다면?
            # 문제 없이 완료되었음
            if is_valid:
                # global에있는 result를 최대값으로 갱신
                result = max(result, len(dessert))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    result = -1 # 못가는 경우를 기본값으로 설정

    '''
        1. 조사 방향은 상관 없음. (사각형만 그리면 됨) -> 정사각형 x
            - 정사각형 아니라서 이런 모양도 됨
            - 오른쪽 아래 방향으로 1칸
            - 왼쪽 아래 방향으로 3칸
            - 왼쪽 위 방향으로 1칸
            - 오른쪽 위 방향으로 3칸
            
            : (우하, 좌상), (좌하, 우상)은 각각 같은 크기만큼 이동해야함
            
        2. 한 자리 맴돌기 안된다.
            : 한 방향으로 최소, 1칸은 이동해야한다.
            : 한 방향으로 최대 N-1칸 까지만 이동가능하다.
            
        3. 범위를 벗어날 수 없음.
            : col은 조사가능 범위가 1 ~ N-2 까지
            : row의 조사가능 범위 index는 N-3 까지
            
        4. 갔던 곳 또 갈 수 없다.
        
        5. 도중에 같은 종류 중복 불가
    
    '''
    
    # 완전탐색
    #  3. 범위를 벗어날 수 없음.
    # : col은 조사가능 범위가 1 ~ N-2 까지
    # : row의 조사가능 범위 index는 N-3 까지
    for x in range(N-2):
        for y in range(1, N-1):
            search(x, y)
    print(f'#{tc} {result}')