class Node:
    # Defines the Node class, representing an individual element in a linked list.
    def __init__(self, value):
        # Constructor for the Node class.
        # Initializes a new node with a given value and a pointer to the next node.
        #
        # Args:
        #     value: The data to be stored in this node.
        self.value = value  # Stores the actual data of the node.
        self.next = None  # Pointer to the next node in the sequence, initialized to None.
        

class LinkedList:
    # Defines the LinkedList class, a data structure composed of a sequence of nodes.
    def __init__(self, value):
        # Constructor for the LinkedList class.
        # Initializes a new linked list with a single node containing the provided value.
        #
        # Args:
        #     value: The value for the first node in the linked list.
        new_node = Node(value)  # Create a new Node object.
        self.head = new_node  # The new node becomes the head (start) of the list.
        self.tail = new_node  # The new node also becomes the tail (end) of the list.
        self.length = 1  # Initialize the length of the list to 1.

    def print_list(self):
        # Method to print all values of the nodes in the linked list.
        # Traverses from the head to the tail, printing each node's value.
        temp = self.head  # Start traversal from the head of the list.
        while temp is not None:  # Continue as long as there are nodes to process.
            print(temp.value)  # Print the value of the current node.
            temp = temp.next  # Move to the next node in the list.
        
    def append(self, value):
        # Method to add a new node with a given value to the end of the linked list (tail).
        #
        # Args:
        #     value: The value for the new node to be appended.
        # Returns:
        #     True if the append operation was successful.
        new_node = Node(value)  # Create a new Node with the given value.
        if self.length == 0:  # Check if the list is currently empty.
            # If empty, the new node becomes both the head and the tail.
            self.head = new_node
            self.tail = new_node
        else:  # If the list is not empty.
            # Point the current tail's 'next' reference to the new node.
            self.tail.next = new_node
            # Update the list's tail to be the new node.
            self.tail = new_node
        self.length += 1  # Increment the length of the list.
        return True  # Indicate successful append.

    def pop(self):
        # Method to remove and return the last node (tail) from the linked list.
        # Returns None if the list is empty.
        if self.length == 0:  # If the list is empty, nothing to pop.
            return None
        
        temp = self.head  # 'temp' will traverse the list to find the last node.
        pre = self.head   # 'pre' will keep track of the node just before 'temp'.
        
        # Traverse until 'temp' is the last node (i.e., temp.next is None).
        while(temp.next):
            pre = temp
            temp = temp.next
            
        # 'temp' is now the last node, 'pre' is the second to last.
        self.tail = pre  # The new tail is the node previously before the old tail.
        self.tail.next = None  # Remove the link from the new tail to the old tail.
        self.length -= 1  # Decrement the list length.
        
        # If the list became empty after popping.
        if self.length == 0:
            self.head = None
            self.tail = None
            
        return temp  # Return the removed node.

    def prepend(self, value):
        # Method to add a new node with a given value to the beginning of the linked list (head).
        #
        # Args:
        #     value: The value for the new node to be prepended.
        # Returns:
        #     True if the prepend operation was successful.
        new_node = Node(value)  # Create a new Node with the given value.
        if self.length == 0:  # Check if the list is currently empty.
            # If empty, the new node becomes both the head and the tail.
            self.head = new_node
            self.tail = new_node
        else:  # If the list is not empty.
            new_node.next = self.head  # Point the new node's 'next' to the current head.
            self.head = new_node  # Update the list's head to be the new node.
        self.length += 1  # Increment the length of the list.
        return True  # Indicate successful prepend.

    def pop_first(self):
        # Method to remove and return the first node (head) from the linked list.
        # Returns None if the list is empty.
        if self.length == 0:  # If the list is empty, nothing to pop.
            return None
        
        temp = self.head  # Store the current head node to be returned.
        self.head = self.head.next  # Advance the head pointer to the next node.
        temp.next = None  # Disconnect the old head from the list by setting its 'next' to None.
        self.length -= 1  # Decrement the list length.
        
        # If the list became empty after popping the first element.
        if self.length == 0:
            self.tail = None  # Ensure the tail is also None.
            
        return temp  # Return the removed node.

    def get(self, index):
        # Method to retrieve the node at a specific index in the linked list.
        # The list is 0-indexed.
        #
        # Args:
        #     index (int): The index of the node to retrieve.
        # Returns:
        #     Node: The node at the specified index, or None if the index is out of bounds.
        
        # Check if the requested index is valid.
        # An index is invalid if it's negative or greater than or equal to the list length.
        if index < 0 or index >= self.length:
            return None  # Return None for out-of-bounds index.
        
        temp = self.head  # Start traversal from the head of the list.
        
        # Iterate 'index' times to reach the desired node.
        # The underscore `_` is used as a variable name for the loop counter
        # because its actual value is not used within the loop body,
        # only the number of iterations matters.
        for _ in range(index):
            temp = temp.next  # Move to the next node in each iteration.
            
        # After the loop, 'temp' will be pointing to the node at the specified 'index'.
        return temp
        


# Test code to demonstrate the 'get' method.
my_linked_list = LinkedList(0)  # Create a list: 0
my_linked_list.append(1)        # List: 0 -> 1
my_linked_list.append(2)        # List: 0 -> 1 -> 2
my_linked_list.append(3)        # List: 0 -> 1 -> 2 -> 3

# Retrieve the node at index 3 and print its value.
# get(0) would be node with value 0
# get(1) would be node with value 1
# get(2) would be node with value 2
# get(3) would be node with value 3
retrieved_node = my_linked_list.get(3)
if retrieved_node: # Check if a node was actually returned (not None)
    print(retrieved_node.value)
else:
    print("Node not found at index 3")

# Example of an out-of-bounds access:
# print(my_linked_list.get(10)) # This would print None as per the get method logic.
# If you tried print(my_linked_list.get(10).value), it would cause an AttributeError.

"""
    EXPECTED OUTPUT:
    ----------------
    3

"""