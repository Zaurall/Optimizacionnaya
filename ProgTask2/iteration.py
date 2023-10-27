import numpy as np
from numpy import linalg
from input import C, A, b, epsilon, alpha_1, alpha_2
from trial import make_trial




x = make_trial(A, b)
x_old = np.asarray(x)
while True:
    print("Iteration:")
    print("x_old:", x_old)
    matrix = np.zeros((x_old.size, x_old.size))

    D = np.diag(x_old) + matrix
    I = np.identity(x_old.size)
    alpha = alpha_1

    #print("A:", A)

    D_1 = linalg.inv(D)
    A1 = np.dot(A, D)  # tilda
    c_tilda = np.dot(D, C)
    #print("D_1:", D_1)
    '''print("A_tilda:", A1)
    print("c_tilda:", c_tilda)
    '''
    A1_t = A1.transpose()
    #print("A1_t:", A1_t)
    A1A1_t = np.dot(A1, A1_t)
    #print("A1A1_t:", A1A1_t)

    num_row, num_col = A1A1_t.shape
    if num_row == 1:
        A1A1_t_1 = 1 / A1A1_t
    elif num_row != 1 and linalg.det(A1A1_t) == 0:
        print("Solution doesn't exist")
        exit(0)
    else:
        A1A1_t_1 = linalg.inv(A1A1_t)
    #print("Inverse: ", A1A1_t_1)

    A2 = np.dot(A1_t, A1A1_t_1)
    A_full = np.dot(A2, A1)
    P = I - A_full
    cp = np.dot(P, c_tilda)

    #print("P:", P)
    #print("cp:", cp)

    v = abs(min(i for i in cp))

    #print("v:", v)

    ones = np.ones(x_old.size)
    #print("ones:", ones)
    temp = (alpha / v) * cp
    #print("temp:", temp)
    x_tilda = np.add(ones, temp)

    x_new = np.dot(D, x_tilda)
    print("x_new:", x_new)
    if linalg.norm(np.subtract(x_new, x_old),ord = 2) < epsilon:
        break
    else:
        x_old = x_new