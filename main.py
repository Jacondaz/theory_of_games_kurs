def check_saddle_point(matr):
    len_matr = len(matr)
    len_column = len(matr[0])
    alpha = max([min(part) for part in matr])
    temp_list = list()
    for i in range(len_column):
        temp_list.append(max([matr[j][i] for j in range(len_matr)]))
    betta = min(temp_list)

    if alpha == betta:
        max_index, _ = max(enumerate([min(part) for part in matr]), key=lambda pair: pair[1])
        min_index, _ = min(enumerate(temp_list), key=lambda pair: pair[1])
        p_list = [0 for _ in range(len(matr))]
        q_list = [0 for _ in range(len(matr[0]))]
        p_list[max_index] = 1
        q_list[min_index] = 1
        return p_list, q_list, alpha
    else:
        return False

# 9 5 6 7
# 1 4 3 8
# 6 3 2 -4


def crossing_out_rows(mtx, flag=None):

    if len(mtx) >= 2:
        for row in range(len(mtx) - 1):
            temp1 = mtx[row]
            for row2 in range(row + 1, len(mtx)):
                temp2 = mtx[row2]
                if all([x <= y for x, y in zip(temp1, temp2)]):
                    mtx.pop(row)
                    return crossing_out_rows(mtx, flag=True)
                elif all([x >= y for x, y in zip(temp1, temp2)]):
                    mtx.pop(row2)
                    return crossing_out_rows(mtx, flag=True)

    if flag:
        return crossing_out_columns(mtx)
    else:
        return mtx


def crossing_out_columns(mtx, flag=None):

    if len(mtx) >= 2:
        for elem in range(len(mtx[0]) - 1):
            temp_arr = [x[elem] for x in mtx]
            for elem2 in range(elem + 1, len(mtx[0])):
                temp_arr2 = [x[elem2] for x in mtx]
                if all([x <= y for x, y in zip(temp_arr, temp_arr2)]):
                    for i in range(len(mtx)):
                        mtx[i].pop(elem2)
                    return crossing_out_columns(mtx, flag=True)
                elif all([x >= y for x, y in zip(temp_arr, temp_arr2)]):
                    for j in range(len(mtx)):
                        mtx[j].pop(elem)
                    return crossing_out_columns(mtx, flag=True)

    if flag:
        return crossing_out_rows(mtx)
    else:
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

    saddle_point = check_saddle_point(matrix)
    if isinstance(saddle_point, bool):
        matrix = crossing_out_rows(matrix)
        print(matrix)
    else:
        p, q, saddle = saddle_point
        print(f'Седловая точка: {saddle}')
        print(f'Стратегия 1 игрока: p = {p}')
        print(f'Стратегия 2 игрока: q = {q}')
