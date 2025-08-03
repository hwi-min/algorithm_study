n = int(input()) # 컴퓨터의 수 0 ~ 100
m = int(input()) # 커플 수
couples = [list(map(int, input().split())) for _ in range(m)] # 연결 쌍 정보
connect = [[i+1] for i in range(n)] # 연결된 그룹 인덱스 별로 담을 리스트

for a, b in couples :
    group_a = group_b = -1 # 연결 된 컴퓨터 그룹 인덱스 정보 초기화
    for i in range(len(connect)) : 
        if a in connect[i] : 
            group_a = i # 본인 값 있으면 그 인덱스 값 저장
        if b in connect[i] :
            group_b = i # 본인 값 있으면 그 인덱스 값 저장
        
    if group_a != group_b : # 연결된 두 값의 연결 그룹이 다르면 그룹 서로 합침
        if group_a < group_b : # 인덱스 정렬 안망가지게 하려면 순서 맞춰야 함
            connect[group_a] += connect[group_b]
            connect.pop(group_b) # 합쳐진 그룹 원본은 제거
        else :
            connect[group_b] += connect[group_a]
            connect.pop(group_a)

for group in connect :
    if 1 in group : # 다 합친 후 1번 컴퓨터 있는 그룹 개수 출력
        print(len(group)-1)
        break
