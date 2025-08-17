def check(nums): # nums : 구역들 넣은 리스트
    if len(nums) == 0 or len(nums) == n:
        return False
    
    stack = [nums[0]]
    visited = {nums[0]}
    while stack:
        u = stack.pop()
        for value in info[u-1][1:]:
            if value in nums and value not in visited:
                visited.add(value)
                stack.append(value)

    return len(visited) == len(nums)



def dfs(idx, group):
    global min_pop

    if min_pop == 0:
        return

    if idx == n + 1:
        full = [i for i in range(1, n+1)]
        remain = list(set(full) - set(group))
        if check(group) and check(remain):
            pop1 = 0
            pop2 = 0
            for i in range(n):
                if i + 1 in group:
                    pop1 += population[i]
                else : pop2 += population[i]
                
            min_pop = min(min_pop, abs(pop1 - pop2))
        return
    
    if idx == 1:
        dfs(idx + 1, group + [idx])
        return
    
    dfs(idx + 1, group + [idx])
    dfs(idx + 1, group)


n = int(input()) # 구역 개수
population = list(map(int, input().split())) # 구역별 인구 수
info = [list(map(int, input().split())) for _ in range(n)]
# 인접한 구역의 수, 인접한 구역 번호들
min_pop = sum(population)
dfs(1, [])
print(-1 if min_pop == sum(population) else min_pop)



        
    
