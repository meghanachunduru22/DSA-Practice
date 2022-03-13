class Queue:
    def __init__(self,n):
        self.front = -1
        self.rear = -1
        self.size = n
        self.q = [-1]*n
    def enque(self,x):
        self.rear += 1
        self.q[self.rear] = x
    def deque(self):
        if self.rear > self.front:
            self.front += 1
            print(self.q[self.front])
        else:
            print("Empty")


qu = Queue(20)
qu.enque(1)
qu.enque(2)
qu.enque(3)
qu.enque(4)
qu.enque(5)
qu.enque(6)
qu.enque(7)
qu.enque(8)
qu.deque()
qu.deque()
qu.deque()
qu.deque()
qu.deque()
qu.deque()
qu.deque()
qu.deque()
