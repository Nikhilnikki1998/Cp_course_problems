"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next!=None:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        current=self.head
        new_element.next=current
        current=new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        

class stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)
    def isempty(self):
        if(self.ll==None):
            return True
        else:
            return False

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        if(self.ll==None):
            self.ll=Element(new_element)
        else:
            temp=Element(new_element)
            temp.next=self.ll
            self.ll=temp
        

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        if(self.isempty()):
            return None
        else:
            temp=self.ll
            if(self.ll.next!=None):
                self.ll=self.ll.next
            else:
                self.ll=None
            temp.next=None
            return temp.value
            
    