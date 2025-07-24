n = int(input())
num = [int(input()) for _ in range(n)]
stack = []
answer = []
a = 0 

for i in range(1, n+1) :
    stack.append(i)
    answer.append('+')
    while stack and stack[-1] == num[a] :
        stack.pop()
        answer.append('-')
        a += 1

if not stack :
    for a in answer :
        print(a)
else :
    print("NO")