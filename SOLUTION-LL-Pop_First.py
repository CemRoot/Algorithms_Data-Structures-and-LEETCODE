class Node:
    def __init__(self, value):
        # Constructor for the Node class.
        # Initializes a node with a value and a next pointer.
        self.value = value  # The data stored in the node.
        self.next = None  # Pointer to the next node in the list, initialized to None.
        

class LinkedList:
    def __init__(self, value):
        # Constructor for the LinkedList class.
        # Initializes the list with a single node.
        new_node = Node(value)  # Create a new node.
        self.head = new_node  # Set the new node as the head of the list.
        self.tail = new_node  # Set the new node as the tail of the list.
        self.length = 1  # Initialize the length of the list to 1.

    def print_list(self):
        # Prints all the values in the linked list.
        temp = self.head  # Start from the head.
        while temp is not None:  # Iterate until the end of the list.
            print(temp.value)  # Print the value of the current node.
            temp = temp.next  # Move to the next node.
        
    def append(self, value):
        # Adds a new node with the given value to the end of the list.
        new_node = Node(value)  # Create a new node.
        if self.length == 0:  # If the list is empty.
            self.head = new_node  # The new node is both head and tail.
            self.tail = new_node
        else:  # If the list is not empty.
            self.tail.next = new_node  # Link the current tail to the new node.
            self.tail = new_node  # Update the tail to be the new node.
        self.length += 1  # Increment the length of the list.
        return True  # Indicate successful append operation.

    def pop(self):
        # Removes the last node from the list and returns it.
        # Returns None if the list is empty.
        if self.length == 0:  # If the list is empty.
            return None
        
        temp = self.head  # Used to traverse the list to find the last node.
        pre = self.head   # Used to keep track of the node before temp (the new tail).
        
        while(temp.next):  # Traverse until temp is the last node (temp.next is None).
            pre = temp
            temp = temp.next
            
        self.tail = pre  # The node before the original tail becomes the new tail.
        self.tail.next = None  # Remove the link to the old tail.
        self.length -= 1  # Decrement the length.
        
        if self.length == 0:  # If the list becomes empty after popping.
            self.head = None
            self.tail = None
            
        return temp  # Return the popped node.

    def prepend(self, value):
        # Adds a new node with the given value to the beginning of the list.
        new_node = Node(value)  # Create a new node.
        if self.length == 0:  # If the list is empty.
            self.head = new_node  # The new node is both head and tail.
            self.tail = new_node
        else:  # If the list is not empty.
            new_node.next = self.head  # Link the new node to the current head.
            self.head = new_node  # Update the head to be the new node.
        self.length += 1  # Increment the length.
        return True  # Indicate successful prepend operation.

    def pop_first(self):
        # Removes the first node from the list and returns it.
        # Returns None if the list is empty.
        if self.length == 0: # If the list is empty.
            return None
        
        temp = self.head  # Store the current head to be returned later.
        self.head = self.head.next  # Move the head pointer to the next node.
        temp.next = None  # Disconnect the old head from the list.
        self.length -= 1  # Decrement the length.
        
        if self.length == 0:  # If the list becomes empty after popping.
            self.tail = None # Ensure tail is also None.
            
        return temp # Return the popped node.



# Test code for pop_first method.
my_linked_list = LinkedList(2) # Create a list with 2.
my_linked_list.append(1)       # Append 1, list is now 2 -> 1.


# (2) Items - Returns 2 Node
# Pops the first item (2), prints its value.
print(my_linked_list.pop_first().value)
# (1) Item -  Returns 1 Node
# Pops the new first item (1), prints its value.
print(my_linked_list.pop_first().value)
# (0) Items - Returns None
# Tries to pop from an empty list, should print None (or raise an error if .value is accessed on None).
# The original test code directly prints the result of pop_first(), which would be the Node object or None.
# If pop_first() returns None, printing None.value would cause an AttributeError.
# The expected output suggests printing the object itself when it's None.
popped_node = my_linked_list.pop_first()
if popped_node:
    print(popped_node.value)
else:
    print(popped_node) # This will print None


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
