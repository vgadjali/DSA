class Node():
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BST():
    
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            #if empty tree
            self.root = newNode
            return True
        current = self.root
        while True:
            print("loop: {}".format(current.value))
            if current.value > value:
                #go to the left
                if current.left == None:
                    current.left = newNode
                    return True
                else:
                    current = current.left
            else:
                #go to the right
                if current.right == None:
                    current.right = newNode
                    return True
                else:
                    current = current.right

    def find(self, value):
        current = self.root
        while current:
            if current.value == value:
                return current
            elif current.value > value:
                #go to the left
                current = current.left
            else:
                #go to the right
                current = current.right
        return None