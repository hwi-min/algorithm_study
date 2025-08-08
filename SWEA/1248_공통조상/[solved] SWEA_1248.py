import sys
sys.stdin = open('input_1248.txt')

# 각 노드의 조상 찾기: 
def find_all_ancestor(n1, n2, parents):
    # n1에 대한 조상들을 저장할 집합
    n1_set = set() # 조상을 저장할 set
    current = n1 # 현재 노드를 n1로 저장

    while current != 0: # node가 0이 아닌 동안 순회 (즉, 노드의 부모가 없는 경우(0)까지 반복) / 초기에 parents를 0으로 초기화했으므로 부모정보가 없는(0) 경우 루트 노드이거나 리프 노드
        n1_set.add(current) # 조상 set에 저장
        """
        n1_set에 자기 자신도 포함시키면 안되지 않나?
        -> 가능함: 자기 자신도 자신의 조상이라고 봄
        """
        current = parents[current] # 노드 업데이트

    # n2 조상 확인하며 겹치는지 확인
    current = n2
    while current != 0:
        if current in n1_set:
            return current
        current = parents[current]

    return 0

# 서브트리의 개수 세기
def cnt_subtree(node): # 서브트리의 부모 노드를 입력 받음
    cnt = 1 # 자기 자신 포함

    for child in children[node]: # 자식정보를 담은 리스트를 순회하면서
        cnt += cnt_subtree(child) # 카운트 증가

    return cnt


T = int(input())
for t in range(1, T+1):
    # 정점개수, 간선개수, 타겟정점1, 타겟정점2
    V, E, n1, n2 = map(int, input().strip().split())
    infos = list(map(int, input().strip().split()))
    parents = [0] * (V+1) # 인덱스의 부모 노드만 저장된 리스트 (부모정보)
    children = [[] for _ in range(V+1)] # 1-based이므로 V+1개 생성 / 인덱스의 자식노드만 저장된 리스트 (자식정보)

    # 부모와 자식 node 정보 저장
    for i in range(0, len(infos), 2): # 2씩 증가시키면서
        parent_node, child_node = infos[i], infos[i+1] # 부모노드, 자식노드
        parents[child_node] = parent_node # 해당 인덱스(노드)의 직속부모 저장
        children[parent_node].append(child_node) # 해당 인덱스(노드)의 자식노드 저장

    # 1.공통 조상 찾기 (가장 먼저 등장하는 동일한 부모 노드가 가장 가까운 부모 노드가 됨)
    common_ancestor = find_all_ancestor(n1, n2, parents) # 하나의 int로 반환

    # 2. 가장 가까운 공통 조상으로부터 서브트리의 개수 세기 (본인 포함)
    sub_tree_node = cnt_subtree(common_ancestor)

    print(f"#{t} {common_ancestor} {sub_tree_node}")


