#include <stdio.h>

int main() {
    int nums[] = {-10, 2, 3, -4, 5};  
    int n = 5;  
    int max = nums[0];  

    for (int i = 1; i < n; i++) {
        if (nums[i] > max) {
            max = nums[i];  
        }
    }

    printf("%d\n", max);  
    return 0;
}


