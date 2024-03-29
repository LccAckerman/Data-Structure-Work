class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.num_elements += 1

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.is_empty():
            return None
        elem = self.head
        self.head = elem.next
        self.num_elements -= 1
        return elem.val


# Setup
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

# Test size
print("Pass" if (stack.size() == 5) else "Fail")

# Test pop
print("Pass" if (stack.pop() == 50) else "Fail")

# Test push
stack.push(60)
print("Pass" if (stack.pop() == 60) else "Fail")
print("Pass" if (stack.pop() == 40) else "Fail")
print("Pass" if (stack.pop() == 30) else "Fail")
stack.push(50)
print("Pass" if (stack.size() == 3) else "Fail")
