# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다.
# 이제 순서대로 K번째 사람을 제거한다.
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 1,000)

# 출력
# 예제와 같이 요세푸스 순열을 출력한다.

# 예제 입력 1 
# 7 3
# 예제 출력 1 
# <3, 6, 2, 7, 5, 1, 4>


from queue import Queue
perm = Queue()  # 순열을 저장할 queue

N, K = map(int, input().split())

for person in range(1, N + 1):  # 사람 앉히기
    perm.put(person)

print('<', end='')

while(True):
    for _ in range(K - 1):
        perm.put(perm.get())  # K번째 사람 전까지 queue 뒤로 보내기

    remove = perm.get()  # K번째 사람 제거
    
    # queue에 사람이 남아있다면 (아직 앉아있는 사람이 있다면) 콤마 찍고 while문 진행
    if not perm.empty():
        print(f'{remove}, ', end='')
    # queue에 사람이 남아있지 않다면 (앉아있는 사람이 없다면) 콤마 찍지 않고 종료
    else:
        print(remove, end='')
        break

print('>')