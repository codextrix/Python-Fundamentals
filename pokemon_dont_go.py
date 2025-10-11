# Pokemon Don't Go — interactive-safe solution

def adjust(arr, removed):
    for i, v in enumerate(arr):
        arr[i] = v + removed if v <= removed else v - removed

nums = list(map(int, input().split()))
removed_sum = 0

while nums:
    try:
        idx = int(input().strip())
    except EOFError:
        # No more indices provided; end here
        break

    if idx < 0:
        removed = nums[0]
        removed_sum += removed
        nums[0] = nums[-1]          # copy last value into first slot
        adjust(nums, removed)

    elif idx >= len(nums):
        removed = nums[-1]
        removed_sum += removed
        nums[-1] = nums[0]          # copy first value into last slot
        adjust(nums, removed)

    else:
        removed = nums.pop(idx)
        removed_sum += removed
        adjust(nums, removed)

print(removed_sum)
