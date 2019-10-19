import copy
def permute(mylist):
    perm = []
    if len(mylist) == 0:
        perm.append([])
    else:
        first_elem = mylist[0]
        after_first = slice(1, None)
        sub_permutes = permute(mylist[after_first])
        for p in sub_permutes:
            for j in range(0, len(p)+1):
                r = copy.deepcopy(p)
                r.insert(j, first_elem)
                perm.append(r)
    return perm


def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.

    Note that the ordering of the list is not important.

    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list

    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input

    o.sort()
    e.sort()
    return o == e


# print("Pass" if (check_output(permute([]), [[]])) else "Fail")
# print("Pass" if (check_output(permute([0]), [[0]])) else "Fail")
# print("Pass" if (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print("Pass" if (
    check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")
