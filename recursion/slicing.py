def sum_array_recursive_pass_slicing_array(array):
    if len(array) == 1:
        return array[0]
    output = sum_array_recursive_pass_slicing_array(array[1:])
    return output + array[0]

arr = [1, 2, 3, 4]
arr = [5, 2, 9, 11]
print(sum_array_recursive_pass_slicing_array(arr))
