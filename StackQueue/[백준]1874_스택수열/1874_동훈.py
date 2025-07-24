# 스택에 넣을 숫자
num = 0
stack = [] 
answer = [] # 정답 리스트
sequence = [] # 수열 리스트
correct = True
N = int(input())

# 수열 입력 받기
for i in range(N):
    sequence.append(int(input()))

# stack empty 방지 더미 push
stack.append(num)
num += 1


for i in range(N):    
    # stack top이 수열과 일치할 때 까지 push
    while stack[-1] < sequence[i]:
        stack.append(num)
        num += 1
        answer.append("+")
    
    # 수열과 stack top이 일치하면 pop
    if stack[-1] == sequence[i]:
        stack.pop()
        answer.append('-')
    else: # 다르다면 중복되었거나 더 큰 숫자
        correct = False
    #print(stack, sequence[i])

if correct:
    for i in range(len(answer)):
        print(answer[i])
else:
    print("NO")
    