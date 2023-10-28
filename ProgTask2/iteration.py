# Import necessary libraries and modules
import numpy as np
from numpy import linalg
from input import C, A, b, epsilon, alpha_1, alpha_2
from trial import make_trial


# Function to perform one iteration of the interior point algorithm
def count_iteration(D, I, alpha):
    # Calculate values required for the iteration
    # Calculating matrix A-tilda
    A1 = np.dot(A, D)
    # Calculating vector c-tilda
    c1 = np.dot(D, C)
    # Calculating matrix A-tilda-transpose
    A1_t = A1.transpose()
    # Calculating matrix A-tilda * A-tilda-transpose
    A1_A1_t = np.dot(A1, A1_t)
    # Check if the matrix is invertible
    num_rows, num_cols = A1_A1_t.shape
    if num_rows == 1:
        # Calculating inverse of number (A-tilda * A-tilda-transpose)
        A1_A1_t_inverse = 1 / A1_A1_t
    elif num_rows != 1 and linalg.det(A1_A1_t) == 0:
        print("Solution doesn't exist")
        exit(0)
    else:
        # Calculating inverse matrix (A-tilda * A-tilda-transpose)
        A1_A1_t_inverse = linalg.inv(A1_A1_t)

    # Calculate projection matrix P and update x value
    P = I - np.dot(np.dot(A1_t, A1_A1_t_inverse), A1)
    # Calculating projected gradient
    cp = np.dot(P, c1)
    # Define v as the absolute value of the negative component of cp having the largest absolute value
    v = abs(min(i for i in cp))
    # Create a vector of ones
    ones = np.ones(x_old.size)
    # Calculating vector x-tilda
    x_tilda = np.add(ones, (alpha / v) * cp)
    # Calculating new x value
    x_new = np.dot(D, x_tilda)
    return x_new

# Generate an initial trial solution
x = make_trial(A, b)
x_old = np.asarray(x)
index_of_iteration = 1

# Iterate until convergence
while True:
    print("Iteration:", index_of_iteration)
    index_of_iteration += 1

    # Set up matrices D and I for the current iteration
    zero_matrix = np.zeros((x_old.size, x_old.size))
    D = np.diag(x_old) + zero_matrix
    I = np.identity(x_old.size)

    # Perform iterations using different alpha values
    x_new_alpha1 = count_iteration(D, I, alpha_1)
    x_new_alpha2 = count_iteration(D, I, alpha_2)

    # Print the results for each alpha value
    print("X value, using alpha = 0.5: ", x_new_alpha1)
    print("X value, using alpha = 0.9: ", x_new_alpha2)

    # Check for convergence
    if linalg.norm(np.subtract(x_new_alpha1, x_old), ord=2) < epsilon:
        break
    else:
        x_old = x_new_alpha1

# Calculating maximum value of z
z = np.dot(x_old, C)
print("Maximum value of z: ", z)
