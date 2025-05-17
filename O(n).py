def print_items(n):
    # Defines a function named print_items that accepts a single integer argument 'n'.
    # The purpose of this function is to demonstrate O(n) time complexity,
    # also known as linear time complexity.
    # A function has O(n) complexity if its execution time grows linearly
    # with the size of the input 'n'.

    # The loop below iterates 'n' times, from 0 up to n-1.
    for i in range(n):
        # Inside the loop, a print operation is performed.
        # This print operation itself is typically considered O(1) (constant time).
        print(i)  # Prints the current value of 'i'.

    # Since the O(1) operation (print) is performed 'n' times due to the loop,
    # the total time complexity of this function is n * O(1) = O(n).
    
    # If there were another separate loop that also runs 'n' times, like:
    # for j in range(n):
    #     print(j)
    # The total complexity would be O(n) + O(n) = O(2n).
    # In Big O notation, constant factors are dropped, so O(2n) simplifies to O(n).

# Example call to the function:
# print_items(5)

# Expected behavior for print_items(5):
# The loop will run 5 times (for i = 0, 1, 2, 3, 4).
# It will print:
# 0
# 1
# 2
# 3
# 4
# The number of print operations is directly proportional to 'n'.
# If n doubles, the number of operations also doubles.
