#include <stdio.h>
#include <string.h>
#include <stdbool.h>
bool isPalindrome(char str[]) {
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        if (str[i] != str[len - i - 1]) {
            return false;
        }
    }
    return true;
}
char* firstPalindromicString(char words[][100], int size) {
    for (int i = 0; i < size; i++) {
        if (isPalindrome(words[i])) {
            return words[i];
        }
    }
    return ""; 
}

int main() {
    char words[][100] = {"abc", "car", "ada", "racecar", "cool"};
    int size = sizeof(words) / sizeof(words[0]);
    
    char* result = firstPalindromicString(words, size);
    
    if (strlen(result) > 0) {
        printf("First palindromic string: %s\n", result); 
    } else {
        printf("No palindromic string found.\n");
    }
    return 0;
}



