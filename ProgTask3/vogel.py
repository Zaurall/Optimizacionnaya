import numpy as np
import sys


def calculate_difference(for_row: bool, c):
    difference = []
    if not for_row:
        for i in range(c.shape[1]):
            minimum = float("inf")
            second_minimum = float("inf")
            for j in range(c.shape[0]):
                minimum = min(c[j][i], minimum)
            for j in range(c.shape[0]):
                if c[j][i] < second_minimum and c[j][i] != minimum:
                    second_minimum = c[j][i]
            if second_minimum == float("inf"):
                difference.append(-float("inf"))
            else:
                difference.append(second_minimum - minimum)
    else:
        for i in range(c.shape[0]):
            minimum = float("inf")
            second_minimum = float("inf")
            for j in range(c.shape[1]):
                minimum = min(c[i][j], minimum)
            for j in range(c.shape[1]):
                if c[i][j] < second_minimum and c[i][j] != minimum:
                    second_minimum = c[i][j]
            if second_minimum == float("inf"):
                difference.append(-float("inf"))
            else:
                difference.append(second_minimum - minimum)
    return difference


def pick_cell_column(c_temp, column_difference):
    column_idx = 0
    max_el = 0
    for i in range(len(column_difference)):
        if column_difference[i] > max_el:
            max_el = column_difference[i]
            column_idx = i
    row_idx = 0
    min_el = float("inf")
    for i in range(c_temp.shape[0]):
        if c_temp[i][column_idx] < min_el:
            row_idx = i
            min_el = c_temp[i][column_idx]
    return row_idx, column_idx


def pick_cell_row(c_temp, row_difference):
    row_idx = 0
    max_el = 0
    for i in range(len(row_difference)):
        if row_difference[i] > max_el:
            max_el = row_difference[i]
            row_idx = i
    column_idx = 0
    min_el = float("inf")
    for i in range(c_temp.shape[1]):
        if c_temp[row_idx][i] < min_el:
            column_idx = i
            min_el = c_temp[row_idx][i]
    return row_idx, column_idx


def vogel(s, c, d):
    s_temp = s.copy()
    d_temp = d.copy()
    c_temp = c.copy()
    answer = list()
    for i in range(c.shape[0]):
        answer.append([])
        for j in range(c.shape[1]):
            answer[i].append(0)
    while max(s_temp) != 0 and max(d_temp) != 0:
        column_difference = calculate_difference(False, c_temp)
        row_difference = calculate_difference(True, c_temp)
        max_column_element = max(column_difference)
        max_row_element = max(row_difference)
        if max_column_element >= max_row_element:
            cell = pick_cell_column(c_temp, column_difference)
        else:
            cell = pick_cell_row(c_temp, row_difference)
        answer[cell[0]][cell[1]] = min(s_temp[cell[0]], d_temp[cell[1]])
        s_temp[cell[0]] -= answer[cell[0]][cell[1]]
        d_temp[cell[1]] -= answer[cell[0]][cell[1]]
        if s_temp[cell[0]] == 0:
            for i in range(c_temp.shape[1]):
                c_temp[cell[0]][i] = 2 ** 31 - 1
        if d_temp[cell[1]] == 0:
            for i in range(c_temp.shape[0]):
                c_temp[i][cell[1]] = 2 ** 31 - 1
    return answer


def test():
    import input
    s, c, d = input.input_linear_program()
    for i in vogel(s, c, d):
        print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
