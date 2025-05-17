def print_items(n):
    # Defines a function named print_items that accepts a single integer argument 'n'.
    # The purpose of this function is to demonstrate O(n^2) time complexity,
    # also known as quadratic time complexity.
    # A function has O(n^2) complexity if its execution time grows proportionally
    # to the square of the size of the input 'n'. This typically occurs with nested loops
    # where each loop iterates based on the input size 'n'.

    # Outer loop: Iterates 'n' times.
    # For each value of 'i' from 0 to n-1,
    for i in range(n):
        # Inner loop: Also iterates 'n' times.
        # For each iteration of the outer loop, this inner loop runs completely.
        # So, for each 'i', 'j' goes from 0 to n-1.
        for j in range(n):
            # The operation inside the inner loop (print) is O(1).
            # This O(1) operation is executed n times by the inner loop,
            # and the inner loop itself is executed n times by the outer loop.
            # Thus, the print(i, j) statement is executed n * n = n^2 times.
            print(i, j)  # Prints the current pair of (i, j).

    # Total operations: The print statement runs n^2 times.
    # Therefore, the time complexity of this function is O(n^2).

    # If there was another O(n^2) block, e.g.:
    # for x in range(n):
    #     for y in range(n):
    #         print(x,y)
    # The complexity would be O(n^2) + O(n^2) = O(2n^2), which simplifies to O(n^2)
    # because constant factors are dropped in Big O notation.

# Example call to the function:
# print_items(3)

# Expected behavior for print_items(3):
# Outer loop (i): 0, 1, 2
# Inner loop (j): 0, 1, 2 for each i
# Output will be:
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2
# Total of 3 * 3 = 9 print operations.
# If n doubles to 6, operations would be 6*6 = 36 (increases by a factor of 4, which is 2^2).

print_items(10)

# The function print_items is called with the argument 10.
# This means that the sequence of numbers from 0 to 9 will be printed.

