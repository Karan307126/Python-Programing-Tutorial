class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def incertion(self):
        cheak = input("Do you want to add a new node? (yes or no) : ")
        if cheak == "no":
            return None
        
        val = int(input("Enter value : "))
        new_node = Node(val)
        print(f"Enter left child of {val}.")
        new_node.left = self.incertion()
        print(f"Enter right child of {val}.")
        new_node.right = self.incertion()

        return new_node

def presidesore(root):
    temp = root
    while temp and temp.right:
        temp = temp.left
    
    return temp



def inorderd(root):
    if root is None:
        return
        
    root.left = inorderd(root.left)
    print(root.data, end=" ")
    root.right = inorderd(root.right)
        
        
        

t = BinaryTree()
t.root = t.incertion()
inorderd(t.root)