# LinkedList Node class for your reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# my solution
def skip_i_delete_j(head, i, j):
    if head is None:
        return None
    while head:
        icount = 0
        jcount = 0
        while icount != i:
            r_next_node = head.next
            head = head.next
            if head.next is None:
                break
            icount += 1
        while jcount != j:
            d_next_node = head.next
            head = head.next
            if head is None:
                break
            jcount += 1
        r_next_node.next = d_next_node
        head = d_next_node
    return head


# courses solution
def skip_i_delete_j(head, i, j):
    if i == 0:
        return None

    if head is None or j < 0 or i < 0:
        return head

    current = head
    previous = None
    while current:
        # skip (i - 1) nodes
        for _ in range(i - 1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next

        # delete next j nodes
        for _ in range(j):
            if current is None:
                break
            next_node = current.next
            current = next_node
        previous.next = current
    return head


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr) == 0:
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


def test_function(test_case):
    head = test_case[0]
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]

    temp = skip_i_delete_j(head, i, j)
    index = 0
    try:
        while temp is not None:
            if temp.data != solution[index]:
                print("Fail")
                return
            index += 1
            temp = temp.next
        print("Pass")
    except Exception as e:
        print("Fail")


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 2
head = create_linked_list(arr)
solution = [1, 2, 5, 6, 9, 10]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 3
head = create_linked_list(arr)
solution = [1, 2, 6, 7, 11, 12]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5]
i = 2
j = 4
head = create_linked_list(arr)
solution = [1, 2]
test_case = [head, i, j, solution]
test_function(test_case)
