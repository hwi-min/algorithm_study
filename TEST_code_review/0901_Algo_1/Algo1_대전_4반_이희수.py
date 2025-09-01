def find(x): # 크루스칼 find
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b): #  크루스칼 union
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    elif rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    info = []
    for _ in range(m):
        s, e, w = map(int, input().split())
        info.append((w, s, e)) # 가중치를 우선으로 두고 리스트에 삽입

    parent = [i for i in range(n + 1)] # 부모 담을 리스트
    rank = [0] * (n + 1) # 깊이 담을 리스트
    info.sort() # 가중치 오름차순으로 정렬
    total = 0 # 가중치 더할 답 초기화
    picked = 0 # 고른 개수 저장할 변수
    check = set() # 부모 다른지, 같은지 확인할 set


    for w, s ,e in info:
        if union(s, e): # 둘이 부모 합쳤으면
            total += w # 가중치 더함
            picked += 1 # 개수 1 증가
            check.add(parent[s]) # 합친 후 부모 한개 저장
            if picked == n - 1: # 간선 개수만큼 다 이었으면 끝내기
                break
    if len(check) > 1: # 만약 부모가 다 하나로 안이어졌으면, 정거장들끼리 모두 이어지지 않는다는 뜻
        total = -1 # 즉, 모든 정거장 연결 불가능 -1 출력

    print(f'#{tc} {total}')