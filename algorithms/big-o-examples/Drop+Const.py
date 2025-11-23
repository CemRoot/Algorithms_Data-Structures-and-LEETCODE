def print_items(n):
    # Defines a function named print_items that accepts a single integer argument 'n'.
    # The purpose of this function is to demonstrate a simple loop that runs 'n' times,
    # which is a common example of O(n) time complexity (linear time complexity).
 
    for i in range(n):  # This loop iterates 'n' times.
        # In each iteration, 'i' takes on values from 0, 1, ..., up to n-1.
 
        print(i)  # Prints the current value of 'i' to the console.
        # This operation inside the loop is considered a constant time operation (O(1)).
 
    # Since the loop runs 'n' times and performs a constant time operation in each iteration,
    # the total time complexity of this function is O(n) * O(1) = O(n).
    # The term "Drop Constants" refers to the practice in Big O notation where constant
    # multipliers are ignored. For example, if there were two such loops one after another,
    # the complexity would be O(n) + O(n) = O(2n), which simplifies to O(n).
    # Or if the loop contained, say, 3 print statements, it would be O(n * 3), still O(n).

# Example call to the function.
print_items(10)

# When print_items(10) is called:
# The loop will iterate for i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.
# It will print each of these numbers on a new line.
# This demonstrates that the number of operations (prints) scales linearly with the input 'n'.

