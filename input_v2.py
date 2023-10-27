import numpy as np

# Function that creates Identity Matrix and combines it with the matrix of constraints.
def define_A(constraints_matrix):
    A = []
    identity_matrix = np.identity(constraints_matrix.shape[0])
    for row in range(constraints_matrix.shape[0]):
        A.append(np.append(constraints_matrix[row] ,identity_matrix[row]))
    return np.array(A)

# Main input function.
def input_linear_program():
    # Input the number of variables and constraints.
    n = int(input("Enter the number of variables (n): "))
    m = int(input("Enter the number of constraints (m): "))

    # Input the coefficients of the objective function (C).
    print("Enter the coefficients of the objective function (C):")
    C = np.array([float(input(f"C[{i}]: ")) for i in range(n)])
    C = np.append(C, np.array([0 for _ in range(m)]))

    # Input the coefficients of the constraint function (A).
    print("Enter the coefficients of the constraint matrix (A):")
    A = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            A[i, j] = float(input(f"A[{i}][{j}]: "))
            
    # Complete constraint function (A).
    A = define_A(A)

    # Input the right-hand side values (b).
    print("Enter the right-hand side values (b):")
    b = np.array([float(input(f"b[{i}]: ")) for i in range(m)])

    # Input the approximation accuracy (ε).
    epsilon = float(input("Enter the approximation accuracy (ε): "))

    # Set first and second values of α:
    alpha_1 = 0.5
    alpha_2 = 0.9

    return C, A, b, epsilon, alpha_1, alpha_2

# Example usage:
C, A, b, epsilon, alpha_1, alpha_2 = input_linear_program()
print("C:", C)
print("A:", A)
print("b:", b)
print("ε:", epsilon)
print("Initial value of α:", alpha_1)
print("Second value of α:", alpha_2)
