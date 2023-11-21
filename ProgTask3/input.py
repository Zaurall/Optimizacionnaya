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


def verify(supply, cost_matrix, demand):
    # Check if the problem is balanced
    total_supply = sum(supply)
    total_demand = sum(demand)

    if total_supply != total_demand:
        print("The problem is not balanced.")
        exit(0)

    # Check if Russell's or Vogel's Method can be applied
    num_suppliers = len(supply)
    num_consumers = len(demand)

    if num_suppliers * num_consumers != cost_matrix.size:
        print("The method is not applicable.")
        print(cost_matrix.size)
        exit(0)

    return True


# Example usage:
S, C, D = input_linear_program()
verify(S, C, D)
