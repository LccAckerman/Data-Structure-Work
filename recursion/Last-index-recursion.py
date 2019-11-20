"""Problem statement
Given an array arr and a target element target, find the last index of occurence of target in arr using recursion. If target is not present in arr, return -1.

For example:

For arr = [1, 2, 5, 5, 4] and target = 5, output = 3

For arr = [1, 2, 5, 5, 4] and target = 7, output = -1"""

"""my solution ,i think it will be easier without using recursion,,,
but since it is the regulation, i will try another way"""


def last_index1(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    TODO: complete this method to find the last index of target in arr
    """
    lastidx = None
    for index,item in enumerate(arr):
        if item == target:
            lastidx = index
    return lastidx

def last_index(arr, target):
    return last_index_help(arr, target, len(arr)-1)
def last_index_help(arr, target, index):
    if index < 0: # show that we can't find the target
        return -1
    if arr[index] == target: # from back to front wo have got it
        return index
    return last_index_help(arr, target, index - 1)

def test_function(test_case):
    arr = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = last_index(arr, target)
    if output == solution:
        print("Pass")
    else:
        print("False")

arr = [1, 2, 5, 5, 4]
target = 5
solution = 3

test_case = [arr, target, solution]
test_function(test_case)