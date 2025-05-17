def print_items(n):
    # Defines a function to demonstrate O(n^2 + n) complexity, which simplifies to O(n^2)
    # due to the dominance of the n^2 term over the n term for large values of n.
    # This illustrates the concept of ignoring non-dominant terms in Big O notation.

    # First part: O(n^2) complexity
    # This section has a nested loop structure.
    # The outer loop runs 'n' times.
    # The inner loop also runs 'n' times for each iteration of the outer loop.
    # Therefore, the print(i, j) statement executes n * n = n^2 times.
    for i in range(n):  # Outer loop: 0 to n-1
        for j in range(n):  # Inner loop: 0 to n-1
            print(i, j)  # This operation is O(1), executed n^2 times.

    # Second part: O(n) complexity
    # This section has a single loop that runs 'n' times.
    # The print(k) statement executes 'n' times.
    for k in range(n):  # Single loop: 0 to n-1
        print(k)  # This operation is O(1), executed n times.

    # Total operations = (n * n) + n = n^2 + n.
    # In Big O notation, as 'n' becomes large, the n^2 term grows much faster
    # than the 'n' term. Thus, the 'n' term is considered non-dominant and is dropped.
    # So, the overall time complexity of this function is O(n^2).

# Example call to the function:
# print_items(3)

# Expected behavior for print_items(3):
# First part (O(n^2)) will print:
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2
# (3*3 = 9 lines)

# Second part (O(n)) will print:
# 0
# 1
# 2
# (3 lines)

print_items(10)

# The function print_items is called with the argument 10.
# This means that the sequence of numbers from 0 to 9 will be printed.
