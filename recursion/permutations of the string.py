import copy
def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    perm = []
    if len(string) == 0:
        perm.append([])
    else:
        mylist = list(string)
        first_alpha = mylist[0]
        after_first = slice(1,None)
        sub = permutations(mylist[after_first])
        for p in sub:
            for i in range(len(p)+1):
                r = copy.deepcopy(list(p))
                r.insert(i, first_alpha)
                perm.append(''.join(r))
    print(perm)
    return perm


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)