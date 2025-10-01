# 포도주 잔이 일렬로 놓여있고, 효주는 다음과 같은 규칙에 따라 포도주를 마시려고 한다.
# 1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
# 2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.

# 효주가 마실 수 있는 최대 포도주의 양을 구합시다.

grape_count = int(input())  # 포도주 잔의 개수
grape_amount = list(int(input()) for _ in range(grape_count))   # 각 포도주 잔에 들어있는 포도주의 양


# 만일 포도주 잔이 2잔 이하라면, 다 마셔 버리기
if grape_count <= 2:
    print(sum(grape_amount))

# 포도주 잔이 3잔 이상이라면, 규칙에 따라 마셔 버리기
else:
    # max_grape_amount[i] : (i + 1)번째 포도주 잔까지 고려했을 때, 마실 수 있는 최대 포도주의 양
    max_grape_amount = [0] * grape_count

    # 초기값 설정
    max_grape_amount[0] = grape_amount[0]
    max_grape_amount[1] = grape_amount[0] + grape_amount[1]
    max_grape_amount[2] = max(
        grape_amount[0] + grape_amount[2],  # 두 번째 포도주를 마시지 않는 경우
        grape_amount[1] + grape_amount[2],  # 첫 번째 포도주를 마시지 않는 경우
        max_grape_amount[1]                 # 첫 번째, 세 번째 포도주를 마시지 않는 경우
        )

    # 규칙에 따라 max_grape_amount 배열 채우기
    for i in range(3, grape_count):
        max_grape_amount[i] = max(
            max_grape_amount[i-1],  # 현재 포도주를 마시지 않는 경우
            max_grape_amount[i-2] + grape_amount[i],    # 이전 포도주를 마시지 않는 경우
            max_grape_amount[i-3] + grape_amount[i-1] + grape_amount[i] # 현재 포도주와 이전 포도주를 마시고, 그 이전 포도주를 마시지 않는 경우
            )

    print(max_grape_amount[-1])