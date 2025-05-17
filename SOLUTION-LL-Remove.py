class Node:
    # Defines the Node class. Think of a Node as a single link or a "box" in our chain (Linked List).
    # Each box holds two pieces of information:
    # 1. 'value': The actual data we want to store (e.g., a number, a name).
    # 2. 'next': A pointer or reference to the next box in the chain. If it's the last box, 'next' will be None.
    def __init__(self, value):
        # This is the constructor for the Node class. It's called when we create a new Node.
        # Args:
        #   value: The data to store in this new node.
        self.value = value  # Store the provided value in this node.
        self.next = None  # Initially, this new node doesn't point to any other node, so 'next' is None.
        

class LinkedList:
    # Defines the LinkedList class. This class manages the entire chain of Nodes.
    # It provides methods to add, remove, find, and modify nodes in the list.
    def __init__(self, value):
        # Constructor for the LinkedList. Called when we create a new LinkedList.
        # It starts the list with a single node.
        # Args:
        #   value: The value for the very first node in our new list.
        new_node = Node(value)    # Create a new Node object.
        self.head = new_node      # The 'head' pointer always points to the first node in the list.
        self.tail = new_node      # The 'tail' pointer always points to the last node in the list.
                                  # Since there's only one node, it's both the head and the tail.
        self.length = 1           # Keep track of the number of nodes in the list. Starts at 1.

    def print_list(self):
        # This method prints the values of all nodes in the list, from head to tail.
        temp = self.head  # Start with a temporary pointer at the head.
        while temp is not None:  # Loop as long as 'temp' is pointing to an actual node.
            print(temp.value)    # Print the value of the current node.
            temp = temp.next     # Move 'temp' to the next node in the list.
        
    def append(self, value):
        # Adds a new node with the given 'value' to the *end* of the list (after the current tail).
        # Args:
        #   value: The value for the new node.
        # Returns:
        #   True, to indicate the operation was successful.
        new_node = Node(value)  # Create the new node.
        if self.length == 0:  # If the list is empty.
            self.head = new_node  # The new node is both the head and the tail.
            self.tail = new_node
        else:  # If the list is not empty.
            self.tail.next = new_node  # Make the current tail's 'next' pointer point to the new node.
            self.tail = new_node      # The new node is now the new tail.
        self.length += 1  # Increment the length of the list.
        return True

    def pop(self):
        # Removes and returns the *last* node (the tail) from the list.
        # Returns None if the list is empty.
        if self.length == 0:
            return None
        
        temp = self.head  # 'temp' will traverse the list to find the last node.
        pre = self.head   # 'pre' will trail 'temp' to become the new tail.
        
        while(temp.next):  # Loop until 'temp' is the last node (its 'next' is None).
            pre = temp
            temp = temp.next
            
        self.tail = pre          # The node before the old tail ('pre') is the new tail.
        self.tail.next = None  # Break the link from the new tail to the old (removed) tail.
        self.length -= 1      # Decrement the length.
        
        if self.length == 0:  # If the list became empty after popping.
            self.head = None
            self.tail = None
            
        return temp  # Return the node that was removed.

    def prepend(self, value):
        # Adds a new node with the given 'value' to the *beginning* of the list (before the current head).
        # Args:
        #   value: The value for the new node.
        # Returns:
        #   True, to indicate success.
        new_node = Node(value) # Create the new node.
        if self.length == 0: # If the list is empty.
            self.head = new_node # The new node is both head and tail.
            self.tail = new_node
        else: # If the list is not empty.
            new_node.next = self.head # Make the new node's 'next' point to the current head.
            self.head = new_node      # The new node becomes the new head.
        self.length += 1 # Increment the length.
        return True

    def pop_first(self):
        # Removes and returns the *first* node (the head) from the list.
        # Returns None if the list is empty.
        if self.length == 0:
            return None
        
        temp = self.head          # Temporarily store the current head (the node to be removed).
        self.head = self.head.next # Make the second node the new head.
        temp.next = None          # Disconnect the old head from the list.
        self.length -= 1          # Decrement the length.
        
        if self.length == 0: # If the list became empty.
            self.tail = None # The tail must also be None.
            
        return temp # Return the removed node.

    def get(self, index):
        # Retrieves the node at a specific 'index' in the list (0-indexed).
        # Args:
        #   index: The position (0 for head, 1 for second, etc.) of the node to get.
        # Returns:
        #   The Node object at the specified index, or None if the index is invalid.
        if index < 0 or index >= self.length: # Index out of bounds.
            return None
        
        temp = self.head # Start at the head.
        for _ in range(index): # Loop 'index' times to move to the desired node.
            temp = temp.next
            
        return temp # Return the node found at that index.
        
    def set_value(self, index, value):
        # Changes the 'value' of the node at a specific 'index'.
        # Args:
        #   index: The position of the node to modify.
        #   value: The new value to set for that node.
        # Returns:
        #   True if the value was set successfully (index was valid).
        #   False if the index was invalid.
        temp = self.get(index) # Use the 'get' method to find the node.
        if temp: # If a node was found (get didn't return None).
            temp.value = value # Update its value.
            return True
        return False # Node not found at index.
    
    def insert(self, index, value):
        # Inserts a new node with the given 'value' at a specific 'index'.
        # Nodes at and after the index are shifted to the right.
        # Args:
        #   index: The position where the new node should be inserted (0 to self.length).
        #   value: The value for the new node.
        # Returns:
        #   True if insertion was successful.
        #   False if the index was invalid.
        if index < 0 or index > self.length: # Invalid index.
            return False
        if index == 0: # Inserting at the beginning.
            return self.prepend(value)
        if index == self.length: # Inserting at the end.
            return self.append(value)
        
        # Inserting in the middle.
        new_node = Node(value)       # Create the new node.
        pre = self.get(index - 1)  # Get the node *before* the insertion point.
        new_node.next = pre.next   # New node points to what 'pre' was pointing to.
        pre.next = new_node        # 'pre' now points to the new node.
        self.length += 1           # Increment length.
        return True  

    def remove(self, index):
        # Removes and returns the node at a specific 'index' from the list.
        # Args:
        #   index: The position of the node to remove (0-indexed).
        # Returns:
        #   The removed Node object, or None if the index is invalid or list is empty.

        # 1. Check for invalid index (less than 0 or greater than or equal to current length).
        if index < 0 or index >= self.length:
            return None  # Cannot remove from an invalid position.

        # 2. Case: Removing the first node (head) - index is 0.
        #    We can use our existing pop_first() method for this.
        if index == 0:
            return self.pop_first()

        # 3. Case: Removing the last node (tail) - index is self.length - 1.
        #    We can use our existing pop() method for this.
        if index == self.length - 1:
            return self.pop()

        # 4. Case: Removing a node from the middle of the list.
        #    We need to find the node *before* the one we want to remove.
        #    Let's call this 'pre'. The node to remove will be 'pre.next'.
        pre = self.get(index - 1)  # Get the node at 'index - 1'.
        
        # The node to be removed is the one currently after 'pre'.
        # Let's call it 'temp' for clarity (though it's pre.next).
        temp = pre.next 
        
        # To remove 'temp', we make 'pre' skip over 'temp' and point directly
        # to whatever 'temp' was pointing to.
        pre.next = temp.next
        
        # It's good practice to completely disconnect the removed node from the list.
        temp.next = None 
        
        self.length -= 1  # We've removed a node, so decrease the length.
        return temp       # Return the removed node.
  


# Example code to test the 'remove' method.
my_linked_list = LinkedList(1) # List: 1
my_linked_list.append(2)       # List: 1 -> 2
my_linked_list.append(3)       # List: 1 -> 2 -> 3
my_linked_list.append(4)       # List: 1 -> 2 -> 3 -> 4
my_linked_list.append(5)       # List: 1 -> 2 -> 3 -> 4 -> 5

print('LL before remove():')
my_linked_list.print_list()    # Print the initial list.

print('\nRemoved node:')
# Remove the node at index 2 (which is the node with value 3).
removed_node_middle = my_linked_list.remove(2)
if removed_node_middle:
    print(removed_node_middle.value) # Expected: 3
print('LL after remove() in middle:')
my_linked_list.print_list()        # Expected: 1, 2, 4, 5

print('\nRemoved node:')
# Remove the node at index 0 (the first node, which is now 1).
removed_node_first = my_linked_list.remove(0)
if removed_node_first:
    print(removed_node_first.value) # Expected: 1
print('LL after remove() of first node:')
my_linked_list.print_list()       # Expected: 2, 4, 5

print('\nRemoved node:')
# Remove the node at index 2 (in the current list 2 -> 4 -> 5, index 2 is node 5, the last one).
removed_node_last = my_linked_list.remove(2)
if removed_node_last:
    print(removed_node_last.value) # Expected: 5
print('LL after remove() of last node:')
my_linked_list.print_list()        # Expected: 2, 4



"""
    EXPECTED OUTPUT:
    ----------------
    LL before remove():
    1
    2
    3
    4
    5

    Removed node:
    3
    LL after remove() in middle:
    1
    2
    4
    5

    Removed node:
    1
    LL after remove() of first node:
    2
    4
    5

    Removed node:
    5
    LL after remove() of last node:
    2
    4

"""

