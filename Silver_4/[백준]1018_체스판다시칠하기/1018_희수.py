n, m = map(int, input().split())
arr = [input() for _ in range(n)]
answer = 64

for i in range(n-7) :
    for j in range(m-7) : # 첫번째 칸 기준으로 완전 탐색
        count1 = 0
        count2 = 0 # 첫번째 칸이 'W', 'B'일 2가지 경우의 수
        first_color = arr[i][j]
        for x in range(8) :
            for y in range(8) :
                if (x + y) % 2 == 0 : # 대각선으로 색이 같으므로
                    if arr[i+x][j+y] == first_color :
                        count1 += 1
                    else : count2 += 1
                else :
                    if arr[i+x][j+y] == first_color :
                        count2 += 1
                    else : count1 +=1
        answer = min(answer, count1, count2) # 가장 적게 칠하는 수

print(answer)
        
