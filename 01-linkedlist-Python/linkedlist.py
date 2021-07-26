"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        new_node = Element(new_element)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next =  new_node
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        current = self.head
        count = 0
        while (current):
            if (count == position):
                return current.data
            count += 1
            current = current.next

        return None
    def getNode(self,data):
 
    # allocating space
        newNode = Element(data)
        return newNode
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        
        head = self.head
        
        # This condition to check whether the
        # position given is valid or not.
        if (position < 1):       
            print("Invalid position!")
        
        if position == 1:
            newNode = Element(new_element)
            newNode.next = self.head
            head = newNode
                
        else:
        
            # Keep looping until the position is zero
            while (position != 0):          
                position -= 1
    
                if (position == 1):
                    newNode = getNode(new_element)

                    newNode.next = self.head.next
    
                # Replacing headNode with new Node
                # to the old Node to point to the new Node
                    self.head.next = newNode
                    break
                
                self.head = self.head.next
                if self.head == None:
                    break           
            if position != 1:
                print("position out of range")       
        return head
            
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        pass
