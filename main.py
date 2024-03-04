def check_saddle_point(matr):
    len_matr = len(matr)
    len_column = len(matr[0])
    alpha = max([min(part) for part in matr])
    temp_list = list()
    for i in range(len_column):
        temp_list.append(max([matr[j][i] for j in range(len_matr)]))
    betta = min(temp_list)
    return alpha == betta


def crossing_out_rows():
    pass


def crossing_out_columns():
    pass


# def crossing_out(matr):
#     temp_list = list()
#     len_matr = len(matr)
#     len_column = len(matr[0])
#     matr_copy = matr.copy()
# 
#     for i in range(len(matr) - 1):
#         for j in range(i, len(matr)):
#             temp1 = matr[i]
#             temp2 = matr[j]
#             if all([x <= y for x, y in zip(temp1, temp2)]):
#                 matr_copy.remove(matr[i])
#             elif all([x >= y for x, y in zip(temp1, temp2)]):
#                 matr_copy.remove(matr[j])
#     return matr_copy


if __name__ == '__main__':

    # 1 2 3
    # 4 7 9
    # 1 2 3

    # 4 -2 5 1 2 7
    # 1 2 4 3 0 10
    # 3 5 6 7 1 9
    # 1 2 4 3 0 10
    # 2 1 3 6 5 4

    matrix = list()
    k = int(input("Введите количество строк в матрице: "))
    for i in range(k):
        matrix.append(list(map(int, input().split())))
    if not check_saddle_point(matrix):
        print(crossing_out(matrix))
    else:
        print("Седловая точка")
