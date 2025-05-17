class Node:
    # Defines the Node class, a fundamental component of a linked list.
    # Each Node instance holds a 'value' and a pointer ('next') to the subsequent node.
    def __init__(self, value):
        # Constructor for the Node class.
        # Initializes a node with a specified value and sets its 'next' pointer to None initially.
        # 
        # Args:
        #     value: The data to be stored within this node.
        self.value = value  # Stores the data for the node.
        self.next = None  # Initializes the 'next' pointer; it will be updated to link nodes.

class LinkedList:
    # Defines the LinkedList class, which encapsulates the behavior of a linked list data structure.
    # It manages nodes, including the head (start), tail (end), and the list's length.
    def __init__(self, value):
        # Constructor for the LinkedList class.
        # Initializes a new linked list with a single node containing the given 'value'.
        # 
        # Args:
        #     value: The value for the initial node of the linked list.
        new_node = Node(value)      # Create a new Node instance.
        self.head = new_node        # The new node is initially the head of the list.
        self.tail = new_node        # It is also the tail of the list.
        self.length = 1             # The list starts with one node, so length is 1.

    # --- LL: Print List Method --- 
    def print_list(self):
        # Method to print all the values of the nodes in the linked list, one value per line.
        # It traverses the list from the head to the tail.
        
        temp = self.head  # Start with a temporary pointer ('temp') at the head of the list.
                          # This pointer will be used to iterate through the list.
        
        while temp is not None:  # Loop as long as 'temp' points to an existing node (not None).
                                 # 'None' indicates the end of the list has been reached.
            
            print(temp.value)  # Print the value stored in the current node pointed to by 'temp'.
            
            temp = temp.next   # Move 'temp' to the next node in the list.
                               # If 'temp' was the last node, 'temp.next' will be None,
                               # and the loop will terminate on the next check.
        # Once the loop finishes, all node values from head to tail have been printed.
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.print_list()


