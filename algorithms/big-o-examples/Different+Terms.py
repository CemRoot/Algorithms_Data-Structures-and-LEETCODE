def print_items(a,b):
    # Defines a function named print_items that accepts two integer arguments, 'a' and 'b'.
    # The purpose of this function is to demonstrate nested loops and how their
    # execution counts differ when the ranges are independent (additive complexity).

    # First loop: Iterates 'a' times.
    for i in range(a):  # Outer loop, iterates from 0 up to (but not including) 'a'.
        # For each iteration, 'i' takes on values 0, 1, ..., a-1.

        print(i)  # Prints the current value of 'i' to the console.
        # This print statement executes 'a' times in total due to this loop.

    # Second loop: Iterates 'b' times.
    # This loop is separate from the first one; it is not nested within it.
    for j in range(b):  # Second loop, iterates from 0 up to (but not including) 'b'.
        # For each iteration, 'j' takes on values 0, 1, ..., b-1.

        print(j)  # Prints the current value of 'j' to the console.
        # This print statement executes 'b' times in total due to this loop.

    # The total number of print operations is a + b.
    # This is an example of O(a + b) time complexity if we consider both inputs.
    # If one input is significantly larger than the other, it dominates.
    # If a and b are roughly the same (e.g., both are n), it's O(n + n) = O(2n) = O(n).

# Example call to the function.
print_items(1, 10)

# When print_items(1, 10) is called:
# The first loop (for i in range(a)) where a=1:
#   - i will be 0.
#   - It will print: 0
#   (1 operation)
#
# The second loop (for j in range(b)) where b=10:
#   - j will be 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.
#   - It will print: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (each on a new line)
#   (10 operations)
# Total operations = 1 + 10 = 11.