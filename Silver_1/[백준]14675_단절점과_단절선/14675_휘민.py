# ing ...

N = int(input())
adj = [[] for _ in range(N+1)]
edges = []

for _ in range(N):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    edges.append((a, b))

Q = int(input())
for _ in range(Q):
    t, k = map(int, input().split())
    if t == 2:
        print('yes')

    else:
        if edges[k]