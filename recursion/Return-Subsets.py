import copy
def subsets(arr):
    """
    :param: arr - input integer array
    Return - list of lists (two dimensional array) where each list represents a subset
    TODO: complete this method to return subsets of an array
    """
    if len(arr) == 0:
        return [[]]
    first_elem = arr[0]
    rest_elem = arr[1:]
    output = subsets(rest_elem)

    outputcopy = []
    for index in range(len(output)):
        if isinstance(output[index], list):
            tmp = copy.deepcopy(output[index])
            tmp.insert(0, first_elem)
            outputcopy.append(tmp)
            outputcopy.append(output[index])
        else:
            outputcopy = [first_elem, output[index]]
    return outputcopy

# solution supported by teacher
def subsets_solution(arr):
    return return_subsets(arr, 0)

def return_subsets(arr, index):
    if index >= len(arr):
        return [[]]

    small_output = return_subsets(arr, index + 1)

    output = list()
    # append existing subsets
    for element in small_output:
        output.append(element)

    # add current elements to existing subsets and add them to the output
    for element in small_output:
        current = list()
        current.append(arr[index])
        current.extend(element)
        output.append(current)
    return output


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = subsets(arr)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [9]
solution = [[], [9]]

test_case = [arr, solution]
test_function(test_case)