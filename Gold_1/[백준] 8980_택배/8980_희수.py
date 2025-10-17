n, c = map(int, input().split())
# 마을 수, 트럭 용량
m = int(input())
# 박스 정보 개수
infos = [list(map(int, input().split())) for _ in range(m)]
# 보낸이, 받는이, 박스개수
boxes = []

for info in infos:
    s, r, b = info
    boxes.append((r - s, s, r, b)) # (박스 싣고 가는 거리, 시작점, 도착점, 박스 개수)

boxes.sort(key=lambda x: (x[2], x[0])) # 박스 빨리 내리는 순 -> 박스 싣고 가는 거리 짧은 순 정렬
truck = [0] * (n + 1) # 트럭 공간 계산할 리스트
answer = 0

for box in boxes:
    d, s, r, b = box # 거리, 시작점, 도착점, 박스 개수
    if s == r: continue # 만약 시작점 == 도착점이면 패스
    max_num = max(truck[s:r]) # 박스 싣고가는 동안 가장 많이 싣고 가는 박스의 개수
    if max_num + b < c: # 용량 충분한 경우
        answer += b # 박스 전부 다 담기
        for i in range(s, r):
            truck[i] += b # 트럭 용량 상황 업데이트
    elif max_num < c: # 박스 다 담지는 못하는데, 담을 공간은 있는 경우
        answer += c - max_num # 여유 공간 만큼 담음
        for i in range(s, r):
            truck[i] += c - max_num # 트럭 상황 업데이트

print(answer)