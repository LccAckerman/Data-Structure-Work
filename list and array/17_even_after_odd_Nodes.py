class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def even_after_odd(head):
    if head is None:
        return None
    even = None
    odd = None
    even_tail = None
    odd_tail = None

    while head:
        next_node = head.next
        if head.data % 2 == 0:
            if even is None:
                even = head
                even_tail = head
            else:
                even_tail.next = head
                even_tail = head
        else:
            if odd is None:
                odd = head
                odd_tail = head
            else:
                odd_tail.next = head
                odd_tail = head
        head.next = None
        head = next_node

    if odd is None:
        return even
    else:
        odd_tail.next = even
        return odd


def test_function(test_case):
    head = test_case[0]
    solution = test_case[1]

    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)
    temp = head
    index = 0
    try:
        while temp:
            if temp.data != solution[index] or temp not in node_tracker['nodes']:
                print("Fail")
                return
            temp = temp.next
            index += 1
        print("Pass")
    except Exception as e:
        print("Fail")



arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)