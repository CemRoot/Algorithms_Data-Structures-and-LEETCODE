class Node: # Defines the Node class for creating nodes in a linked list.
    def __init__(self, value): # Constructor for the Node class.
        # Initializes a new node with a given value.
        self.value = value # Stores the value of the node.
        self.next = None # Initializes the next pointer to None, indicating it doesn't point to another node yet.
        

class LinkedList: # Defines the LinkedList class.
    def __init__(self, value): # Constructor for the LinkedList class.
        # Initializes a new linked list with a single node.
        new_node = Node(value) # Creates a new Node object.
        self.head = new_node # Sets the head of the linked list to the new node.
        self.tail = new_node # Sets the tail of the linked list to the new node.
        self.length = 1 # Sets the initial length of the linked list to 1.

    def print_list(self): # Method to print all values in the linked list.
        temp = self.head # Starts from the head of the list.
        while temp is not None: # Iterates through the list as long as temp is not None.
            print(temp.value) # Prints the value of the current node.
            temp = temp.next # Moves to the next node in the list.
    
    def make_empty(self): # Method to empty the linked list.
        # Resets the head, tail, and length to their initial empty states.
        self.head = None # Sets the head to None.
        self.tail = None # Sets the tail to None.
        self.length = 0 # Sets the length to 0.
        
    def append(self, value): # Method to add a new node to the end of the linked list.
        new_node = Node(value) # Creates a new Node object with the given value.
        if self.head is None: # Checks if the linked list is empty.
            # If the list is empty, the new node becomes both the head and the tail.
            self.head = new_node
            self.tail = new_node
        else: # If the list is not empty.
            # The current tail's next pointer is set to the new node.
            self.tail.next = new_node
            # The new node becomes the new tail of the list.
            self.tail = new_node
        self.length += 1 # Increments the length of the linked list.
        # Note: This method did not originally have a return statement.
        # In many implementations, append might return True or the list itself for chaining,
        # but here it implicitly returns None.


# Test code to demonstrate the LinkedList functionality.
my_linked_list = LinkedList(1) # Creates a LinkedList with initial value 1.
my_linked_list.make_empty() # Empties the list.

my_linked_list.append(1) # Appends 1 to the list.
my_linked_list.append(2) # Appends 2 to the list.

# Prints the head, tail, and length of the list to verify the append operation.
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:') # Prints a header for the list content.
my_linked_list.print_list() # Prints all elements in the list.


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Linked List:
    1
    2
    
"""
