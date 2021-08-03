class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # if self.root is None:
        #     return Node(new_val)
        # else:
        #     if self.root.value == new_val:
        #         return self.root
        #     elif self.root.value < new_val:
        #         self.root.right = BST.insert(self.root.right, new_val)
        #     else:
        #         self.root.left = BST.insert(self.root.left, new_val)
        # return self.root
        new_Node=Node(new_val)
        if(self.root==None):
            self.root=new_Node
        else:
            current=self.root
            root1=self.root
            while(current!=None):
                root1=current
                if(new_val<current.value):
                    current = current.left
                else:
                    current=current.right
            if(new_val<root1.value):
                root1.left=new_Node
            else:
                root1.right=new_Node
    def printSelf(self):
        # Your code goes here
        print(self.root)

        
    def search(self, find_val):

        # if self.root is None or self.root.value == find_val:
        #     return self.root.value
        # if self.root.value < find_val:
        #     return BST.search(self.root.right,find_val)
        # return BST.search(self.root.left,find_val)
        while(self.root!=None):
            if(self.root.value==find_val):
                return True
            if(self.root.value<find_val):
                self.root=self.root.right
            else:
                self.root=self.root.left
        return False

    

