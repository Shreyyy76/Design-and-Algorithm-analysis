import itertools
def total_value(items, values):
    value = 0
    for i in items:
        value += values[i]
    return value
def is_feasible(items, weights, capacity):
    total_weight = 0
    for i in items:
        total_weight += weights[i]
    return total_weight <= capacity
def knapsack_problem(weights, values, capacity):
    num_items = len(weights)
    best_value = 0
    best_selection = []
    for r in range(num_items + 1):
        for subset in itertools.combinations(range(num_items), r):
            if is_feasible(subset, weights, capacity):
                current_value = total_value(subset, values)
                if current_value > best_value:
                    best_value = current_value
                    best_selection = list(subset)
    return best_selection, best_value
def test_knapsack_problem():
    weights1 = [2, 3, 1]
    values1 = [4, 5, 3]
    capacity1 = 4
    selection1, value1 = knapsack_problem(weights1, values1, capacity1)
    print("Test Case 1:")
    print(f"Optimal Selection: {selection1} (Items with indices {selection1})")
    print(f"Total Value: {value1}\n")
    weights2 = [1, 2, 3, 4]
    values2 = [2, 4, 6, 3]
    capacity2 = 6
    selection2, value2 = knapsack_problem(weights2, values2, capacity2)
    print("Test Case 2:")
    print(f"Optimal Selection: {selection2} (Items with indices {selection2})")
    print(f"Total Value: {value2}\n")
if __name__ == "__main__":
    test_knapsack_problem()
