import numpy as np



# Main input function.
def input_linear_program():

    # Input vector of coefficients of supply (S).
    print("Enter the vector of coefficients of supply (S) with space:")
    S = np.array([int(num_str) for num_str in input().split(' ')])


    C = []
    # Input the  matrix of coefficients of costs  (C).
    print("Enter the coefficients of the constraint matrix (C):")
    for i in range(len(S)):
        row = input(f"Enter the elements of the first row {i + 1} with space: ").split()
        row = [int(element) for element in row]
        C.append(row)
    C = np.array(C)


    # Input the vector of coefficients of demand (D).
    print("Enter the vector of coefficients of demand (D) with space:")
    D = np.array([int(num_str) for num_str in input().split()])

    return S, C, D


# Example usage:
S, C, D = input_linear_program()
