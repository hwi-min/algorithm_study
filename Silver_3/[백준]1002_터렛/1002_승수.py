# 조규현, 백승환 각각의 좌표(x, y)를 원점,
# 각각이 계산한 류재명과의 거리 r을 반지름으로 하는 원을 생각하면 된다.
# 따라서 류재명이 있을 수 있는 좌표의 수는
# 두 원이 같을 때 무한대 (-1), 만나지 않을 때 0,
# 서로 다른 두 점에서 만날 때 2, 한 점에서 접할 때 1 네 가지 경우의 수밖에 없다.

import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().strip().split())
    # 조규현과 백승환 사이의 거리
    distance = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    
    # 둘 사이의 거리가 0(같은 위치)이고,
    # 류재명과의 거리(반지름)가 같다면 위치의 개수는 무한대
    if (distance == 0) and (r1 == r2):
        print(-1)
    # 둘 사이의 거리가 반지름을 합한 값보다 크거나
    # 반지름의 차이보다 작다면 (두 원이 만나지 않으므로) 위치의 개수는 0
    elif (distance > r1 + r2) or (distance < abs(r1 - r2)):
        print(0)
    # 둘 사이의 거리가 반지름의 합과 같거나 차와 같다면 (접했으므로) 위치의 개수는 1
    elif (distance == r1 + r2) or (distance == abs(r1 - r2)):
        print(1)
    # 이외의 경우 (두 원이 두 점에서 만났으므로) 위치의 개수는 2
    else:
        print(2)