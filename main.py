import numpy as np


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

def solution_p(matr, ind=None):
    if ind is None:
        number1 = matr[0]
        number2 = matr[1]

        size = np.arange(0, 1.001, 0.001)
        total = list()

        for coord in size:
            temp = list()
            for i in range(len(number1)):
                temp.append((i, round(number1[i] * coord + number2[i] * (1 - coord), 3)))
            total.append(min(temp, key=lambda x: x[1]))
        max_index = total.index(max(total, key=lambda x: x[1]))
        set_of_index = list({total[max_index][0], total[max_index - 1][0], total[max_index + 1][0]})
        return [max_index * 0.001, 1 - max_index * 0.001], solution_q(matr, set_of_index), max(total,
                                                                                               key=lambda x: x[1])[1]
    else:
        ...


# 1 2
# 3 4
# 5 6

# 9 5 6 7
# 1 4 3 8

def solution_q(matr, inx=None):
    if inx is None:

        number1 = [x[0] for x in matr]
        number2 = [x[1] for x in matr]

        size = np.arange(0, 1.001, 0.001)
        total = list()

        for coord in size:
            temp = list()
            for i in range(len(number1)):
                temp.append(round(number1[i] * coord + number2[i] * (1 - coord), 3))
            total.append(max(temp))
    else:

        number1 = [matr[0][ind] for ind in inx]
        number2 = [matr[1][ind] for ind in inx]

        size = np.arange(0, 1.001, 0.001)
        total = list()
        results = [0 for _ in range(len(matr[0]))]

        for coord in size:
            temp = list()
            for i in range(len(number1) - 1):
                temp.append((i, round(number1[i] * coord + number1[i + 1] * (1 - coord), 3)))
                temp.append((i, round(number2[i] * coord + number2[i + 1] * (1 - coord), 3)))
            total.append(max(temp, key=lambda x: x[1]))

        index = total.index(min(total, key=lambda x: x[1])) * 0.001
        sol = [index, 1 - index]
        for t in inx:
            results[t] = sol[0]
            sol.pop(0)

        return results


def crossing_out_rows(mtx):
    if len(mtx) >= 2:
        for row in range(len(mtx) - 1):
            temp1 = mtx[row]
            for row2 in range(row + 1, len(mtx)):
                temp2 = mtx[row2]
                if all([x <= y for x, y in zip(temp1, temp2)]):
                    mtx.pop(row)
                    return crossing_out_columns(mtx)
                elif all([x >= y for x, y in zip(temp1, temp2)]):
                    mtx.pop(row2)
                    return crossing_out_columns(mtx)

    return crossing_out_columns(mtx)


def crossing_out_columns(mtx):
    if len(mtx) >= 2:
        for elem in range(len(mtx[0]) - 1):
            temp_arr = [x[elem] for x in mtx]
            for elem2 in range(elem + 1, len(mtx[0])):
                temp_arr2 = [x[elem2] for x in mtx]
                if all([x <= y for x, y in zip(temp_arr, temp_arr2)]):
                    for i in range(len(mtx)):
                        mtx[i].pop(elem2)
                    return crossing_out_rows(mtx)
                elif all([x >= y for x, y in zip(temp_arr, temp_arr2)]):
                    for j in range(len(mtx)):
                        mtx[j].pop(elem)
                    return crossing_out_rows(mtx)

    return mtx


if __name__ == '__main__':

    matrix = list()
    k = int(input("Введите количество строк в матрице: "))
    for _ in range(k):
        matrix.append(list(map(int, input().split())))

    saddle_point = check_saddle_point(matrix)
    if isinstance(saddle_point, bool):
        matrix = crossing_out_rows(matrix)
        if len(matrix) == 2:
            result_p, result_q, weight = solution_p(matrix)
            print(f'Стратегия 1 игрока: p = {result_p}')
            print(f'Стратегия 2 игрока: q = {result_q}')
            print(f'Стоимость игры: V = {weight}')
        elif len(matrix[0]) == 2:
            result_q, result_p, weight = solution_q(matrix)
        else:
            print("Матрица не соответствует виду 2xM или Nx2")
    else:
        p, q, saddle = saddle_point
        print(f'Седловая точка: {saddle}')
        print(f'Стратегия 1 игрока: p = {p}')
        print(f'Стратегия 2 игрока: q = {q}')
