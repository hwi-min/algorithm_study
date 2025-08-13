import sys
sys.stdin = open('sample_input.txt')

from collections import deque

def rotation(num, direct):
    # 각 자석의 회전 방향 저장할 리스트
    # 0: 회전 안함, 1: 시계 방향 회전, -1: 반시계 방향 회전
    rotate_dir = [0] * 4
    rotate_dir[num] = direct    # 전달받은 자석은 회전방향 결정

    # num 번째 자석의 왼쪽 체크
    for i in range(num - 1, -1, -1):
        if mag_deque[i][2] != mag_deque[i + 1][6]:  # 인접 날의 극성이 다르면
            rotate_dir[i] = -rotate_dir[i + 1]  # 반대로 회전
        else: break     # 극성이 같으면 회전 전파 중지

    # num 번째 자석의 오른쪽 체크
    for i in range(num + 1, 4):
        if mag_deque[i][6] != mag_deque[i - 1][2]:  # 인접 날의 극성이 다르면
            rotate_dir[i] = -rotate_dir[i - 1]  # 반대로 회전
        else: break     # 극성이 같으면 회전 전파 중지

    # 모든 자석 동시에 회전 실행
    for i in range(4):
        # rotate_dir[i]가 1이면 시계방향 회전, -1이면 반시계 방향 회전
        mag_deque[i].rotate(rotate_dir[i])


T = int(input())
for tc in range(1, T + 1):
    K = int(input())    # 자석을 회전시키는 횟수
    score = 0   # 획득한 점수
    # 자석의 자성 정보 (0: N극, 1: S극)
    magnetic = [list(map(int, input().split())) for _ in range(4)]
    # 각 자석을 deque 으로 저장
    mag_deque = [deque(magnetic[i]) for i in range(4)]

    # K번 회전시키기
    for _ in range(K):
        # number: 회전시킬 자석 번호, direction: 회전 방향(1: 시계, -1: 반시계)
        number, direction = map(int, input().split())
        rotation(number - 1, direction) # idx 는 0부터 시작하므로 -1 해주기

    # 회전 종료 후 모든 자석의 화살표 위치 자성 확인해서 점수 갱신
    for i in range(4):
        if mag_deque[i][0] == 1:    # S극 이면
            score += 1 << i         # 점수 증가

    print(f'#{tc} {score}')