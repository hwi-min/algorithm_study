n, *heights = map(int, input().split())  # 첫 값은 막대 개수 n, 이후는 히스토그램 높이들

stack = []       # 인덱스를 저장할 스택
answer = 0       # 최대 직사각형 넓이 저장

for i in range(n):
    # 현재 막대 높이가 스택 top보다 낮으면 직사각형 확정
    while stack and heights[stack[-1]] > heights[i]:
        h = heights[stack.pop()]                     # 직사각형 높이 = pop된 막대의 높이
        w = i if not stack else i - stack[-1] - 1    # 너비 계산: 스택이 비면 처음부터, 아니면 이전 인덱스 사이
        answer = max(answer, h * w)                  # 넓이 갱신
    stack.append(i)                                  # 현재 인덱스 push

# 남은 막대 처리
while stack:
    h = heights[stack.pop()]                         # 스택에서 꺼낸 막대 높이
    w = n if not stack else n - stack[-1] - 1        # 오른쪽 끝까지 확장 가능
    answer = max(answer, h * w)                      # 넓이 갱신

print(answer)  # 최댓값 출력
