t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split()) # 가로, 세로
    k = int(input()) # 세균 종류 수
    limit = list(map(int, input().split())) # 세균 별 최대 증식 크기
    arr = [list(input().split()) for _ in range(m)] # 세균 지도
    # 알파벳 인덱스로 찾기 위한 리스트
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = [i for i in range(len(limit))] # 지도에 존재하는 알파벳들 인덱스 순으로 큐에 넣어놓고 시작

    while queue:
        idx = queue.pop(0) # 가장 첫번째 알파벳(인덱스) 꺼내기

        if limit[idx] <= 0: # 증식 횟수 다 썼으면 건너뛰기
            continue

        spread = [] # 증식 정보 담아둘 리스트
        is_spread = False

        for i in range(m):
            for j in range(n):
                if arr[i][j] == alphabet[idx]: # 이번에 증식할 알파벳을 지도에서 찾으면
                    for d in range(4): # 4방향으로 퍼짐
                        nx, ny = j + dx[d], i + dy[d]
                        if 0 <= nx < n and 0 <= ny < m and arr[ny][nx] == '.': # 지도 안에 있고, 아직 증식 안된 빈 곳이면
                            spread.append((nx, ny)) # 증식 정보에 담아둠
                            is_spread = True # 증식 성공

        if is_spread and limit[idx] > 0: # 증식 성공하고 증식 횟수 아직 남았으면
            limit[idx] -= 1 # 증식 횟수 하나 줄이기
            for x, y in spread:
                arr[y][x] = alphabet[idx] # 증식 정보에 담아둔 대로 실제 지도에 반영
            queue.append(idx) # 알파벳 인덱스 큐 맨 뒤에 넣어주기


    print(f'#{tc}')
    for i in range(m):
        print(' '.join(arr[i]))