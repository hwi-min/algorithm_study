from collections import defaultdict

N = int(input())

# 2-친구
# 두사람이 친구이거나 하나 건너 친구가 존재하면 2-친구수가 +1 됨
# 친구면 Yes 아니면 No

# A : B.    -> 2명
# B : A, C  -> 2 + 1 : 3명
# c : B, D  -> 2 + 1 + 1 : 4명
# D : C, E  -> 2 + 1 : 3명
# E : D     -> 1 + 1 : 2명

data = [list(input()) for _ in range(N)]
# 친구 기록 사전
friends = defaultdict(list)
for i in range(N):
    for j in range(N):
        if data[i][j] == 'Y' and i != j:
            friends[i].append(j)
# print(friends)

max_count = 0
# 2-친구 기록 셋
two_friends = set()
for i in range(N):
    two_friends.clear()
    # i번째 사람의 친구들 set에 add
    for f in friends[i]:    
        two_friends.add(f)
        # 친구들의 친구들 확인
        for ff in friends[f]:
            if ff != i:
                two_friends.add(ff)
#    print(two_friends)

    max_count = max(max_count, len(two_friends))
print(max_count)