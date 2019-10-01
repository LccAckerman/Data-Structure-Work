def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    SUM = 0
    for item in arr:
        SUM += item
        if SUM < 0:
            SUM = 0
    return SUM


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr= [1, 2, 3, -4, 6]
solution= 8 # sum of array

test_case = [arr, solution]
test_function(test_case)