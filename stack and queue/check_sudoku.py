def check_sudoku(list):
    standard = [n for n in range(1, len(list)+1)]
    for order in range(len(list)):
        raw = []
        for item in list:
            raw.append(item[order])
        raw.sort()
        if raw != standard:
            return False
    for item in list:
        item.sort()
        if item != standard:
            return False
    return True


correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]
wrong2 = [[1, 2, 3, 4], [2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 1, 2]]
正确 = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
print(check_sudoku(correct))
print(check_sudoku(wrong2))
print(check_sudoku(正确))
