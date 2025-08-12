import sys
sys.stdin = open('input_2105.txt')

# 방향 정의     우하      좌하      좌상      우
direction = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

def dfs(x, y, current_cnt, )


T = int(input())
for t in range(1, T+1):
    N = int(input())
    cafe_map = [list(map(int, input().strip().split())) for _ in range(N)]
    visited = [[False] * (N) for _ in range(N)]
    print(visited)

