'''
    복구시간이 가장 짧은 경로에 대한 총 복구시간을 구하시오
'''
import sys
import heapq

sys.stdin = open('input.txt', 'r')

t = int(input())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dijkstra():
    heap = []
    heapq.heappush(heap, (0,0,0)) # 지금까지의 거리와 좌표를 추가

    while heap:
        dist, row, col = heapq.heappop(heap)
        for i in range(4):
            ny, nx = row + dy[i], col + dx[i]

            if 0 <= ny < N and 0 <= nx < N:
                # 거리를 계산함
                if distance[ny][nx] > dist + war[ny][nx]:
                    distance[ny][nx] = dist + war[ny][nx] # 거리를 갱신하고
                    heapq.heappush(heap, (distance[ny][nx], ny, nx)) # 갱신된 위치에서 새로 찾음
    return distance[N-1][N-1]


for tc in range(1, t+1):

    # 지도의 크기
    N = int(input())

    # 지도 정보
    war = [list(map(int, input())) for _ in range(N)]
    distance = [[float('inf')] * N for _ in range(N)]

    print(f'#{tc} {dijkstra()}')