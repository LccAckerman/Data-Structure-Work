class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class Queue:
    def __init__(self):
        self.instack = Stack()
        self.outstack = Stack()

    def size(self):
        return self.instack.size() + self.outstack.size()

    def enqueue(self, data):
        self.instack.push(data)

    def dequeue(self):
        if self.instack.size() == 0 and self.outstack.size() == 0:
            return None
        if self.outstack.size() == 0:
            while self.instack.size() != 0:
                self.outstack.push(self.instack.pop())
        return self.outstack.pop()


# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")