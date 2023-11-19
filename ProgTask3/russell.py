import numpy as np


def russell(s, c, d):
    # Define the m and n as the size of the matrix
    m, n = len(s), len(d)

    # Initialize supply, demand, and costs matrices
    supply = np.array(s)
    demand = np.array(d)
    costs = np.array(c)

    # Here we are using an alternative method to obtain a non-zero initial solution
    x0 = np.zeros((m, n), dtype=int)  # Set the initial solution matrix with all 0's
    penalties = np.zeros((m, n), dtype=int)

    # Continue with the main iteration until all supplies or demands are satisfied
    while np.any(supply > 0) and np.any(demand > 0):
        vi = np.max(costs, axis=0)
        ui = np.max(costs, axis=1)

        # Calculate the penalty values for each cell
        for i in range(m):
            for j in range(n):
                if costs[i][j] == 0:
                    penalties[i][j] = 0
                else:
                    penalties[i][j] = costs[i][j] - ui[i] - vi[j]

        # Find the indices of the minimum penalty value
        # If the penalty values are equal we choose the first found value
        min_penalty_index = np.unravel_index(np.argmin(penalties), penalties.shape)

        # Determine the quantity to be allocated
        allocation_quantity = min(supply[min_penalty_index[0]], demand[min_penalty_index[1]])

        # Allocate the quantity to the selected cell
        x0[min_penalty_index[0], min_penalty_index[1]] += allocation_quantity

        # Update supply and demand
        supply[min_penalty_index[0]] -= allocation_quantity
        demand[min_penalty_index[1]] -= allocation_quantity

        if supply[min_penalty_index[0]] == 0:
            costs[min_penalty_index[0]][min_penalty_index[1]] = 0

        elif demand[min_penalty_index[1]] == 0:
            costs[min_penalty_index[0]][min_penalty_index[1]] = 0

    # Check if the solution is feasible
    if not np.allclose(np.sum(x0, axis=1), s) or not np.allclose(np.sum(x0, axis=0), d):
        return None, "The method is not applicable!"

    print("==================")
    print("Russell:")

    # Print the vectors of the initial basic feasible solution and total cost
    for i, vector in enumerate(x0):
        print(i + 1, "vector of initial basic solution:", list(vector))

    summ = np.sum(x0 * c)

    print("Total Cost:", summ)
