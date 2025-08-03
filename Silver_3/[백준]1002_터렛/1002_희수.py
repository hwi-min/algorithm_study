t = int(input())
for _ in range(t) :
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5 # 두 좌표의 거리 값
    answer = 0

    # 각 좌표를 중심으로 r1, r2를 반지름으로 한 원을 그리면, 류재명은 그 원 위에 위치할 것
    # 두 원이 만나는 점의 개수가 류재명이 위치할 수 있는 개수

    if x1 == x2 and y1 == y2 : # 두 좌표가 일치할 경우
        if r1 == r2 : # 반지름도 같으면 완전 일치 (점점이 무한대)
            answer = -1
        else : answer = 0 # 반지름 다르면 안만남
    else :
        if distance > r1 + r2 : # 두 반지름 합한 값보다 거리가 더 멀면 안만남
            answer = 0
        elif distance == r1 + r2 : # 한 점에서 외접
            answer = 1
        elif distance == abs(r1 - r2) : # 한 점에서 내접
            answer = 1
        elif abs(r1 - r2) < distance < r1 + r2 : # 두 점에서 외접
            answer = 2
        else : answer = 0 # 그 외 안만남
    
    print(answer)
