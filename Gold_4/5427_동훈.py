from collections import deque

n = int(input())

for _ in range(n):
    
    # 빌딩의 너비 w, 높이 h
    w, h = map(int, input().split())

    building = [list(input()) for _ in range(h)]
    fire_pos = deque()
    dog_queue = deque()

    visited = [[True] * w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*': # 불이면
                fire_pos.append((i,j,0))
                visited[i][j] = False
            if building[i][j] == '@': # 상근이면
                dog_queue.append((i,j,0))
                building[i][j] = '.'
    # print(fire_pos)
    # print(dog_queue)
    '''
        bfs로 돌며 한번 돌 때 마다 불을 퍼트림
        불이 먼저 퍼지고, 상근이가 이동함.
    '''
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    answer = -1
    

    while dog_queue:
        row, col, curr_time = dog_queue.popleft()
        visited[row][col] = False
        
        # 종료조건 : 상근이가 가장자리에 도착하면
        if row in [0, h-1] or col in [0, w-1]:
            # print(row,col,curr_time)
            answer = curr_time + 1
            break
        
        # 불이 먼저 이동
        while fire_pos:
            # 현재 시간에 이동할 불만 이동
            if fire_pos[0][2] != curr_time: break
            
            f_row, f_col, f_time = fire_pos.popleft()
            
            for i in range(4):
                nf_row, nf_col = f_row + dy[i], f_col + dx[i]
                if 0 <= nf_row < h and 0 <= nf_col < w:
                    if building[nf_row][nf_col] == '.': # 빈공간으로 이동
                        building[nf_row][nf_col] = '*'
                        fire_pos.append((nf_row, nf_col, f_time + 1))
        
        # 상근이 이동
        for i in range(4):
                n_row, n_col = row + dy[i], col + dx[i]
                if 0 <= n_row < h and 0 <= n_col < w and visited[n_row][n_col]:
                    # 벽이 아니고, 불이 아니면 이동 가능
                    if building[n_row][n_col] != '#' and building[n_row][n_col] != '*':
                        dog_queue.append((n_row, n_col, curr_time + 1))
                        visited[n_row][n_col] = False
        
        # print('현재 시간: ', curr_time)
        # print('현재 불')
        # for row in building:
        #     print(row)
        # print('빌딩 높이',h,'빌딩너비',w)
        # print('현재 상근이 가능 위치', dog_queue)

        
    # for row in building:
    #     print(row)
        
    if answer == -1:
        print('IMPOSSIBLE')
    else:
        print(answer)