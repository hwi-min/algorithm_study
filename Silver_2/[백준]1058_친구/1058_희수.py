n = int(input())
friend = [input() for _ in range(n)]
answer = 0

for i in range(n) :
    two_friend = set() # i번의 2-친구 담을 집합 초기화 (중복 방지)
    for j in range(n) :
        if friend[i][j] == 'Y' : 
            two_friend.add(j) # i번의 직접 친구 j 추가
            for k in range(n) :
                if friend[j][k] =='Y' and k != i : # j번의 직접 친구 탐색
                    two_friend.add(k) #j번의 직접 친구(i번의 2-친구) k 추가
    answer = max(answer, len(two_friend)) # 친구 수 중 큰 값 정답에 저장

print(answer)
