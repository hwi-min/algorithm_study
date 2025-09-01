
to_alpha = {1: 'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:"Q", 18:"R",19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:'Z' }

direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split()) # N: 가로크기, M: 세로크기
    K = int(input()) # 세균 종류 수 (A부터 ~) #1 -> A, 4면 1~4 (1, K+1)
    max_sizes = [0] + list(map(int, input().split()))  # 최대 증식 가능 크기
    lab = [list(input().split()) for _ in range(M)] # ['.', '.', 'A', 'A', '.', '.', '.', 'A', 'A', '.', '.']

    # 전체 알파벳을 돌면서
    while sum(max_sizes) > 0:
        added = set()

        for k in range(1, K + 1): # 1
            if max_sizes[k] - 1 >= 0: # [2]
                max_sizes[k] -= 1 # 1번 연산할거니까 미리 빼주고

                for i in range(M):  # 가로
                    for j in range(N):  # 세로

                        alpha = lab[i][j]
                        if (i, j) not in added and (alpha == to_alpha.get(k)):  # k번째 알파벳과 lab[i][j]의 값이 같으면
                            for dx, dy in direction:  # 사방면을 확인하면서 업데이트
                                nx, ny = i + dx, j + dy

                                if 0 <= nx < M and 0 <= ny < N and lab[nx][ny] == '.':
                                    lab[nx][ny] = alpha
                                    added.add((nx, ny))

            elif max_sizes[k] - 1 < 0:  # 남은 기회가 없는 경우는
                continue  # 다음 순회로 돌아감

        # 턴이 바뀌면 이전 턴에서 바이러스를 퍼뜨리지 못하는 애들이 바이러스를 이제 퍼뜨릴 수 있어야 하니까
        added = set()

    print(f"#{t}")
    for i in range(M):
        print(" ".join(lab[i]))
