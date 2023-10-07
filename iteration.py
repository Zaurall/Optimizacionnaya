import numpy as np


# Checks if the model has more optimal solutions
def has_more_optimal_solution(matrix: np.array):
    z_row = matrix[0]
    z_row = np.delete(z_row, np.shape(matrix)[1] - 1)
    pivot = np.min(z_row)
    return pivot < 0


# Returns the index of minimum negative z-row element
def get_pivot_index(matrix: np.array):
    t = np.where(matrix[0] == np.min(matrix[0][:-1]))[0][0]
    return t


# Returns the index of row(variable) to replace
def row_index_for_replace(matrix: np.array, pivot_idx):
    dimensions = np.shape(matrix)
    minimum_positive = float("inf")
    idx_for_replacement = 0
    for i in range(1, dimensions[0]):
        if matrix[i][pivot_idx] != 0:
            temp_ratio = matrix[i][dimensions[1] - 1] / matrix[i][pivot_idx]
            if 0 < temp_ratio < minimum_positive:
                minimum_positive = temp_ratio
                idx_for_replacement = i

    return idx_for_replacement


def change_pivot_row(matrix: np.array, pivot_idx, row_idx):
    matrix[row_idx] = np.divide(matrix[row_idx], matrix[row_idx][pivot_idx])


def change_other_rows(matrix: np.array, pivot_idx, row_idx):
    dimensions = matrix.shape
    for i in range(dimensions[0]):
        if i != row_idx:
            matrix[i] = np.subtract(matrix[i], np.multiply(matrix[row_idx], matrix[i][pivot_idx]))


# Function that calculates the one iteration of Simplex method.
# Returns True if iteration was completed and False if optimal solution already founded
def iteration(matrix: np.array, basic_variables: np.array, all_variables: np.array):
    if has_more_optimal_solution(matrix):
        pivot_index = get_pivot_index(matrix)
        row_index = row_index_for_replace(matrix, pivot_index)
        basic_variables[row_index] = all_variables[pivot_index]
        change_pivot_row(matrix, pivot_index, row_index)
        change_other_rows(matrix, pivot_index, row_index)
        return True
    return False


def test():
    basic = np.array(["z", "s1", "s2", "s3"])
    all_vars = np.array(["x1", "x2", "x3", "s1", "s2", "s3"])
    matrix = np.array([[-9.0, -10., -16., 0., 0., 0., 0.],
                       [18., 15., 12., 1., 0., 0., 360.],
                       [6., 4., 8., 0., 1., 0., 192.],
                       [5., 3., 3., 0., 0., 1., 180.]])
    while iteration(matrix, basic, all_vars):
        continue
    print(basic)
    print(matrix)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
