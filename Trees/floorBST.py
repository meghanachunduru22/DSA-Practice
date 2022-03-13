class Node:
	
	def __init__(self, x):
		
		self.val = x
		self.left = None
		self.right = None

# Helper function to find floor and
# ceil of a given key in BST

def floorBST(root,key,temp):
	if root:
		if root.val == key:
			return key
		if root.val > key:
			return floorBST(root.left,key,temp)
		if root.val < key:
			temp = root.val
			return floorBST(root.right,key,temp)
	return temp
        
def ceilBST(root,key,temp):
	if root:
		# print(root.val)
		if root.val == key:
			return key
		elif root.val > key:
			temp = root.val
			return ceilBST(root.left,key,temp)
		else:
			
			return ceilBST(root.right,key,temp)
	return temp

# Driver code
if __name__ == '__main__':
	
	floor, ceil = -1, -1
	
	root = Node(8)
	root.left = Node(4)
	root.right = Node(12)
	root.left.left = Node(2)
	root.left.right = Node(6)
	root.right.left = Node(10)
	root.right.right = Node(14)

	for i in range(16):
		print(i,floorBST(root, i,temp=-1),ceilBST(root, i,temp=-1))
	# print(ceilBST(root, 1,temp=-1))