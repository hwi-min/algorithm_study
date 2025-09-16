'''
    양수와 +, - 그리고 괄호를 가지고 식을 만들고, 괄호를 모두 지움.
    그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 함.    
'''
from collections import deque

equation = str(input())
ops = ['+', '-']
operand = deque()
operator = deque()
number = ''
stack_number = deque()

operator.append('+') # 처음엔 플러스
for st in equation: 
    if st in ops:
        operator.append(st)
        operand.append(int(number))
        number = '' # 숫자 초기화
    else:
        number += st
        
operand.append(int(number)) # 마지막 숫자

'''
    만약 마이너스라면? 나중에 수행해야함.
    플러스라면? 현재 operator에 연결된 숫자 더해서 넣어줌
'''
# print(operator,operand)

for op in operator:
    # print(op, operand)
    if op == '-': # 마이너스면 숫자 그냥 넣기
        stack_number.append(int(operand.popleft()))
    else: # 플러스이면 스택에서 빼고 더한다음 다시 넣기
        if stack_number:
            stack_number.append(stack_number.pop() + int(operand.popleft()))
        else:
            stack_number.append(int(operand.popleft()))

while len(stack_number) > 1:
    a = stack_number.popleft()
    b = stack_number.popleft()
    stack_number.appendleft(a-b)

print(stack_number[0])