class Stack:
    def __init__(self, size = 10):
        self.arr = [x for x in range(size)]
        self.next_index = 0
        self.num_elements = 0
    def push(self, data):
        if self.next_index == len(self.arr):
            print("Out of Space!")
            self._handle_stack_capacity_full()
        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1
    def _handle_stack_capacity_full(self):
        old_arr = self.arr

        self.arr = [0 for x in range(2*len(old_arr))]
        for index in range(len(old_arr)):
            self.arr[index] = old_arr[index]
    def is_empty(self):
        return self.num_elements == 0
    def size(self):
        return self.num_elements
    def pop(self):
        if self.is_empty():
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]
