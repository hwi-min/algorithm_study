import math

T = int(input())
for _ in range(1, T+1):
    x1, y1, r1, x2, y2, r2 = map(int, input().strip().split())

    # 두 원의 교점 개수 구하기 (두 터렛에서 측정한 거리로 만들어지는 원의 교점을 찾아야 함)
    # 조건 분기
    # 1. 무한개(-1): 두 원이 완전히 같은 원일 경우
    # 2. 0개
        # - 두 원이 너무 멀어서 만나지 못함: d > r1 + r2
        # - 한 원이 다른 원 안에 존재: d < |r1 - r2|
    # 3. 1개
        # - 외접: d = r1 + r2
        # - 내접: d = |r1 - r2|
    # 4. 2개
        # - 위 경우가 아닌 나머지

    # 두 원의 중심점 사이의 거리 (조규현과 백승환 사이의 직선 거리): 유클리드 거리 공식
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    if d == 0 and r1 == r2: # 완전히 같은 원인 경우
        print(-1)
    elif d > r1 + r2 or d < abs(r1- r2): # 두 원이 너무 멀어서 만나지 못함 or 한 원이 다른 원 안에 존재
        print(0) 
    elif d == r1 + r2 or d == abs(r1- r2): # 외접 or 내접하는 경우
        print(1)
    else:
        print(2)