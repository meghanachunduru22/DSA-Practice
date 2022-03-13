class Node:
    def __init__(self,x):
        self.val = x
        self.next = None




def removedups(head):
    if head.next == None:
        return head
    first = True
    prev= Node(0)
    temp = prev
    cur = head
    nextt = head.next
    while(cur!=None and nextt!=None):
        while(nextt!=None and cur.val == nextt.val):
            nextt = nextt.next
        # print(nextt.val)
        if nextt != None and nextt.next!=None and nextt.val != nextt.next.val:
            if first and cur.val != nextt.val:
                prev.next = cur
                prev = prev.next
            first = False
            prev.next = nextt
            cur = nextt
            nextt = cur.next
            prev = prev.next
        else:
            if nextt == None:
                return temp.next
            cur = nextt
            nextt = cur.next
        
        
    return temp.next








a = Node(1)
b = Node(1)
c = Node(3)
# d = Node(4)
# e = Node(5)
# f = Node(5)
# g = Node(8)
# h = Node(8)

a.next = b
b.next = c
# c.next = d
# d.next = e
# e.next = f
# f.next = g
# g.next = h
head = a
def printt(head):
    while(head!=None):
        print(head.val,end = " ")
        head = head.next
    print()

printt(head)
n = removedups(head)
printt(n)
















