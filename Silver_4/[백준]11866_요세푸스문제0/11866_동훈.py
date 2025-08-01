# 요세푸스 문제는 다음과 같다.

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 
# 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 
# (N, K)-요세푸스 순열이라고 한다. 
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

from collections import deque

N, K = map(int, input().split())
# N명의 사람을 1부터 N까지의 숫자로 표현
queue = deque(range(1, N + 1))
ans = []
for i in range(N):
    # k만큼 앞에서 뒤로 이동
    for _ in range(K-1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())
    
# 결과를 출력 형식에 맞게 조정
anwer = ", ".join(map(str, ans))
print(f"<{anwer}>")
