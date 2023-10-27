import numpy as np


# The idea of setting trial solution is to set all x's firstly to 1 and find compatible slacks variables.
# If one or several slacks are zero all x's would be 0.1, in next 0.01 and so on until all vars would be >=0
# matrix - constraint matrix, b - solution vector, previous - previous unsuccessful solution
def make_trial(matrix: np.array, b: np.array, previous=None):
    if previous is None:
        previous = []
    x = []
    if len(previous) == 0:
        for i in range(matrix.shape[1] - (matrix.shape[0])):
            x.append(1)
    else:
        for i in range(matrix.shape[1] - (matrix.shape[0])):
            x.append(previous[i] / 10)
    for i in range(len(b)):
        x.append(b[i])
        x[-1] -= np.dot(x[:-1], matrix[i][:matrix.shape[1] - (matrix.shape[0])+i])
    if np.min(x) <= 0:
        return make_trial(matrix, b, previous=x)
    return x


def test():
    basic = np.array(["z", "s1", "s2", "s3"])
    all_vars = np.array(["x1", "x2", "x3", "s1", "s2", "s3"])
    matrix = np.array([[18., 15., 12., 1., 0., 0.],
                       [6., 4., 8., 0., 1., 0.],
                       [5., 3., 3., 0., 0., 1.]])
    sol = [360., 192., 180.]
    print(make_trial(matrix, sol))


if __name__ == '__main__':
    test()
