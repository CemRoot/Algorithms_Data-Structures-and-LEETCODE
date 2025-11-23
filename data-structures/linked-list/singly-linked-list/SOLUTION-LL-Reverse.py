class Node:
    # Defines the Node class. Each Node is like a single "box" or link in our list.
    # It holds: 
    #   1. 'value': The actual data (e.g., a number, text).
    #   2. 'next': A pointer to the very next Node in the sequence. If it's the last Node, 'next' is None.
    def __init__(self, value):
        # This is the constructor, called when we do "Node(some_value)".
        # It sets up a new Node.
        self.value = value  # Store the passed-in value inside this Node.
        self.next = None  # When a Node is first created, it doesn't point to anything yet.
        

class LinkedList:
    # Defines the LinkedList class. This manages the whole chain of Nodes.
    # It provides ways to add, remove, find, and manipulate the Nodes in the list.
    def __init__(self, value):
        # Constructor for LinkedList. This is called when we do "LinkedList(some_value)".
        # It creates a new list starting with a single Node.
        new_node = Node(value)    # Create the first Node.
        self.head = new_node      # The 'head' always points to the first Node in the list.
        self.tail = new_node      # The 'tail' always points to the last Node. For a new list, head and tail are the same.
        self.length = 1           # Keep track of how many Nodes are in the list.

    def print_list(self):
        # Goes through the list from head to tail and prints the value of each Node.
        temp = self.head  # Start with a temporary pointer at the head.
        while temp is not None:  # Keep looping as long as 'temp' is pointing to an actual Node.
            print(temp.value)    # Print the value in the current Node.
            temp = temp.next     # Move 'temp' to the next Node in the chain.
        
    def append(self, value):
        # Adds a new Node with the given 'value' to the very end of the list.
        new_node = Node(value)
        if self.length == 0:  # If the list is currently empty.
            self.head = new_node
            self.tail = new_node
        else:  # If the list already has Nodes.
            self.tail.next = new_node  # Make the current last Node point to the new one.
            self.tail = new_node      # The new Node is now the last one (the new tail).
        self.length += 1
        return True

    def pop(self):
        # Removes and returns the last Node from the list. Returns None if the list is empty.
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next): # Loop until 'temp' is the last Node.
            pre = temp
            temp = temp.next
        self.tail = pre          # The Node before the old tail ('pre') is now the new tail.
        self.tail.next = None  # Break the link to the old tail.
        self.length -= 1
        if self.length == 0:  # If the list became empty.
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        # Adds a new Node with the given 'value' to the very beginning of the list.
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head # The new Node points to the old head.
            self.head = new_node      # The new Node becomes the new head.
        self.length += 1
        return True

    def pop_first(self):
        # Removes and returns the first Node from the list. Returns None if the list is empty.
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next # The second Node (if any) becomes the new head.
        temp.next = None          # Disconnect the old head from the list.
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        # Finds and returns the Node at a specific 'index' (position) in the list.
        # Index 0 is the head, 1 is the second, and so on.
        # Returns None if the index is invalid (out of bounds).
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index): # Loop 'index' number of times.
            temp = temp.next   # Move 'temp' forward each time.
        return temp # 'temp' is now at the desired Node.
        
    def set_value(self, index, value):
        # Changes the 'value' inside the Node at a specific 'index'.
        # Returns True if successful, False if the index was invalid.
        temp = self.get(index) # Use our 'get' method to find the Node.
        if temp: # If 'get' returned a Node (not None).
            temp.value = value # Change its value.
            return True
        return False # Index was invalid.
    
    def insert(self, index, value):
        # Inserts a new Node with 'value' at the specified 'index'.
        # Nodes from that index onwards are shifted to the right.
        # Returns True if successful, False if index is invalid.
        if index < 0 or index > self.length: # Index can be 0 up to current length (for appending).
            return False
        if index == 0:
            return self.prepend(value) # Use prepend for index 0.
        if index == self.length:
            return self.append(value)  # Use append for index == length.
        
        new_node = Node(value)
        pre = self.get(index - 1) # Get the Node *before* the insertion point.
        new_node.next = pre.next    # New Node points to what 'pre' was pointing to.
        pre.next = new_node         # 'pre' now points to the new Node.
        self.length += 1   
        return True  

    def remove(self, index):
        # Removes and returns the Node at the specified 'index'.
        # Returns None if the index is invalid.
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first() # Use pop_first for index 0.
        if index == self.length - 1:
            return self.pop()       # Use pop for the last element.
        
        pre = self.get(index - 1) # Get Node before the one to remove.
        temp = pre.next           # This is the Node to remove.
        pre.next = temp.next      # 'pre' skips over 'temp'.
        temp.next = None          # Disconnect 'temp' from the list.
        self.length -= 1
        return temp

    def reverse(self):
        # This method reverses the linked list *in place*.
        # The head becomes the tail, the tail becomes the head, and all 'next' pointers are flipped.
        # IMPORTANT: This specific implementation assumes the list is not empty when called.
        # If self.length is 0, self.head would be None, and accessing temp.next (None.next) below
        # before the loop would cause an AttributeError.

        # Step 1: Swap the head and tail pointers of the list.
        #   Store the original head in a temporary variable.
        temp = self.head          # 'temp' now holds the original head node.
        #   The list's head pointer is updated to point to the original tail node.
        self.head = self.tail
        #   The list's tail pointer is updated to point to the original head node (which we saved in 'temp').
        self.tail = temp          # Now, self.tail points to the original head node.
                                  # And 'temp' also points to the original head node.

        # Step 2: Initialize pointers needed for iterating and reversing the links.
        #   'after':  Will temporarily store the *next* node in the original list sequence,
        #             so we don't lose it when we change the current node's 'next' pointer.
        #             'temp' (our current processing node) starts as the original head.
        after = temp.next         # So, 'after' is initially the second node of the original list.
        #   'before': Will store the node that comes *before* the current node in the *new* reversed order.
        #             It starts as None because the new tail (original head) will point to None in the reversed list.
        before = None

        # Step 3: Iterate through the list, node by node, and reverse each node's 'next' pointer.
        #   The loop will run 'self.length' times to process each node.
        #   'temp' is our current node, starting at the original head (now self.tail).
        for _ in range(self.length):
            # Inside the loop, 'temp' refers to the node we are currently processing.
            
            # Save the node that comes *after* the current 'temp' node in the original list.
            # This is important because we are about to change 'temp.next'.
            # Note: In the first iteration, 'after' was already set to temp.next (original second node).
            # In subsequent iterations, this line updates 'after' based on the current 'temp'.
            after = temp.next 
            
            # Reverse the pointer: Make the current node ('temp') point its 'next' to 'before'.
            # 'before' is the node that was processed in the previous iteration (or None for the first node).
            temp.next = before 
            
            # Move all pointers one step forward for the next iteration:
            # The node we just processed ('temp') now becomes the 'before' node for the *next* node in the sequence.
            before = temp
            # The node we saved as 'after' becomes the new current node ('temp') to be processed.
            temp = after
            # The loop continues. When 'temp' becomes None (after processing the original tail, which is now the new head),
            # 'before' will be pointing to the new head, and all pointers are correctly reversed.
  


# This is example code to test if our LinkedList and its 'reverse' method work correctly.
my_linked_list = LinkedList(1) # Create a list. Initially: 1
my_linked_list.append(2)       # Add 2 to the end. List: 1 -> 2
my_linked_list.append(3)       # Add 3. List: 1 -> 2 -> 3
my_linked_list.append(4)       # Add 4. List: 1 -> 2 -> 3 -> 4

print('LL before reverse():')   # Show the list before reversing.
my_linked_list.print_list()      # Expected: 1, 2, 3, 4 (each on a new line)

my_linked_list.reverse()         # Call the reverse method to flip the list.

print('\nLL after reverse():')    # Show the list after reversing.
my_linked_list.print_list()      # Expected: 4, 3, 2, 1 (each on a new line)



"""
    EXPECTED OUTPUT:
    ----------------
    LL before reverse():
    1
    2
    3
    4

    LL after reverse():
    4
    3
    2
    1
    
"""