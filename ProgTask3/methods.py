import numpy as np
from input import S, C, D


def North_West(S, C, D):
    # Initialize indices for the supply (S) and demand (D) arrays
    i, j = 0, 0

    # Get the dimensions of the cost matrix C
    row_length = len(C[0])
    column_length = len(C)

    # Initialize the total cost summation
    summ = 0

    # Iterate until either supply or demand is exhausted
    while i < column_length and j < row_length:
        # Find the minimum of the supply and demand at the current cell
        mn = min(S[i], D[j])

        # Add the cost of transportation to the total summation
        summ += mn * C[i][j]

        # Update supply and demand based on the minimum value
        if S[i] == mn:
            D[j] -= S[i]
            S[i] = 0
            i += 1
        if D[j] == mn:
            S[i] -= D[j]
            D[j] = 0
            j += 1
    # Print the total cost of transportation
    print(summ)


def Vogel(S, C, D):
    return


def Russell(S, C, D):
    return

