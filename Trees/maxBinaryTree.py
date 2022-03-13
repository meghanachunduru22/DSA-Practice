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

def MaxNode(root):
    if root.left == None and root.right == None:
        return root.val
    elif root.left == None and root.right != None:
        return MaxNode(root.right)
    elif root.right == None and root.left != None:
        return MaxNode(root.left)
    else:

        ml = MaxNode(root.left)
        mr = MaxNode(root.right)

        return max(root.val, ml,mr)

print(MaxNode(a))