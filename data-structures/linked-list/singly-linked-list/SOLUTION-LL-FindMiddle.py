class Node:
    # Constructor for the Node class.
    # A Node consists of a 'value' and a 'next' pointer, which points to the next node in the list.
    # By default, 'next' is None, indicating it's the last node or not yet connected.
    def __init__(self, value):
        self.value = value  # The data stored in the node
        self.next = None    # Pointer to the next node in the list

class LinkedList:
    # Constructor for the LinkedList class.
    # A LinkedList is initialized with a 'head' and a 'tail' pointer, and a 'length' counter.
    # Initially, for an empty list, head and tail are None, and length is 0.
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            # If a value is provided, create a new node and initialize the list with it.
            new_node = Node(value)
            self.head = new_node    # The new node is both the head
            self.tail = new_node    # and the tail of the list
            self.length = 1         # The length of the list is 1

    # Method to print all values in the linked list.
    # It starts from the 'head' and traverses through the list until the end.
    def print_list(self):
        temp = self.head  # Start from the head of the list
        while temp is not None:  # Continue as long as there are nodes
            print(temp.value)    # Print the value of the current node
            temp = temp.next     # Move to the next node

    # Method to add a new node with a given 'value' to the end of the list.
    # This is also known as appending a node.
    def append(self, value):
        new_node = Node(value)  # Create a new node with the given value
        if self.head is None:   # If the list is empty
            self.head = new_node    # The new node becomes both the head
            self.tail = new_node    # and the tail
        else:
            # If the list is not empty, attach the new node after the current tail.
            self.tail.next = new_node
            self.tail = new_node    # Update the tail to be the new node
        self.length += 1        # Increment the length of the list
        return True             # Return True indicating success

    # Method to find the middle node of the linked list.
    # It uses the "slow and fast pointer" technique.
    # The 'slow' pointer moves one step at a time.
    # The 'fast' pointer moves two steps at a time.
    # When the 'fast' pointer reaches the end of the list (or None),
    # the 'slow' pointer will be at the middle node.
    # For lists with an even number of nodes, this method can return either of the two middle nodes.
    # The common convention is to return the first of the two middle nodes if length is even,
    # or the exact middle if length is odd. Our implementation will follow this.
    def find_middle_node(self):
        # Initialize both slow and fast pointers to the head of the list.
        slow = self.head
        fast = self.head

        # Edge case: If the list is empty, there is no middle node.
        if self.head is None:
            return None

        # Traverse the list with the slow and fast pointers.
        # The loop continues as long as 'fast' is not None and 'fast.next' is not None.
        # This ensures that 'fast' does not go beyond the end of the list
        # when trying to access 'fast.next.next'.
        while fast is not None and fast.next is not None:
            slow = slow.next          # Move slow pointer one step
            fast = fast.next.next    # Move fast pointer two steps

        # When the loop terminates, 'slow' will be pointing to the middle node.
        # If the list has an even number of nodes, 'fast' will be None.
        # If the list has an odd number of nodes, 'fast.next' will be None.
        # In both cases, 'slow' is at the correct middle position (or the first of two for even length).
        return slow


# --- Test Cases ---

# Test 1: Create a list with an odd number of elements (1, 2, 3, 4, 5)
print("Test 1: Odd number of elements")
my_linked_list_odd = LinkedList(1)
my_linked_list_odd.append(2)
my_linked_list_odd.append(3)
my_linked_list_odd.append(4)
my_linked_list_odd.append(5)

print("Original list (Odd):")
my_linked_list_odd.print_list()

middle_node_odd = my_linked_list_odd.find_middle_node()
if middle_node_odd:
    print(f"Middle node value (Odd): {middle_node_odd.value}") # Expected: 3
else:
    print("List is empty or something went wrong.")
print("---")

# Test 2: Create a list with an even number of elements (1, 2, 3, 4, 5, 6)
print("Test 2: Even number of elements")
my_linked_list_even = LinkedList(1)
my_linked_list_even.append(2)
my_linked_list_even.append(3)
my_linked_list_even.append(4)
my_linked_list_even.append(5)
my_linked_list_even.append(6)

print("Original list (Even):")
my_linked_list_even.print_list()

middle_node_even = my_linked_list_even.find_middle_node()
if middle_node_even:
    print(f"Middle node value (Even): {middle_node_even.value}") # Expected: 3 (or 4 depending on convention, this will give 3)
else:
    print("List is empty or something went wrong.")
print("---")

# Test 3: List with a single element (1)
print("Test 3: Single element list")
my_linked_list_single = LinkedList(1)
print("Original list (Single):")
my_linked_list_single.print_list()
middle_node_single = my_linked_list_single.find_middle_node()
if middle_node_single:
    print(f"Middle node value (Single): {middle_node_single.value}") # Expected: 1
else:
    print("List is empty.")
print("---")

# Test 4: List with two elements (1, 2)
print("Test 4: Two elements list")
my_linked_list_two = LinkedList(1)
my_linked_list_two.append(2)
print("Original list (Two):")
my_linked_list_two.print_list()
middle_node_two = my_linked_list_two.find_middle_node()
if middle_node_two:
    print(f"Middle node value (Two): {middle_node_two.value}") # Expected: 1
else:
    print("List is empty.")
print("---")


# Test 5: Empty list
print("Test 5: Empty list")
my_linked_list_empty = LinkedList() # Initialize an empty list
# Or, my_linked_list_empty = LinkedList()
# then call my_linked_list_empty.make_empty() if you have it, but we directly initialize.
# We need to make sure the LinkedList constructor handles value=None correctly.
# Let's adjust LinkedList to allow creating an empty list directly or with an initial value.

# The provided LinkedList constructor makes a node if a value is passed.
# To create a truly empty list for testing find_middle_node, we need to initialize it without a value.
# Let's re-initialize it without arguments for this test.

# If the LinkedList class always creates a node, we need a way to test an empty list.
# For now, let's assume we can create one like this:
actual_empty_list = LinkedList() #This was not working as expected
actual_empty_list.head = None
actual_empty_list.tail = None
actual_empty_list.length = 0

print("Original list (Empty):")
actual_empty_list.print_list() # Should print nothing

middle_node_empty = actual_empty_list.find_middle_node()
if middle_node_empty:
    print(f"Middle node value (Empty): {middle_node_empty.value}")
else:
    print("Middle node (Empty): None") # Expected: None
print("---") 