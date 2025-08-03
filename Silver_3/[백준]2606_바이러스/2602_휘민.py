from collections import deque

computer_n = int(input().strip())
edge_n = int(input().strip())
adj_lst = [[] for _ in range(computer_n + 1)]
visited = [False] * (computer_n + 1)

# 인접 리스트에 연결 정보 저장하기
for _ in range(edge_n):
    a, b = map(int, input().strip().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)


# bfs 함수 정의
def bfs(node):
    queue = deque([node]) # queue에 시작 node 저장
    cnt = 0 # 감염된 컴퓨터 개수 초기화

    while queue: # queue안에 요소가 들어있는 동안 계속 반복
        current = queue.popleft() 
        visited[current] = True # 꺼내온 후 방문 처리

        for neighbor in adj_lst[current]: # 해당 노드와 연결된 다른 노드들을 모두 순회하며
            if not visited[neighbor]: # 아직 방문하지 않은 경우
                visited[neighbor] = True # 방문처리 후
                queue.append(neighbor) # queue에 삽입
                cnt += 1 # 감염된 컴퓨터 개수 추가
    return cnt

result = bfs(1)
print(result)