class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            return
        else:
            newnode.next = self.head
            self.head = newnode

    def append(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        else:
            tmp = self.head
            while tmp is not None:
                tmp = tmp.next
            tmp = newnode

    def search(self, data):
        tmp = self.head
        while tmp is not None:
            if tmp.value == data:
                return tmp
            tmp = tmp.next

    def remove(self, data):
        if self.head is None:
            return
        if self.head.value == data:
            self.head = self.head.next
            return
        tmp = self.head
        while tmp is not None:
            if tmp.next.value == data:
                tmp.next = tmp.next.next
                return
            tmp = tmp.next

    def pop(self):
        if self.head is None:
            return
        rst = self.head.value
        self.head = self.head.next
        return rst

    def insert(self, data, pos):
        if pos == 0:
            self.prepend(data)
        elif pos >= self.size():
            self.append(data)
        else:
            count = 0
            tmp = self.head
            while tmp is not None:
                if count == pos - 1:
                    newnode = Node(data)
                    newnode.next = tmp.next
                    tmp.next = newnode
                    return
                count += 1
                tmp = tmp.next

    def size(self):
        if self.head is None:
            return 0
        count = 0
        tmp = self.head
        while tmp is not None:
            count += 1
            tmp = tmp.next
        return count

    def to_list(self):
        out = []
        tmp = self.head
        while tmp:
            out.append(tmp.value)
            tmp = tmp.next
        return out




class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """ Prepend a node to the beginning of the list """

        if self.head is None:
            self.head = Node(value)
            return

        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def append(self, value):
        """ Append a node to the end of the list """
        # Here I'm not keeping track of the tail. It's possible to store the tail
        # as well as the head, which makes appending like this an O(1) operation.
        # Otherwise, it's an O(N) operation as you have to iterate through the
        # entire list to add a new tail.

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            return None

        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

        raise ValueError("Value not found in the list.")


    def remove(self, value):
        """ Delete the first node with the desired data. """
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next

        raise ValueError("Value not found in the list.")


    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next

        return node.value

    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        if pos == 0:
            self.prepend(value)
            return

        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return

            index += 1
            node = node.next
        else:
            self.append(value)

    def size(self):
        """ Return the size or length of the linked list. """
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out




# Test your implementation here

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
print('test prepend done')
# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"
print('test append done')

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"
print('test search done')

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"
print('test remove done')

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"
print('test pop done')

# Test insert
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
print('test insert done')

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"
print('test size done')


# In[45]:
