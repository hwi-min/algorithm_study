# 시험장의 개수 N
N = int(input())

# 시험장에 있는 응시자 수
A = list(map(int, input().split()))

# B 총 감독관이 한 시험장에서 감시할 수 있는 응시자 수
# c 부 감독관..
B, C = map(int, input().split())

total = 0

for Ai in A:
    if Ai <= B: total +=1; continue
    elif Ai < 0: continue
    elif Ai > B: Ai -= B; total += 1
    total += Ai // C
    if Ai % C > 0 : total += 1
print(total)