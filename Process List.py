def process_list(lst):
    if not lst:
        return lst
    elif all(x < 0 for x in lst):
        return sorted(lst)
    else:
        return lst
test_cases = [
    [],
    [1],
    [7, 7, 7, 7],
    [-5, -1, -3, -2, -4]
]
for i, test in enumerate(test_cases, 1):
    print(f"Test Case {i}: Input: {test}")
    print(f"Output: {process_list(test)}")
    print()
