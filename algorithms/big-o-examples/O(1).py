def add_items(n):
    # Defines a function named add_items that accepts one integer argument 'n'.
    # The purpose of this function is to demonstrate O(1) time complexity,
    # also known as constant time complexity.
    # An operation or function has O(1) complexity if its execution time
    # does not depend on the size of the input 'n'.

    # The operation performed below (addition of two numbers)
    # takes the same amount of time regardless of the value of 'n'.
    # Whether 'n' is 1 or 1,000,000, adding n + n takes a constant number of steps.
    result = n + n  # Performs a single addition operation.

    # Even if we had multiple such constant-time operations, e.g.:
    # result = n + n
    # result2 = n * n
    # result3 = n / 2
    # The total number of operations would still be a constant (e.g., 3 operations).
    # In Big O notation, O(3) simplifies to O(1).
    
    return result # Returns the sum of n and n.

# Example call to the function:
# sum_result = add_items(5)
# print(sum_result) # Expected output: 10

# sum_result_large = add_items(100000)
# print(sum_result_large) # Expected output: 200000

# The key takeaway is that the number of operations inside add_items
# does not change with the input size 'n'. It's always a fixed number of operations.

print(add_items(10))

# The function add_items is called with the argument 10.
# This means that the value 10 will be used as the argument for 'n' in the function.

# The function returns the sum of 10 added to itself three times, which is 30.
# The result 30 is then printed to the console.