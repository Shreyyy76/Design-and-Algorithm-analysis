#include <stdio.h>

int main() {
    int nums[] = {1, 2, 1};
    int n = 3;  
    int result = 0;

    for (int i = 0; i < n; i++) {
        int count[101] = {0};   
        int distinct = 0;

        for (int j = i; j < n; j++) {
            if (count[nums[j]] == 0) {
                distinct++;  
            }
            count[nums[j]]++;
            result += distinct * distinct;  
        }
    }

    printf("%d\n", result);
    return 0;
}
