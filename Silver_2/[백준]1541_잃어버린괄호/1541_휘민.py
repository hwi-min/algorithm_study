"""
시간제한 2초 (2억)
-가 나오면 괄호를 열고, -를 다시 만나면 닫음
"""

from collections import deque

inputs = input().strip()
num_list = []
queue = deque()

num = ''
for input in inputs:
    if input.isnumeric():
        num += input
    elif input in ('-', '+'):
        queue.append(int(num))
        num = ''
        queue.append(input)

if num: queue.append(int(num))

total = 0
sub_sum = 0

while queue:
    current = queue.popleft()
    if type(current) == int:  # 숫자인 경우
        total += current  # total에 더한다
    else:  # 숫자가 아닌 경우 -> 연산자인 경우
        if current == '-':  # 연산자 -가 등장하면 -> while을 돌면서 sub_sum을 계산해야 함
            while queue:  # - 이후의 queue를 순회하면서
                next = queue[0]
                if type(next) == int:  # 숫자인 경우
                    next = queue.popleft()
                    sub_sum += next  # sub_sum에 더해줌
                else:  # 연산자인 경우
                    # + 인 경우에는 아무것도 안해도 됨 계속 더할거니까
                    # - 인 경우에는 처리해줘야함
                    if next == "-":
                        total -= sub_sum  # sub_sum을 빼주고
                        sub_sum = 0  # sub_sum 초기화
                        break
                    else: queue.popleft()
            total -= sub_sum  # sub_sum을 빼주고
            sub_sum = 0  # sub_sum 초기화



print(total)


#####################################################################################################
# -> gemini가 알려준 충격적인 사실 ... 그냥 -가 등장하면 그 시점부터 다 빼면 된다 ...
# -> 너무 현타가 오지만 ...
# -> 어쨌든 우리가 괄호를 마음대로 넣어서 -가 등장한 시점부터 다시 -가 등장할때까지 다 더하다가 빼주는 거니까
# -> 그냥 다 빼는거랑 다를 바가 없음 ㅠㅠ
#####################################################################################################

while queue:
    operator = queue.popleft()
    number = queue.popleft()
    
    if operator == '-':
        is_minus = True
    
    if is_minus:
        total -= number
    else:
        total += number

print(total)




