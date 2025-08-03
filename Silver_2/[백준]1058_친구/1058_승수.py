N = int(input())
friends_matrix = []
two_friends = 0

for _ in range(N):
    friends_matrix.append(input().strip())
    
for i in range(N):
    count = 0   # 2-친구의 수

    for j in range(N):
        if i == j:  # i와 j가 같으면 본인이므로 무시
            continue

        if friends_matrix[i][j] == 'Y':     # Y라면 친구이므로 count++
            count += 1
        else:   # N이라도
            # i와 j의 공통친구 k가 있다면 count++ (한 번만 count++ 하고 반복문 빠져나오기)
            for k in range(N):
                if friends_matrix[i][k]=='Y' and friends_matrix[k][j] == 'Y':
                    count += 1
                    break
    # 2-친구 최대값 갱신
    two_friends = max(two_friends, count)

print(two_friends)    