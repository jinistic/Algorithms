class MyCircularQueue:
    def __init__(self, k: int):
        self.q = k * [None]
        self.maxlen = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.maxlen
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.maxlen
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.q[self.front] is None

    def isFull(self) -> bool:
        return self.q[self.rear] is not None


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
