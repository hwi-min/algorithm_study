from collections import deque
words = []
N = int(input())
answer = N
for _ in range(N):
    words.append(input())
    
for word in words:
    target = deque(word)
    # 홀수면 무조건 불가능
    if len(word) % 2 == 1:
        answer -= 1
    else:
        # 짝수면 스택을 이용해서 확인
        stack = [0]
        while target:
            # 스택에 문자를 넣고, 스택의 마지막 두 문자가 같으면 제거
            stack.append(target.popleft())
            if stack[-2] == stack[-1]:
                stack.pop()
                stack.pop()
        if len(stack) > 1:
            answer -= 1
print(answer)