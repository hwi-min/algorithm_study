# 입력
# 첫째 줄에 단어의 수 N이 주어진다. (1 ≤ N ≤ 100)

# 다음 N개 줄에는 A와 B로만 이루어진 단어가 한 줄에 하나씩 주어진다.
# 단어의 길이는 2와 100,000사이이며, 모든 단어 길이의 합은 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 좋은 단어의 수를 출력한다.


good_count = 0

n = int(input())

for _ in range(n):
    stack = []  # 단어를 담을 스택
    good_word = input()
    
    for ch in good_word:
        if stack and stack[-1] == ch: stack.pop()  # 스택이 비어있지 않고 같은 문자가 인접해있으면 pop
        else: stack.append(ch)  # 스택이 비어있거나 같은 문자가 인접하지 않았으면 push
        
    if not stack: good_count += 1  # 스택이 비어있다면 짝이 다 맞았단 뜻이므로 count 증가

print(good_count)