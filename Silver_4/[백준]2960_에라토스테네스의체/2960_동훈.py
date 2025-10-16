'''
    1. 2~N까지 모든 정수를 적음
        2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다.
            이를 P라고 하고, 이 수는 소수이다.
        3. P를 지우고 아직 지우지 않은 P의 배수를 크기 순서대로 지움
    4. 수가 남아 있으면 2번으로 돌아감
'''
N, K = map(int, input().split())

# 숫자 배열 초기화
numbers = [True] * (N+1)

# 0,1은 소수아니라 false 처리
numbers[0], numbers[1] = False, False

cnt = 0
prime = 0
while cnt < K:
    
    for i in range(2, N+1):
        if numbers[i]:
            # True인 숫자 중 가장 작은 것이 소수
            prime = i
            break
        
    for i in range(prime,N+1,prime):
        if numbers[i]:
            # 지워지지 않은 숫자면 지움
            # print(prime, i, cnt)
            numbers[i] = False
            cnt += 1
        if cnt == K:
            print(i)
            break