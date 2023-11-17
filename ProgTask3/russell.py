import numpy as np

def russells_approximation(S, C, D):
    # Check if the problem is balanced
    if sum(S) != sum(D):
        return None, "The problem is not balanced!"

    # Define the m and n as the size of the matrix
    m, n = len(S), len(D)

    # Initialize supply, demand, and costs matrices
    supply = np.array(S)
    demand = np.array(D)
    costs = np.array(C)

    # Here we are using an alternative method to obtain a non-zero initial solution
    x0 = np.zeros((m, n))  # Set the initial solution matrix with all 0's

    # Using North-West Corner Rule we create the initial solution
    # i, j = 0, 0
    # while i < m and j < n:
    #     allocation_quantity = min(supply[i], demand[j])
    #     x0[i, j] = allocation_quantity
    #     supply[i] -= allocation_quantity
    #     demand[j] -= allocation_quantity
    #     if supply[i] == 0:
    #         i += 1
    #     if demand[j] == 0:
    #         j += 1

    supply = np.array(S)
    demand = np.array(D)

    penalties = np.zeros((m, n))
    # Continue with the main iteration until all supplies or demands are satisfied
    while np.any(supply > 0) and np.any(demand > 0):
        # Calculate the penalty values for each cell

        vi = np.max(costs, axis=0)
        ui = np.max(costs, axis=1)

        # penalties = costs - np.max(costs, axis=0) - np.max(costs, axis=1)[:, np.newaxis]
        for i in range(m):
            for j in range(n):
                if costs[i][j] == 0:
                    penalties[i][j] = 0
                else:
                    penalties[i][j] = costs[i][j] - ui[i] - vi[j]
        # Find the indices of the minimum penalty value
        min_penalty_index = np.unravel_index(np.argmin(penalties), penalties.shape)

        # Determine the quantity to be allocated
        allocation_quantity = min(supply[min_penalty_index[0]], demand[min_penalty_index[1]])

        # Allocate the quantity to the selected cell
        x0[min_penalty_index[0], min_penalty_index[1]] += allocation_quantity
        # x0[min_penalty_index[0], :] += allocation_quantity

        # Update supply and demand
        supply[min_penalty_index[0]] -= allocation_quantity
        demand[min_penalty_index[1]] -= allocation_quantity

        if supply[min_penalty_index[0]] == 0:
            costs[min_penalty_index[0]][min_penalty_index[1]] = 0
            # supply = np.delete(supply, min_penalty_index[0])
            # costs = np.delete(costs, min_penalty_index[0], axis=0)

        elif demand[min_penalty_index[1]] == 0:
            costs[min_penalty_index[0]][min_penalty_index[1]] = 0
            # demand = np.delete(demand, min_penalty_index[1])
            # costs = np.delete(costs, min_penalty_index[1], axis=1)


    # Check if the solution is feasible
    # if not np.allclose(np.sum(x0, axis=1), S) or not np.allclose(np.sum(x0, axis=0), D):
    #     return None, "The method is not applicable!"

    return x0, "Success"

def print_table(S, C, D, x0, message):
    m, n = len(S), len(D)

    # Display the input parameter table
    print("\nInput Parameter Table:")
    print("Supply (S):", S)
    print("Demand (D):", D)
    print("\nCost Matrix (C):")
    for i in range(m):
        for j in range(n):
            print(C[i][j], end="\t")
        print()

    # Display the initial solution matrix
    print("\nInitial Solution Matrix (x0):")
    for i in range(m):
        for j in range(n):
            print(x0[i, j], end="\t")
        print()

    # Print the message
    print("\nMessage:", message)

S = [50, 30, 10]
D = [30, 30, 10, 20]
C = [[1, 2, 4, 1],
     [2, 3, 1, 5],
     [3, 2, 4, 4]]

result, message = russells_approximation(S, C, D)

print_table(S, C, D, result, message)
