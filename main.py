def check_saddle_point(matr):
    len_matr = len(matr)
    len_column = len(matr[0])
    alpha = max([min(part) for part in matr])
    temp_list = list()
    for i in range(len_column):
        temp_list.append(max([matr[j][i] for j in range(len_matr)]))
    betta = min(temp_list)
    return alpha == betta


def crossing_out_rows(mtx):
    if len(mtx) >= 2:
        for row in range(len(mtx) - 1):
            temp1 = mtx[row]
            for row2 in range(row + 1, len(mtx)):
                temp2 = mtx[row2]
                if all([x <= y for x, y in zip(temp1, temp2)]):
                    mtx.pop(row)
                    return crossing_out_rows(mtx)
                elif all([x >= y for x, y in zip(temp1, temp2)]):
                    mtx.pop(row2)
                    return crossing_out_rows(mtx)

        return mtx


def crossing_out_columns(mtx):
    if len(mtx) >= 2:
        for elem in range(len(mtx[0]) - 1):
            temp_arr = [x[elem] for x in mtx]
            for elem2 in range(elem + 1, len(mtx[0])):
                temp_arr2 = [x[elem2] for x in mtx]
                if all([x <= y for x, y in zip(temp_arr, temp_arr2)]):
                    for i in range(len(mtx)):
                        mtx[i].pop(elem2)
                    return crossing_out_columns(mtx)
                elif all([x >= y for x, y in zip(temp_arr, temp_arr2)]):
                    for j in range(len(mtx)):
                        mtx[j].pop(elem)
                    return crossing_out_columns(mtx)

    return mtx


if __name__ == '__main__':

    # 4 -2 5 1 2 7
    # 1 2 4 3 0 10
    # 3 5 6 7 1 9
    # 1 2 4 3 0 10
    # 2 1 3 6 5 4

    matrix = list()
    k = int(input("Введите количество строк в матрице: "))
    for _ in range(k):
        matrix.append(list(map(int, input().split())))
    if not check_saddle_point(matrix):
        cross_row = crossing_out_rows(matrix)
        cross_column = crossing_out_columns(matrix)
        while cross_row != cross_column:
            cross_row = crossing_out_rows(matrix)
            cross_column = crossing_out_columns(matrix)
        print(matrix)

    else:
        print("Седловая точка")
