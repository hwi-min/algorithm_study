# 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다.
# 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

N, M = map(int, input().strip().split())
board = [input().strip() for _ in range(N)]

# 최대로 다시 칠해야 하는 횟수는 64번
repaint = 64

# 8 X 8 크기의 체스판으로 자른 모든 경우의 수 구하기
for x in range(N - 7):
    for y in range(M - 7):
        # 다시 칠해야 하는 횟수
        cnt = 0

        # 맨 왼쪽 위 칸이 흰색인 경우와 비교
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    expected = 'W'
                else:
                    expected = 'B'

                # expected와 다르다면 다시 칠해야 하므로 cnt++
                if board[x + i][y + j] != expected:
                    cnt += 1
        # 64 - cnt는 맨 왼쪽 위 칸이 검은색인 경우에서의 cnt
        repaint = min(repaint, cnt, 64 - cnt)

print(repaint)