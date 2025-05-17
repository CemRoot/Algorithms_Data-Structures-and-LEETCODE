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
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp # Return the popped node.

    def prepend(self, value):
        # Adds a new node with the given value to the beginning of the list.
        new_node = Node(value)  # Create a new node.
        if self.length == 0:  # If the list is empty.
            self.head = new_node  # The new node becomes both the head and the tail.
            self.tail = new_node
        else:  # If the list is not empty.
            new_node.next = self.head  # Point the new node's 'next' to the current head.
            self.head = new_node  # Update the list's head to be the new node.
        self.length += 1  # Increment the length of the list.
        return True  # Indicate successful prepend operation.



# Test code for the prepend method.
my_linked_list = LinkedList(2) # Initialize list with 2.
my_linked_list.append(3)       # Append 3. List: 2 -> 3.

print('Before prepend():')
print('----------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()


my_linked_list.prepend(1) # Prepend 1. List should be: 1 -> 2 -> 3.


print('\n\nAfter prepend():')
print('---------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    
    Before prepend():
    ----------------
    Head: 2
    Tail: 3
    Length: 2 

    Linked List:
    2
    3


    After prepend():
    ---------------
    Head: 1
    Tail: 3
    Length: 3 

    Linked List:
    1
    2
    3   

"""