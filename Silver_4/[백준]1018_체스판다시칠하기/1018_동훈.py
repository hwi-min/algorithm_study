# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
# 결국엔 맨 위쪽이 흰색인 경우와 검은색인 경우 두가지이다.

# 체스판처럼 칠해져 있다는 보장이 없기에 8x8크기의 체스판으로
# 잘라낸 후 몇 개의 정사각형을 다시 칠한다.

# 다시 칠해야하는 정사각형의 최소 개수를 구함

N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
min_change = 64
# 완전탐색
for start_row in range(N-7):
    for start_col in range(M-7):
        # 하나를 기준으로 삼고 다른건 64-count로 계산함.
        count = 0
        for i in range(start_row,start_row+8):
            for j in range(start_col,start_col+8):
                # i + j의 합이 짝수인지 홀수인지에 따라 값이 달라짐
                # 짝수일때는 처음과 같음
                if (i + j) % 2 == 0:
                    if chess[i][j] != chess[start_row][start_col]: count += 1
                else:
                    if chess[i][j] == chess[start_row][start_col]: count += 1
        min_change = min(min_change, min(count, 64-count))       
           
print(min_change)

