def deep_reverse(element):
    lo = 0
    hi = len(element) - 1
    while lo < hi:
        temp = element[lo]
        element[lo] = element[hi]
        element[hi] = temp
        lo += 1
        hi -= 1
    for item in element:
        if isinstance(item, list):
            deep_reverse(item)
    return element


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")

arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)