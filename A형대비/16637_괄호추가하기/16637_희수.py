def calc(a, op, b):
    if op == '+': return a + b
    elif op == '-': return a - b
    else : return a * b


def dfs(i, value):
    global answer
    if i == len(ops):
        answer = max(answer, value)
        return
    
    no_paren = calc(value, ops[i], nums[i+1])
    dfs(i + 1, no_paren)

    if i + 1 < len(ops):
        t = calc(nums[i+1], ops[i+1], nums[i+2])
        with_paren = calc(value, ops[i], t)
        dfs(i + 2, with_paren)

n = int(input())
expr = input()

nums = list(map(int, expr[::2]))
ops = list(expr[1::2])

answer = -2 ** 31

dfs(0, nums[0])
print(answer)