from itertools import combinations
def subset_sums(arr):
    n = len(arr)
    sums = []
    for i in range(n+1):
        for subset in combinations(arr, i):
            sums.append(sum(subset))
    return sums
def meet_in_the_middle(arr, target):
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_sums = subset_sums(left_half)
    right_sums = subset_sums(right_half)
    right_sums.sort()
    closest_sum = float('inf')
    closest_diff = float('inf')
    for left_sum in left_sums:
        lo, hi = 0, len(right_sums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            current_sum = left_sum + right_sums[mid]
            current_diff = abs(target - current_sum)
            if current_diff < closest_diff:
                closest_diff = current_diff
                closest_sum = current_sum
            if current_sum < target:
                lo = mid + 1
            else:
                hi = mid - 1
    return closest_sum
arr = [45, 34, 4, 12, 5, 2]
target = 42
result = meet_in_the_middle(arr, target)
print(f"Closest subset sum to {target} is: {result}")
