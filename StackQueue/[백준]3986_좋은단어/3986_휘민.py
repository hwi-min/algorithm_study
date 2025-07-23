N = int(input())
cnt = 0

for i in range(N):
    stacked = []
    word = input()
    for current in word:
        if not stacked: # 스택이 비어있다면
            stacked.append(current)
        else: # 스택이 비어있지 않다면
            prev = stacked.pop()
            if prev != current: # 이전 단어와 현재 단어가 다르다면
                stacked.append(prev)
                stacked.append(current)
    if not stacked: # 단어 내 모든 letter을 돈 후, 스택에 남아있는 것이 없다면
        cnt += 1

print(cnt)