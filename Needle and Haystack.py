def strStr(haystack, needle):
    if not needle:
        return 0
    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):
        return i
    return -1
haystack = "sadbutsad"
needle = "sad"
result = strStr(haystack, needle)
print(f"Index of the first occurrence of '{needle}' in '{haystack}': {result}")
