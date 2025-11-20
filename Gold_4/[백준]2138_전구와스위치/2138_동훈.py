'''
    N개의 전구들을 우리가 만들고자 하는 상태로 만드려면 스위치를 최소 몇 번 누르면 되는지.
'''
N = int(input())
state = list(map(int,input()))
state_2 = state[:]
goal = list(map(int,input()))

'''
    이전의 변화만 보면 됨.
    이전게 변해야 하면 이번거를 누름.
    
    다 돌고 오른쪽 끝에서 만들 수 없으면 -1 출력
'''
ans = 0
ans2 = 1
state_2[0] ^= 1 # XOR 비트연산
state_2[1] ^= 1
# print(state, state_2)
for i in range(1,N):
    if i < N-1:
        if goal[i-1] != state[i-1]: # 누르기
            state[i-1] ^= 1
            state[i] ^= 1
            state[i+1] ^= 1
            ans += 1
        if goal[i-1] != state_2[i-1]: # 누르기
            state_2[i-1] ^= 1
            state_2[i] ^= 1
            state_2[i+1] ^= 1
            ans2 += 1
    else:
        if goal[i-1] != state[i-1]: # 누르기
            state[i-1] ^= 1
            state[i] ^= 1
            ans += 1
        if goal[i-1] != state_2[i-1]: # 누르기
            state_2[i-1] ^= 1
            state_2[i] ^= 1
            ans2 += 1
        
#     print(i, state, state_2)

# print(state, ans)
# print(state_2, ans2)
cand1, cand2, target = "".join(map(str,state)), "".join(map(str,state_2)),  "".join(map(str,goal))

if cand1 == target: print(ans)
elif cand2 == target: print(ans2)
else: print(-1)