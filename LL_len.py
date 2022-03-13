class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
p=Node(1)
q=Node(2)
r=Node(3)
p.next = q
q.next = r

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
# b.next =  c


def length(head):
    count=0
    while head!=None:
        count += 1
        head = head.next
    return count
    
print(length(p)==length(a))


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None



# def lenn(head):
#     ct = 0
#     while(head != None):
#         ct+= 1
#         head = head.next
#     return ct

# print(lenn(a))