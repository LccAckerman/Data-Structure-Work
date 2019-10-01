class Queue:
    def __init__(self, initial_size = 10):
        self.arr = [0 for n in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.size() == 0

    def front(self):
        if self.is_empty():
            return None
        return self.arr[self.front_index]

    def dequeue(self):
        if self.is_empty():
            self.front_index = -1
            self.next_index = 0
            return None
        de_elem = self.front()
        self.front_index = (self.front_index +1) % len(self.arr)
        self.queue_size -= 1
        return de_elem

    def _handle_queue_capacity_full(self):
        old_arr = [item for item in self.arr]
        self.arr = [0 for n in range(len(self.arr)*2)]
        myIndex = 0
        for index, value in enumerate(old_arr):
            self.arr[index] = old_arr[index]
            myIndex += 1

        for i in range(0, self.front_index):
            self.arr[myIndex] = old_arr[i]
            myIndex += 1

        self.front_index = 0
        self.next_index = myIndex


# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")