from collections import deque

N = int(input())
queue = deque()
result = []

for _ in range(N):
    command = input()

    if command.startswith('push'):
        cmd, num = command.split()
        queue.append(int(num))

    elif command == 'pop':
        result.append(queue.popleft() if queue else -1)

    elif command == 'size':
        result.append(len(queue))

    elif command == 'empty':
        result.append(1 if not queue else 0)

    elif command == 'front':
        result.append(queue[0] if queue else -1)

    elif command == 'back':
        result.append(queue[-1] if queue else -1)

for n in result:
    print(n)