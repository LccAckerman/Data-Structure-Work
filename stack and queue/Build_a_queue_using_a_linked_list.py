class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_element = 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.num_element == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        self.num_element += 1

    def size(self):
        return self.num_element

    def is_empty(self):
        return self.num_element == 0

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            poped = self.head.value
            self.head = self.head.next
            self.num_element -= 1
            return poped


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