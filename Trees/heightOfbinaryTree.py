class newNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
#Driver Code
root = newNode(0)
root.left = newNode(1)
root.left.left = newNode(3)
root.left.left.left = newNode(7)
root.left.right = newNode(4)
root.left.right.left = newNode(8)
root.left.right.right = newNode(9)
root.right = newNode(2)
root.right.left = newNode(5)
root.right.right = newNode(6)

def hOfBTree(root):
    if root == None:
        return 0
    else:
        return 1+ max( hOfBTree(root.left), hOfBTree(root.right))

print(hOfBTree(root))