import numpy as np


def north_west(supply, costs, demand):
    # Initialize indices for the supply (S) and demand (D) arrays
    i, j = 0, 0

    s = np.array(supply)
    d = np.array(demand)
    c = np.array(costs)

    # Get the dimensions of the cost matrix C
    row_length = len(c[0])
    column_length = len(c)

    # Initialize the total cost summation
    summ = 0

    # Initialize vectors for the initial basic feasible solution
    x0 = [[0] * row_length for _ in range(column_length)]

    # Number of items that you need to distribute between the sources and destinations
    number_remaining_items = sum(s)

    # Iterate until you distributed all the items
    while number_remaining_items > 0:
        # Find the minimum of the supply and demand at the current cell
        mn = min(s[i], d[j])

        summ += mn * c[i][j]

        # Update vectors based on the minimum value and decrease remaining items
        if i < column_length and s[i] == mn:
            number_remaining_items -= mn
            x0[i][j] = mn
            d[j] -= s[i]
            s[i] = 0
            i += 1
        elif j < row_length and d[j] == mn:
            number_remaining_items -= mn
            x0[i][j] = mn
            s[i] -= d[j]
            d[j] = 0
            j += 1

    print("==================")
    print("North-West:")

    # Print the vectors of the initial basic feasible solution and total cost
    for i, vector in enumerate(x0):
        print(i + 1, "vector of initial basic solution:", vector)

    print("Total Cost:", summ)
