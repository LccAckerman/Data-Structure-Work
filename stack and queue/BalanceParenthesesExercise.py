class Stack:
    def __init__(self):
        self.arr = []

    def size(self):
        return len(self.arr)

    def push(self, data):
        return self.arr.append(data)

    def is_empty(self):
        return self.arr == []
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.arr.pop()

def equation_checker(equation):
    myList = list(equation)
    myStack = Stack()
    for item in myList:
        if item == "(":
            myStack.push(item)
        elif item == ")":
            if myStack.is_empty():
                return False
            else:
                myStack.pop()
    if myStack.is_empty():
        return True
    else:
        return False

print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")