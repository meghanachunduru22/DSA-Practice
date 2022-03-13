class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
#Driver Code
a = Node(10)
a.left = Node(50)
a.left.left = Node(40)
a.left.right = Node(25)
a.right = Node(30)
a.right.left = Node(80)

def countNodes(root):
    if root == None:
        return 0
    else:
        return 1+ countNodes(root.left) + countNodes(root.right)

print(countNodes(a))