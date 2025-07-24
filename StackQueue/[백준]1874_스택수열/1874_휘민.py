N = int(input())
target_list = [int(input()) for _ in range(N)] #target 리스트 저장
stacked = []
result= []
current = 1 # 시작 1로 지정

for num in target_list: # target 숫자를 도는 동안
    while current <= num: # target 보다 작은 수를 stack에 저장
        stacked.append(current)
        result.append('+') # + 추가
        current += 1 # current 1 증가 (target과 같은 숫자가 등장 할 때까지 push)

    if num == stacked[-1]: # target 숫자와 지금 숫자가 동일하면
        stacked.pop() # pop
        result.append('-') 

    else: # 그렇지 않다면 수열 완성 불가 하므로 'NO'
        print('NO')
        exit()

for r in result:
    print(r)
