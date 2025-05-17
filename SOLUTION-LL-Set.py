class Node:
    # Defines the Node class, representing an individual element (or node) in a linked list.
    # Each node stores a piece of data (value) and a reference (next) to the subsequent node.
    def __init__(self, value):
        # Constructor for the Node class.
        # Initializes a new node with a specified value.
        # The 'next' pointer is initialized to None, indicating it doesn't point to another node yet.
        #
        # Args:
        #     value: The data to be stored within this node.
        self.value = value  # Assigns the provided value to the node's 'value' attribute.
        self.next = None  # Initializes the 'next' pointer to None.
        

class LinkedList:
    # Defines the LinkedList class, which manages a sequence of Node objects.
    # It encapsulates operations like adding, removing, and accessing nodes,
    # and keeps track of the list's head, tail, and length.
    def __init__(self, value):
        # Constructor for the LinkedList class.
        # Initializes a new linked list with a single node containing the given value.
        #
        # Args:
        #     value: The value for the first node in the linked list.
        new_node = Node(value)  # Create a new Node instance.
        self.head = new_node  # Set the new node as the head (start) of the list.
        self.tail = new_node  # Set the new node as the tail (end) of the list.
        self.length = 1  # Initialize the list's length to 1.

    def print_list(self):
        # Method to print all values of the nodes in the linked list, one value per line.
        # It traverses the list from the head to the tail.
        temp = self.head  # Start traversal from the head.
        while temp is not None:  # Loop as long as 'temp' points to an existing node.
            print(temp.value)  # Print the value of the current node.
            temp = temp.next  # Move to the next node.
        
    def append(self, value):
        # Method to add a new node with a given value to the end (tail) of the linked list.
        #
        # Args:
        #     value: The value for the new node to be appended.
        # Returns:
        #     True, indicating the append operation was successful.
        new_node = Node(value)  # Create a new node with the given value.
        if self.length == 0:  # If the list is empty.
            self.head = new_node  # The new node is both head and tail.
            self.tail = new_node
        else:  # If the list is not empty.
            self.tail.next = new_node  # Link the current tail to the new node.
            self.tail = new_node  # Update the list's tail to be the new node.
        self.length += 1  # Increment the length of the list.
        return True  # Append operation is considered successful.

    def pop(self):
        # Method to remove and return the last node (tail) from the linked list.
        # Returns the removed node, or None if the list is empty.
        if self.length == 0:  # If the list is empty, nothing to pop.
            return None
        
        temp = self.head  # 'temp' traverses to find the last node.
        pre = self.head   # 'pre' keeps track of the node before 'temp'.
        
        while(temp.next):  # Traverse until 'temp' is the last node.
            pre = temp
            temp = temp.next
            
        self.tail = pre  # The node before the old tail becomes the new tail.
        self.tail.next = None  # Remove the link from the new tail to the old tail.
        self.length -= 1  # Decrement the list length.
        
        if self.length == 0:  # If the list became empty.
            self.head = None
            self.tail = None
            
        return temp  # Return the removed (old tail) node.

    def prepend(self, value):
        # Method to add a new node with a given value to the beginning (head) of the linked list.
        #
        # Args:
        #     value: The value for the new node to be prepended.
        # Returns:
        #     True, indicating the prepend operation was successful.
        new_node = Node(value)  # Create a new node.
        if self.length == 0:  # If the list is empty.
            self.head = new_node  # The new node is both head and tail.
            self.tail = new_node
        else:  # If the list is not empty.
            new_node.next = self.head  # Link the new node to the current head.
            self.head = new_node  # Update the list's head to be the new node.
        self.length += 1  # Increment the list length.
        return True  # Prepend operation is successful.

    def pop_first(self):
        # Method to remove and return the first node (head) from the linked list.
        # Returns the removed node, or None if the list is empty.
        if self.length == 0:  # If the list is empty.
            return None
        
        temp = self.head  # Store the current head to be returned.
        self.head = self.head.next  # Advance the head pointer to the next node.
        temp.next = None  # Disconnect the old head from the list.
        self.length -= 1  # Decrement the list length.
        
        if self.length == 0:  # If the list became empty.
            self.tail = None  # Ensure tail is also None.
            
        return temp  # Return the removed (old head) node.

    def get(self, index):
        # Method to retrieve the node at a specific index in the linked list (0-indexed).
        #
        # Args:
        #     index (int): The index of the node to retrieve.
        # Returns:
        #     Node: The node at the specified index, or None if the index is out of bounds.
        if index < 0 or index >= self.length:  # Check for invalid index.
            return None
        temp = self.head  # Start traversal from the head.
        for _ in range(index):  # Iterate 'index' times to reach the target node.
            temp = temp.next
        return temp  # Return the node found at the given index.
        
    def set_value(self, index, value):
        # Method to update the value of a node at a specific index in the linked list.
        #
        # Args:
        #     index (int): The index of the node whose value is to be updated.
        #     value: The new value to set for the node at the specified index.
        # Returns:
        #     True if the value was successfully updated (i.e., index was valid).
        #     False if the index was out of bounds and the value could not be set.
        
        # Use the existing 'get' method to find the node at the given index.
        temp = self.get(index)
        
        if temp:  # Check if 'get' returned a valid node (not None).
            # If a node was found at the index...
            temp.value = value  # Update its value with the new value provided.
            return True  # Indicate that the set operation was successful.
        
        # If 'get' returned None (meaning the index was invalid), then temp will be None.
        return False  # Indicate that the set operation failed.
    


# Test code to demonstrate the 'set_value' method.
my_linked_list = LinkedList(11) # List: 11
my_linked_list.append(3)        # List: 11 -> 3
my_linked_list.append(23)       # List: 11 -> 3 -> 23
my_linked_list.append(7)        # List: 11 -> 3 -> 23 -> 7

print('LL before set_value():')
my_linked_list.print_list()     # Prints the initial list.

# Set the value of the node at index 1 (which currently holds 3) to 4.
my_linked_list.set_value(1, 4)

print('\nLL after set_value():')
my_linked_list.print_list()     # Prints the list after modification.

# Example of trying to set a value at an invalid index:
# result = my_linked_list.set_value(10, 100) # Index 10 is out of bounds.
# print(result) # This would print False.


"""
    EXPECTED OUTPUT:
    ----------------
    LL before set_value():
    11
    3
    23
    7

    LL after set_value():
    11
    4
    23
    7
"""