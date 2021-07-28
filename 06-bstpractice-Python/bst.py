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
        pass
    def printSelf(self):
        # Your code goes here
        if self.root:
            BST.printSelf(self.root.left)
            print(self.root.value)
            BST.printSelf(self.root.right)

        
    def search(self, find_val):

        # if self.root is None or self.root.value == find_val:
        #     return self.root.value
        # if self.root.value < find_val:
        #     return BST.search(self.root.right,find_val)
        # return BST.search(self.root.left,find_val)
        pass

    

