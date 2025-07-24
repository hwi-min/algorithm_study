from collections import deque
n = int(input())
queue = deque()

for _ in range(n) :
    com = list(input().split())
    if com[0] == "push" :
        queue.append(com[1])
    elif com[0] == "pop" :
        if not queue : print(-1)
        else : print(queue.popleft())
    elif com[0] == "size" :
        print(len(queue))
    elif com[0] == "empty" :
        if queue : print(0)
        else : print(1)
    elif com[0] == "front" :
        if not queue : print(-1)
        else : print(queue[0])
    elif com[0] == "back" :
        if not queue : print(-1)
        else : print(queue[-1])