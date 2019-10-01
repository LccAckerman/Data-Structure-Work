def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    if n == 0:
        return [1]
    # 从第二行开始计算
    # 新一行append一个1占位
    #     # 每一行的第🕑n个数起等于上一行的n-1 + n
    #     # 当完成第n行的初始化输出此行数据
    current_row = [1]
    for i in range(0, n+1):
        previous_row = current_row * 1
        count = 1
        for index in range(count, len(current_row)-1):
            current_row[index] = previous_row[index-1] + previous_row[index]
        print(current_row)
        current_row.append(1)
    del current_row[-1]
    return current_row



def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")


n = 0
solution = [1]

test_case = [n, solution]
test_function(test_case)
n = 2
solution = [1, 2, 1]

test_case = [n, solution]
test_function(test_case)

n = 4
solution = [1, 4, 6, 4, 1]

test_case = [n, solution]
test_function(test_case)