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
        if self.length == 0:  # If the list is empty, there's nothing to pop.
            return None
        
        temp = self.head  # Start a traversal pointer from the head.
        pre = self.head   # Keep a pointer to the node before 'temp'.
        
        # Traverse the list until 'temp' is the last node.
        # 'temp.next' will be None when 'temp' is the last node.
        while(temp.next):
            pre = temp  # 'pre' trails 'temp'.
            temp = temp.next # Move 'temp' to the next node.
            
        # At this point, 'temp' is the last node (the one to be popped),
        # and 'pre' is the second to last node (which will become the new tail).
        self.tail = pre  # Update the tail to be the second to last node.
        self.tail.next = None  # Sever the link to the old tail node.
        self.length -= 1  # Decrement the length of the list.
        
        # If the list becomes empty after popping the last element.
        if self.length == 0:
            self.head = None  # Set head to None.
            self.tail = None  # Set tail to None.

        return temp  # Return the popped node (which is 'temp').
 


# Test code for the pop method.
my_linked_list = LinkedList(1) # Create a list with 1.
my_linked_list.append(2)       # Append 2. List is now 1 -> 2.

# (2) Items - Returns 2 Node
# Pops the last item (2), prints its value.
print(my_linked_list.pop().value)
# (1) Item -  Returns 1 Node
# Pops the new last item (1), prints its value.
print(my_linked_list.pop().value)
# (0) Items - Returns None
# Tries to pop from an empty list.
# The original test code directly prints the result of pop(), which would be the Node object or None.
# If pop() returns None, printing None.value would cause an AttributeError.
# The expected output suggests printing the object itself when it's None.
popped_node = my_linked_list.pop()
if popped_node:
    print(popped_node.value) # This won't execute if popped_node is None
else:
    print(popped_node) # This will print "None"


"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""