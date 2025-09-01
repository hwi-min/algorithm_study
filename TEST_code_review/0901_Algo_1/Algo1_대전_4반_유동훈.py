'''
    N 개의 우주 정거장이 있으며 각 번호는 1~N까지다.
    모든 우주 정거장을 연결하는 최소 비용의 통신 네트워크를 구축하는 것
    만약 모든 정거장을 연결하는 것이 불가능하다면 -1을 반환

    모든 정거장을 연결해야 함. -> 최소신장트리
'''

import sys

sys.stdin = open('algo1_sample_in.txt', 'r')

T = int(input())

def find_set(x):
    # 현재 노드가 부모 노드가 아니면
    if parent[x] != x:
        # 부모노드를 찾아감, 경로 압축
        parent[x] = find_set(parent[x])
    return parent[x]

# 합집합 함수
def union_set(x,y):
    root_x = find_set(x)
    root_y = find_set(y)
    # 만약 각 노드의 루트가 다르다면 다른 집합에 있는 것
    if root_x != root_y:
        # x가 포함된 집합의 랭크가 더 크다면
        if rank[root_x] > rank[root_y]:
            parent[root_y] = parent[root_x]
            rank[root_x] += 1
        elif rank[root_y] > rank[root_x]:
            parent[root_x] = parent[root_y]
            rank[root_y] += 1
        else: # 경우에 따라 다름
            rank[root_x] > rank[root_y]
            parent[root_y] = parent[root_x]
            rank[root_x] += 1
        return True
    else:# 같다면 합집합 실패
        return False

for tc in range(1,T+1):

    # N 우주 정거장의 수, 가능한 연결의 수 M(간선 수)
    N, M = map(int, input().split())
    
    # 각 연결에 대한 정보
    # Xi, Yi, costi
    edges = [list(map(int, input().split())) for _ in  range(M)]
    edges.sort(key=lambda x : x[2])

    # 최소신장트리를 만들기 위해 서로소 집합 생성
    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)
    answer = 0
    mst = [] # 간선의 개수 총 N-1개
    for s,e,w in edges:
        if union_set(s,e):
            mst.append((w,s,e))
            answer += w
    
    if len(mst) != N-1:
        answer = -1

    print(f'#{tc} {answer}')