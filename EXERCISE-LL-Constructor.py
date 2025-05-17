# class Node:
    ## WRITE NODE CONSTRUCTOR HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################
        
# class LinkedList:
    ## WRITE LL CONSTRUCTOR HERE ##
    #                             #
    #                             #
    #                             #
    #                             #
    ###############################



 
my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

class Node:
    # Defines the Node class, which is a building block for a linked list.
    # Each Node object will store a piece of data (value) and a reference (next)
    # to the next Node in the sequence.
    def __init__(self, value):
        # Constructor for the Node class.
        # Initializes a new Node object.
        #
        # Args:
        #     value: The data to be stored in this node.
        self.value = value  # Assigns the provided value to the node's value attribute.
        self.next = None  # Initializes the 'next' pointer to None, indicating that
                          # by default, this node does not point to another node.

class LinkedList:
    # Defines the LinkedList class, which manages a sequence of Node objects.
    # It keeps track of the beginning (head) and end (tail) of the list,
    # as well as its overall length.

    # --- LL: Constructor Exercise ---
    def __init__(self, value):
        # Constructor for the LinkedList class.
        # This method is called when a new LinkedList object is created.
        # It initializes the linked list with a single node containing the given value.
        #
        # Args:
        #     value: The value for the first node in the linked list.

        # 1. Create a new Node object using the provided 'value'.
        #    This new node will be the first and only node in the list initially.
        new_node = Node(value)

        # 2. Set the 'head' of the linked list to point to this 'new_node'.
        #    The head is the entry point to the list.
        self.head = new_node

        # 3. Set the 'tail' of the linked list to also point to this 'new_node'.
        #    Since there's only one node, it's both the head and the tail.
        self.tail = new_node

        # 4. Initialize the 'length' of the linked list to 1.
        #    This reflects that the list currently contains one node.
        self.length = 1

# --- Example of how to use the constructor (for testing) ---
# my_linked_list = LinkedList(4)

# print('Head:', my_linked_list.head.value)  # Expected: 4
# print('Tail:', my_linked_list.tail.value)  # Expected: 4
# print('Length:', my_linked_list.length)    # Expected: 1

# """
#     EXPECTED OUTPUT (if example code is uncommented):
#     -------------------------------------------------
#     Head: 4
#     Tail: 4
#     Length: 1
# """

                                                                                                                    