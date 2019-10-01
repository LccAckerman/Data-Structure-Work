class LinkedListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            tmpNode = self.head
            self.head = tmpNode.next
        self.num_elements -= 1
        return tmpNode.val


# def evaluate_post_fix(input_list):
#     mylist = list(input_list)
#     mystack = Stack()
#     for item in mylist:
#         if item == "+":
#             try:
#                 a = mystack.pop()
#                 b = mystack.pop()
#                 print(a)
#                 print(b)
#             except:
#                 result = a + b
#                 mystack.push(result)
#         elif item == "-":
#             a = mystack.pop()
#             b = mystack.pop()
#             result = a - b
#             mystack.push(result)
#         elif item == "*":
#             a = mystack.pop()
#             b = mystack.pop()
#             result = a * b
#             mystack.push(result)
#         elif item == "/":
#             a = mystack.pop()
#             b = mystack.pop()
#             result = int(a // b)
#             mystack.push(result)
#         else:
#             mystack.push(int(item))
#     return mystack.pop()
def evaluate_post_fix(input_list):
    stack = Stack()
    for element in input_list:
        if element == '*':
            second = stack.pop()
            first = stack.pop()
            output = first * second
            stack.push(output)
        elif element == '/':
            second = stack.pop()
            first = stack.pop()
            output = int(first / second)
            stack.push(output)
        elif element == '+':
            second = stack.pop()
            first = stack.pop()
            output = first + second
            stack.push(output)
        elif element == '-':
            second = stack.pop()
            first = stack.pop()
            output = first - second
            stack.push(output)
        else:
            stack.push(int(element))
    return stack.pop()



def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")
test_case_1 = [["3", "1", "+", "4", "*"], 16]

test_function(test_case_1)