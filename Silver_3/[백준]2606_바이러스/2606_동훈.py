# 네트워크에 연결되어 있는 모든 컴퓨터는 바이러스에 걸림

# 컴퓨터의수가 주어지고
# 직접 연결되어 있는 쌍의 수가 주어진다.
# 그 수 만큼 연결 되어있는 번호 쌍이 주어진다

# 1번 컴퓨터가 바이러스에 걸렸을 때, 총 감염될 컴퓨터 수를 리턴
from collections import defaultdict

# dfs로 순회
def dfs(network, visited, start):
    # 방문처리
    visited.add(start)
    # start에 연결된 node 중
    for node in network[start]:
        # 방문하지 않았으면 
        if node not in visited:
            # dfs 순회
            dfs(network, visited, node)
        
total_computer = int(input())
pair_count = int(input())
network = defaultdict(list)
visited = set()
for i in range(pair_count):
    start, end = map(int, input().split())
    network[start].append(end)
    network[end].append(start)

dfs(network, visited, 1)
print(len(visited)-1)