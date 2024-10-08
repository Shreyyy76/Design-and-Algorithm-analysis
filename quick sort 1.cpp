#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    int nums[] = {3, 1, 4, 1, 5};  
    int n = 5;  
    if (n == 0) {
        printf("List is empty\n");
    } else {
        
        quickSort(nums, 0, n - 1);

       
        printf("Sorted List: ");
        for (int i = 0; i < n; i++) {
            printf("%d ", nums[i]);
        }

        printf("\nMaximum element: %d\n", nums[n - 1]);
    }

    return 0;
}
