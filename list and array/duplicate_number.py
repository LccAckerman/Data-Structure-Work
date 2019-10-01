def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]

    ex:  len = 5, 0~3, 因為重複一個, 少1
        [0,1,2,3,2]

    return - the number that is duplicate in the arr
    """
    maxnum = len(arr) - 2
    mylist = [x for x in range(0,maxnum)]
    for item in arr:
        if item in mylist:
            mylist.remove(item)
        else:
            return item

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [0, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)