def check_saddle_point(matr):
    len_matr = len(matr)
    alpha = max([min(part) for part in matr])
    betta = min([max([])])


if __name__ == '__main__':

    matrix = list()
    k = int(input("Введите количество строк в матрице: "))
    for i in range(k):
        matrix.append(list(map(int, input().split())))
    a = check_saddle_point(matrix)
    print(a)
