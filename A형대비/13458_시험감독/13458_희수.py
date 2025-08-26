n = int(input())
nums = list(map(int, input().split()))
A, B = map(int, input().split())
count = 0

for i in range(len(nums)):
    nums[i] -= A
    count += 1
    if nums[i] > 0:
        count += (nums[i] + B - 1) // B
    
print(count)