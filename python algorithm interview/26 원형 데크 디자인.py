class MyCircularDeque:
    def __init__(self, k: int):
        self.dq = k * [None]
        self.maxlen = k
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.dq[self.front - 1] = value
            self.front = (self.front - 1) % self.maxlen
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.dq[self.rear] = value
            self.rear = (self.rear + 1) % self.maxlen
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.dq[self.front] = None
            self.front = (self.front + 1) % self.maxlen
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.dq[self.rear - 1] = None
            self.rear = (self.rear - 1) % self.maxlen
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.dq[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.dq[self.rear - 1]

    def isEmpty(self) -> bool:
        return self.dq[self.front] is None

    def isFull(self) -> bool:
        return self.dq[self.rear] is not None


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
