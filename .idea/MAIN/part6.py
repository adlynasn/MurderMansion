def knapsack_01(items, capacity):
    n = len(items)


    # Create a 2D table to store the maximum weights
    table = [[0] * (capacity + 1) for _ in range(n + 1)]


    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if items[i - 1][1] <= w:
                table[i][w] = max(table[i - 1][w], table[i - 1][w - items[i - 1][1]] + items[i - 1][1])
            else:
                table[i][w] = table[i - 1][w]


    # Retrieve the included items by backtracking through the table
    included_items = []
    i = n
    w = capacity
    while i > 0 and w > 0:
        if table[i][w] != table[i - 1][w]:
            included_items.append(items[i - 1])
            w -= items[i - 1][1]
        i -= 1


    return included_items[::-1]


# Test the knapsack algorithm with the provided item weights and trolley capacity
items = [("Corn sack", 12), ("Hoe", 5), ("Oil tank", 10), ("Tires", 16)]
trolley_capacity = 30


included_items = knapsack_01(items, trolley_capacity)


if included_items:
    total_weight = sum(item[1] for item in included_items)
    print("The item carried on the trolley is:")
    for item in included_items:
        print(f"Item: {item[0]}, Weight: {item[1]}kg")
    print(f"Total Weight: {total_weight}kg")
else:
    print("No combination of items fits within the trolley's capacity.")
