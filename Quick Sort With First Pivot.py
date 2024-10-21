def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1
        if left > right:
            break
        arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right 
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        print(f"Array after partitioning around pivot {arr[pivot_index]}: {arr}")
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
if __name__ == "__main__":
    N = 9
    arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]
    print(f"Initial Array: {arr}")
    quick_sort(arr, 0, N - 1)
    print(f"Sorted Array: {arr}")
