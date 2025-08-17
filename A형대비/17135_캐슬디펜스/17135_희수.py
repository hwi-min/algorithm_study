def choose_archers(idx):
    global result
    if len(archers) == 3:
        result = max(result, defense())
        return
    
    if idx == m:
        return
    
    archers.append(idx)
    choose_archers(idx + 1)
    archers.pop()
    choose_archers(idx + 1)

def defense():

    board = [row[:] for row in arr]
    kills = 0

    while any(map(any, board)):
        target = set()

        for archer in archers:
            best = None
            best_dist = d + 1

            for y in range(n-1, -1, -1):
                for x in range(m):
                    if board[y][x] == 1:
                        dist = abs(x-archer) + abs(y-n)
                        if dist <= d:
                            if dist < best_dist or (dist == best_dist and (best is None or x < best[1])):
                                best_dist = dist
                                best = (y, x)
            if best:
                target.add(best)
        
        for y, x in target:
            if board[y][x] == 1:
                board[y][x] = 0
                kills += 1
        
        board.pop()
        board.insert(0, [0] * m)
    
    return kills
                

n, m, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
archers = []
result = 0

choose_archers(0)
print(result)