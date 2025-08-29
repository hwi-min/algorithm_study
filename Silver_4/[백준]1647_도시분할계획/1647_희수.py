def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False

    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1
    return True


n, m = map(int, input().split()) # 집 개수, 길 개수
info = []
for _ in range(m):
    A, B, c = map(int, input().split())
    info.append((c, A, B))

info.sort()
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)
total = 0
cnt = 0
big = 0

for c, A, B in info:
    if union(A, B):
        total += c
        cnt += 1
        big = max(big, c)
        if cnt == n - 1:
            break

print(total - big)