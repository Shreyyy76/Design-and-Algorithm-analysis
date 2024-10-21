def partition(arr, low, high, pivot):
    pivot_value = arr[pivot]
    arr[pivot], arr[high] = arr[high], arr[pivot]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index
def find_median(arr):
    arr.sort() 
    return arr[len(arr) // 2]
def select(arr, low, high, k):
    if low == high:
        return arr[low]
    medians = []
    for i in range(low, high + 1, 5):
        group = arr[i:i + 5]
        median = find_median(group)
        medians.append(median)
    if len(medians) <= 5:
        pivot = find_median(medians)
    else:
        pivot = select(medians, 0, len(medians) - 1, len(medians) // 2)
    pivot_index = arr.index(pivot)
    partition_index = partition(arr, low, high, pivot_index)
    if k == partition_index:
        return arr[partition_index]
    elif k < partition_index:
        return select(arr, low, partition_index - 1, k)
    else:
        return select(arr, partition_index + 1, high, k)
def kth_smallest(arr, k):
    return select(arr, 0, len(arr) - 1, k - 1)
arr = [12, 3, 5, 7, 19]
k = 2
result = kth_smallest(arr, k)
print(f"The {k}-th smallest element is: {result}")
