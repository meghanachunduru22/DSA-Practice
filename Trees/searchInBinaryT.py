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

def searchTree(root,k):
    if root is None:
        return False
    elif root.val == k:
        return True
    elif searchTree(root.left,k) == True:
        return True
    else:
        return searchTree(root.right,k)

# def ifNodeExists(node, key):
 
#     if (node == None):
#         return False
 
#     if (node.data == key):
#         return True
 
#     """ then recur on left subtree """
#     res1 = ifNodeExists(node.left, key)
#     # node found, no need to look further
#     if res1:
#         return True
 
#     """ node is not found in left,
#     so recur on right subtree """
#     res2 = ifNodeExists(node.right, key)
 
#     return res2      

print(searchTree(root,4))