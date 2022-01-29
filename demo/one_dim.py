import random
import numpy as np

inverse_matrix = np.linalg.pinv(np.array([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 1]]))


def getMatrix(a, b, c, d):
    matrix = np.array([a, b, c, d]).reshape(4, 1)
    res = inverse_matrix @ matrix
    print(res)
    return res[0, 0], res[1, 0], res[2, 0], res[3, 0]


def create_dim(dim1, dim2):
    min_stop = min(dim1, dim2) - 2
    max_stop = max(dim1, dim2) - 2
    col_arr = [1.] * dim1  # 列存储数组
    row_arr = [1.] * dim2  # 行存储数组
    mat_arr = np.linspace(0, 0, dim1 * dim2)
    rtn_mat = mat_arr.reshape(dim1, dim2)

    def create_random(i):
        print(rtn_mat)
        print(col_arr)
        print(row_arr)
        if i < min_stop:
            rand = random.uniform(0, min(row_arr[i], col_arr[i]))
            rtn_mat[i, i] = rand
            row_arr[i] = row_arr[i] - rand
            col_arr[i] = col_arr[i] - rand
            for j in range(i + 1, dim2-1):
                rand = random.uniform(0, min(col_arr[i], row_arr[j]))
                rtn_mat[i, j] = rand
                row_arr[j] = row_arr[j] - rand
                col_arr[i] = col_arr[i] - rand
            for j in range(i + 1, dim1-1):
                rand = random.uniform(0, min(row_arr[i], col_arr[j]))
                rtn_mat[j, i] = rand
                row_arr[i] = row_arr[i] - rand
                col_arr[j] = col_arr[j] - rand
            rtn_mat[dim1 - 1, i] = row_arr[i]
            rtn_mat[i, dim2 - 1] = col_arr[i]
            create_random(i + 1)
        else:
            if dim1 > dim2:
                for j in range(i, max_stop):
                    rand = random.uniform(0, min(row_arr[i], col_arr[j]))
                    rtn_mat[j, i] = rand
                    row_arr[i] = row_arr[i] - rand
                    col_arr[j] = col_arr[j] - rand
                    rtn_mat[j, i + 1] = col_arr[j]
                x1, x2, y1, y2 = getMatrix(col_arr[max_stop], row_arr[min_stop],
                                           row_arr[min_stop + 1], col_arr[max_stop + 1])
                rtn_mat[max_stop, min_stop] = x1
                rtn_mat[max_stop, min_stop + 1] = x2
                rtn_mat[max_stop + 1, min_stop] = y1
                rtn_mat[max_stop + 1, min_stop + 1] = y2
            else:
                for j in range(i, max_stop):
                    rand = random.uniform(0, min(row_arr[j], col_arr[i]))
                    rtn_mat[i, j] = rand
                    row_arr[j] = row_arr[j] - rand
                    col_arr[i] = col_arr[i] - rand
                    rtn_mat[i + 1, j] = row_arr[j]
                x1, x2, y1, y2 = getMatrix(col_arr[min_stop], row_arr[max_stop],
                                           row_arr[max_stop + 1], col_arr[min_stop + 1])
                rtn_mat[min_stop, max_stop] = x1
                rtn_mat[min_stop, max_stop + 1] = x2
                rtn_mat[min_stop + 1, max_stop] = y1
                rtn_mat[min_stop + 1, max_stop + 1] = y2


    create_random(0)
    return rtn_mat


if __name__ == '__main__':
    mat = create_dim(5, 10)
    res = 0.
    for i in range(5):
        res = 0.
        for j in range(10):
            res += mat[i, j]
        print(res)
    for i in range(10):
        res = 0.
        for j in range(5):
            res += mat[j, i]
        print(res)
