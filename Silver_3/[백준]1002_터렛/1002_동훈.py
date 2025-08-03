# 상대편 마린의 위치를 계산해야 함
# 두명의 직원은 각각 자신의 터렛 위치에서 적까지의 거리계산
# 각 좌표가 (x,y)주어지고, 좌표에서 적까지의 거리(r)
# 가 주어질 때, 적이 있을 수 있는 좌표의 수를 출력

# 테스트 케이스가 주어지고
# 각 테케는 x1, y1, r1, x2, y2, r2로 주어짐
# 위치의 수가 무한대일 경우는 -1을 출력함.
import math

T = int(input())

positions = [list(map(int, input().split())) for _ in range(T)]

# 류재명의 위치는 각 점에서 떨어진 원의 둘레 위에 존재할 수 있음
# 1. 원끼리 접할때 : 1 or 2
# 2. 원끼리 접하지 않거나, 포함관계일때 : 0
# 3. 위치와 거리가 같을때 : 무한대

for position in positions:
    # 터렛 사이의 거리
    turret_distance = math.sqrt(((position[0]-position[3])**2)
    + ((position[1]-position[4])**2))
    # 마린까지의 거리 합
    sum_marine_distance = position[2] + position[5]
    diff_abs_marine = abs(position[2] - position[5])

    #print(turret_distance, sum_marine_distance, diff_abs_marine)
    # 1. 터렛이 같은 위치일 때
    if turret_distance == 0:
        if position[2] == position[5]: print(-1) # 무한대
        else : print(0) # 0개

    # 2. 교점이 2개인 경우 : 두 원이 두점에서 만나는 경우
    elif diff_abs_marine < turret_distance < sum_marine_distance : print(2)
    
    # 3. 교점이 1개인 경우 : 외접하거나 내접할 때
    elif turret_distance == diff_abs_marine or turret_distance == sum_marine_distance: print(1)
    
    # 4. 교점이 0개인 경우 : 멀리 떨어져 있거나 포함해서 만나지 않을 때
    elif turret_distance > sum_marine_distance or turret_distance < diff_abs_marine: print(0)
    
    