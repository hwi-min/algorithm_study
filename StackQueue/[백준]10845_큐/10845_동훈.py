from collections import deque

queue = deque()
# 총 명령어 수
N = int(input())
command = []
for i in range(N):
    command.append(input().split())

# 큐 기본기능 구현
for i in range(N):
    if command[i][0] == 'push':
        queue.append(command[i][1])
    elif command[i][0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif command[i][0] == 'size':
        print(len(queue))
    elif command[i][0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[i][0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[i][0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

    