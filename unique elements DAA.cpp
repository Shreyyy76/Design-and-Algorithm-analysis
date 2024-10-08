#include <stdio.h>

int main() {
    int nums[] = {1, 2, 2, 3, 4, 4, 5};  
    int n = 7;  
    int unique[100];  
    int unique_count = 0;  
    int is_unique;
    for (int i = 0; i < n; i++) {
        is_unique = 1;  
        for (int j = 0; j < unique_count; j++) {
            if (nums[i] == unique[j]) {
                is_unique = 0;  
                break;
            }
        }
        if (is_unique) {
            unique[unique_count] = nums[i];
            unique_count++;
        }
    }
    printf("Unique elements: ");
    for (int i = 0; i < unique_count; i++) {
        printf("%d ", unique[i]);
    }
    printf("\n");
    return 0;
}
