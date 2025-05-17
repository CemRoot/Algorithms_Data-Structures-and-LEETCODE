class Node:
    # Think of a Node as a container or a box in our linked list.
    # Each box holds two things:
    # 1. The actual data or 'value' we want to store (like a number, a name, etc.).
    # 2. A pointer or a reference called 'next', which tells us where the next box in the sequence is.
    def __init__(self, value):
        # This is the constructor. It's called automatically when we create a new Node (a new box).
        # Args:
        #   value: The piece of data we want to put inside this new box.
        self.value = value  # We store the given 'value' inside this node.
        self.next = None  # Initially, when a new box is made, its 'next' pointer points to 'None'
                          # (nothing), because it's not yet connected to any other box.
        

class LinkedList:
    # The LinkedList is like a chain of these Node boxes.
    # This class helps us manage this chain: add new boxes, remove boxes, find boxes, etc.
    def __init__(self, value):
        # This is the constructor for our LinkedList.
        # When we first create a LinkedList, we start it with one box (Node).
        # Args:
        #   value: The value for the very first box in our new chain.
        new_node = Node(value)    # Create a brand new box (Node) with the given value.
        self.head = new_node      # The 'head' is a special pointer that always points to the *first* box in the chain.
                                  # So, our new box becomes the head.
        self.tail = new_node      # The 'tail' is another special pointer that always points to the *last* box in the chain.
                                  # Since we only have one box, it's both the first and the last.
        self.length = 1           # We keep track of how many boxes are in our chain. We start with 1.

    def print_list(self):
        # This method goes through each box in the chain, from start to end, and prints the value inside.
        temp = self.head  # We start at the 'head' (the first box).
        while temp is not None:  # We keep going as long as 'temp' is pointing to an actual box (not None).
                                 # 'None' means we've reached the end of the chain.
            print(temp.value)    # Print the value stored in the current box.
            temp = temp.next     # Move 'temp' to the next box in the chain, using the current box's 'next' pointer.
        
    def append(self, value):
        # 'append' means to add a new box (Node) to the very *end* of the chain.
        # Args:
        #   value: The value for the new box we're adding.
        # Returns:
        #   True: Just to indicate that the operation was successful.
        new_node = Node(value)  # Create the new box we want to add.
        if self.length == 0:  # Special case: If the chain is currently empty (no boxes).
            self.head = new_node  # The new box becomes both the first (head)...
            self.tail = new_node  # ...and the last (tail) box.
        else:  # If the chain already has some boxes.
            self.tail.next = new_node  # Take the current last box (tail) and make its 'next' pointer point to our new box.
            self.tail = new_node      # Our new box is now the very last box, so update the 'tail' pointer.
        self.length += 1  # We added a box, so increase the count of boxes in the chain.
        return True

    def pop(self):
        # 'pop' means to remove the *last* box from the end of the chain.
        # Returns:
        #   The box (Node) that was removed, or None if the chain was empty.
        if self.length == 0:  # If the chain is empty, there's nothing to remove.
            return None
        
        temp = self.head  # We need to find the box *before* the last one.
        pre = self.head   # 'pre' will be that second-to-last box.
        
        # We walk down the chain until 'temp' is the last box.
        # 'temp.next' will be None when 'temp' is the last box.
        while(temp.next):  
            pre = temp       # 'pre' always stays one step behind 'temp'.
            temp = temp.next # Move 'temp' forward.
            
        # Now, 'temp' is the last box (the one we want to remove).
        # 'pre' is the box right before it (which will become the new last box).
        self.tail = pre          # Make 'pre' the new tail.
        self.tail.next = None  # Break the chain: the new tail's 'next' pointer should point to nothing (None).
        self.length -= 1      # We removed a box, so decrease the count.
        
        # If we removed the *only* box, the chain is now empty.
        if self.length == 0:
            self.head = None
            self.tail = None
            
        return temp  # Return the box that we removed.

    def prepend(self, value):
        # 'prepend' means to add a new box (Node) to the very *beginning* of the chain.
        # Args:
        #   value: The value for the new box.
        # Returns:
        #   True: To indicate success.
        new_node = Node(value) # Create the new box.
        if self.length == 0: # If the chain is empty.
            self.head = new_node # The new box is both the head...
            self.tail = new_node # ...and the tail.
        else: # If there are already boxes in the chain.
            new_node.next = self.head # Make the new box's 'next' pointer point to the current first box (the old head).
            self.head = new_node      # Our new box is now the first box, so update the 'head' pointer.
        self.length += 1 # Increase the box count.
        return True

    def pop_first(self):
        # 'pop_first' means to remove the *first* box (the head) from the chain.
        # Returns:
        #   The box (Node) that was removed, or None if the chain was empty.
        if self.length == 0: # If empty, nothing to remove.
            return None
        
        temp = self.head          # Keep a temporary hold of the first box (the one we're removing).
        self.head = self.head.next # Make the *second* box in the chain the new 'head'.
        temp.next = None          # Disconnect the old first box from the chain by setting its 'next' to None.
        self.length -= 1          # Decrease the box count.
        
        # If we removed the only box, the chain is now empty.
        if self.length == 0:
            self.tail = None # The tail also needs to be None.
            
        return temp # Return the removed box.

    def get(self, index):
        # 'get' helps us find and return a box at a specific position (index) in the chain.
        # The positions are numbered starting from 0 (0 is the first box, 1 is the second, and so on).
        # Args:
        #   index: The position of the box we want.
        # Returns:
        #   The box (Node) at that position, or None if the index is invalid (e.g., too big or negative).
        if index < 0 or index >= self.length: # If the index is outside the valid range of our chain.
            return None # It's not a valid position.
        
        temp = self.head # Start at the beginning of the chain.
        # We need to take 'index' steps forward to reach the desired box.
        for _ in range(index): # The underscore `_` means we don't care about the loop counter value itself.
            temp = temp.next   # Move to the next box.
            
        return temp # After taking 'index' steps, 'temp' will be pointing to the box we want.
        
    def set_value(self, index, value):
        # 'set_value' changes the data (value) inside a box at a specific position (index).
        # Args:
        #   index: The position of the box we want to change.
        #   value: The new data to put into that box.
        # Returns:
        #   True: If we successfully found the box and changed its value.
        #   False: If the index was invalid and we couldn't find the box.
        temp = self.get(index) # First, let's use our 'get' method to find the box at the given index.
        if temp: # If 'get' found a box (i.e., 'temp' is not None).
            temp.value = value # Change the value inside that box.
            return True        # Report success!
        return False # If 'get' didn't find a box (index was bad), report failure.
    
    def insert(self, index, value):
        # 'insert' adds a new box with a given value at a specific position (index) in our chain.
        # Other boxes at or after this position will be shifted one step to the right.
        # Args:
        #   index: The position where we want to insert the new box (0 for start, 1 for after first, etc.).
        #          You can insert at an index from 0 up to self.length (which means at the end).
        #   value: The value for the new box.
        # Returns:
        #   True: If insertion was successful.
        #   False: If the index was invalid (e.g., negative or too large).

        # Check if the index is valid. It can't be negative or way past the end of the list.
        if index < 0 or index > self.length:
            return False # Not a valid spot to insert.

        # Case 1: Inserting at the very beginning (index 0).
        # We already have a method for this: prepend!
        if index == 0:
            return self.prepend(value) # prepend will handle everything and return True.

        # Case 2: Inserting at the very end (index is the same as the current length).
        # We also have a method for this: append!
        if index == self.length:
            return self.append(value) # append will handle everything and return True.

        # Case 3: Inserting somewhere in the middle of the chain.
        new_node = Node(value)  # Create the new box we want to insert.
        
        # We need to find the box that will be *before* our new box.
        # If we want to insert at 'index', the box before it is at 'index - 1'.
        temp = self.get(index - 1) # Use 'get' to find the box at position 'index - 1'.
        
        # Now we wire up the new box:
        # The new box's 'next' should point to whatever 'temp' (the box before) was originally pointing to.
        new_node.next = temp.next
        # Then, make 'temp' (the box before) point its 'next' to our new box.
        temp.next = new_node
        
        self.length += 1   # We've added a box, so increase the length.
        return True        # Report success!
  


# This is example code to test if our LinkedList and its 'insert' method work correctly.
my_linked_list = LinkedList(1) # Create a list. It initially contains: 1
my_linked_list.append(3)       # Add 3 to the end. List is now: 1 -> 3


print('LL before insert():') # Show the list before we insert anything else.
my_linked_list.print_list()   # Expected: 1, then 3 on the next line.


my_linked_list.insert(1,2) # Try to insert the value 2 at index 1.
                           # The list was 1 -> 3. Index 1 is where 3 is.
                           # So, 2 should go between 1 and 3. List becomes: 1 -> 2 -> 3.

print('\nLL after insert(2) in middle:') # Show the list after the first insert.
my_linked_list.print_list()            # Expected: 1, 2, 3


my_linked_list.insert(0,0) # Try to insert value 0 at index 0 (the beginning).
                           # List was 1 -> 2 -> 3. Should become: 0 -> 1 -> 2 -> 3.

print('\nLL after insert(0) at beginning:') # Show the list.
my_linked_list.print_list()               # Expected: 0, 1, 2, 3


my_linked_list.insert(4,4) # Try to insert value 4 at index 4.
                           # List was 0 -> 1 -> 2 -> 3. Length is 4.
                           # Index 4 means at the end. Should become: 0 -> 1 -> 2 -> 3 -> 4.

print('\nLL after insert(4) at end:') # Show the list.
my_linked_list.print_list()           # Expected: 0, 1, 2, 3, 4



"""
    EXPECTED OUTPUT:
    ----------------
    LL before insert():
    1
    3

    LL after insert(2) in middle:
    1
    2
    3

    LL after insert(0) at beginning:
    0
    1
    2
    3

    LL after insert(4) at end:
    0
    1
    2
    3
    4

"""