import numpy as np
from input import S, C, D


def North_West(S, C, D):
    print("==================")
    print("North-West:")
    # Initialize indices for the supply (S) and demand (D) arrays
    i, j = 0, 0

    # Get the dimensions of the cost matrix C
    row_length = len(C[0])
    column_length = len(C)

    # Initialize the total cost summation
    summ = 0

    # Initialize vectors for the initial basic feasible solution
    x0 = [[0] * row_length for _ in range(column_length)]

    # Number of items that you need to distribute between the sources and destinations
    number_remaining_items = sum(S)

    # Iterate until you distributed all the items
    while number_remaining_items > 0:
        # Find the minimum of the supply and demand at the current cell
        mn = min(S[i], D[j])

        summ += mn * C[i][j]

        # Update vectors based on the minimum value and decrease remaining items
        if i < column_length and S[i] == mn:
            number_remaining_items -= mn
            x0[i][j] = mn
            D[j] -= S[i]
            S[i] = 0
            i += 1
        elif j < row_length and D[j] == mn:
            number_remaining_items -= mn
            x0[i][j] = mn
            S[i] -= D[j]
            D[j] = 0
            j += 1

    # Print the vectors of the initial basic feasible solution and total cost
    print("1 vector of initial basic solution:", x0[0])
    print("2 vector of initial basic solution:", x0[1])
    print("3 vector of initial basic solution:", x0[2])

    print("Total Cost:", summ)
