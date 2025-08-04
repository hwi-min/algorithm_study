N = int(input())
relationship = [input().strip() for _ in range(N)]

max_friends = 0

for i in range(N): # 모든 사람들을 순회
    relation = set() # 중복처리

    # 직접 연결된 친구 정보 탐색
    for j in range(N): # 사람 i과 타인 j에 대한 관계
        if relationship[i][j] == 'Y' and i != j: # i==j인 경우 본인이므로 의미가 없음
            relation.add(j)

    # 간접적으로 연결된 친구 정보 탐색
    for k in range(N): # k는 중간 친구
        if relationship[i][k] == 'Y' and i != k: # i와 k가 친구이고 (본인 제외)
            for j in range(N):
                if relationship[k][j] == 'Y' and k != j and i != j: # k와 j가 친구이면 (본인 제외)
                    relation.add(j) # relation에 추가
    
    max_friends = max(max_friends, len(relation))

print(max_friends)