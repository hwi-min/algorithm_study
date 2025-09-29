t = int(input())

# -------- 시간 초과 -----------
# for _ in range(t):
#     n = int(input())
#     price = list(map(int, input().split()))
#     answer = 0
#
#     for i in range(n):
#         last = price[i:] # 오늘 이후의 주식 가격들
#         if last[0] == max(last): #오늘이 가장 비싸면 걍 지나가기
#             continue
#         answer += (max(last) - last[0]) # 아니면 가장 비싼날 팔기
#
#     print(answer)


for _ in range(t):
    n = int(input())
    price = list(map(int, input().split()))
    max_price = 0
    answer = 0

    for i in range(n - 1, -1, -1): # 거꾸로 탐색
        if price[i] > max_price: #  오늘이 가장 비싼 날보다 비싸면
            max_price = price[i] # 가장 비싼 날 업데이트
        else :
            answer += (max_price - price[i]) # 아니면 가장 비싼 날 팔기

    print(answer)
