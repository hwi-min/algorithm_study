def push(num):
    queue.append(num)
def pop():
    #if not queue: print(-1)
    global front_idx
    if front_idx >= len(queue):
        print(-1)
    else:
        #print(queue.pop(0)) # 이거 때문에 시간초과 났음
        print(queue[front_idx])
        front_idx += 1

def size():
    print(len(queue) - front_idx)

def empty():
    #if not queue: print(1)
    if front_idx >= len(queue):
        print(1)
    else: print(0)

def front():
    #if not queue: print(-1)
    if front_idx >= len(queue):
        print(-1)
    #else: print(queue[0])
    else: print(queue[front_idx])

def back():
    #if not queue: print(-1)
    if front_idx >= len(queue):
        print(-1)
    else: print(queue[-1])


import sys
input = sys.stdin.readline

N = int(input())
queue = []
front_idx = 0

for _ in range(N):
    command = input().strip()
    com = command.split(' ')

    if len(com) != 1:
        push(int(com[1]))
    elif command == 'pop': pop()
    elif command == 'size' : size()
    elif command == 'empty' : empty()
    elif command == 'front' : front()
    elif command == 'back' : back()     
    
    




# import sys
# input = sys.stdin.readline

# N = int(input())
# queue = []
# front_idx = 0

# for _ in range(N):
#     cmd = input().split()
    
#     if cmd[0] == 'push':
#         queue.append(int(cmd[1]))
#     elif cmd[0] == 'pop':
#         if front_idx >= len(queue):
#             print(-1)
#         else:
#             print(queue[front_idx])
#             front_idx += 1
#     elif cmd[0] == 'size':
#         print(len(queue) - front_idx)
#     elif cmd[0] == 'empty':
#         print(1 if front_idx >= len(queue) else 0)
#     elif cmd[0] == 'front':
#         print(-1 if front_idx >= len(queue) else queue[front_idx])
#     elif cmd[0] == 'back':
#         print(-1 if front_idx >= len(queue) else queue[-1])