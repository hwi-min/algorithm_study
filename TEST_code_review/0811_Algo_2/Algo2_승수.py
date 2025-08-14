def calc_cost(str_c):
    global cost
    stack = []  # C 에서의 각 비용의 깊이를 알아내기 위해 스택 사용
    depth = 0   # 깊이를 나타내기 위한 변수

    for char in str_c:
        if char.isdigit():  # 숫자라면 스택에 넣기
            stack.append(char)
        elif char == '[':   # 여는 괄호라면
            stack.append(char)  # 스택에 넣고
            depth += 1  # 깊이 하나 증가
        elif char == ']':   # 닫는 괄호라면
            while stack and stack[-1] != '[':   # 스택이 비어있지 않고, 스택의 마지막 요소가 '['가 아니라면
                cost += depth * int(stack.pop())    # 스택 안의 숫자와 깊이 곱해서 현재 cost에 더해주기
            stack.pop()     # '['를 스택에서 빼기
            depth -= 1      # 깊이 하나 감소 ('['가 사라졌으므로)
        else: continue      # ',' 는 패스


T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # 유지보수 비용의 요소 수
    C = input()    # 비용
    cost = 0    # 최종 비용

    calc_cost(C)    # 총 비용 계산
    print(f'#{tc} {cost}')