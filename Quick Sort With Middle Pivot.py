def partition(arr, low, high):
    mid = (low + high) // 2
    pivot = arr[mid]  
    arr[mid], arr[low] = arr[low], arr[mid]
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
    N = 8
    arr = [19, 72, 35, 46, 58, 91, 22, 31]
    print(f"Initial Array: {arr}")
    quick_sort(arr, 0, N - 1)
    print(f"Sorted Array: {arr}")
    N = 8
    arr = [31, 23, 35, 27, 11, 21, 15, 28]
    print("\nInitial Array:", arr)
    quick_sort(arr, 0, N - 1)
    print(f"Sorted Array: {arr}")
    N = 10
    arr = [22, 34, 25, 36, 43, 67, 52, 13, 65, 17]
    print("\nInitial Array:", arr)
    quick_sort(arr, 0, N - 1)
    print(f"Sorted Array: {arr}")
