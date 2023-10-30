import math
#import iteration as iteration_simplex
import input_v2 as interior_point


def main():
    print('Please, enter the \'z\'-row:')
    c = interior_point.read_vector()
    print('Please, enter the constraint matrix:')
    constr_matr = interior_point.create_constraint_matrix(3)
    print('Please, enter the solution vector:')
    sol_vec = interior_point.read_vector()
    print('Please, enter the accuracy:')
    accuracy = float(input())

    matrix = interior_point.create_main_matrix(c, constr_matr, sol_vec)
    epsilon = 0

    while accuracy < 1:
        accuracy *= 10
        epsilon += 1

    # Check for all cases when the method is not applicable.

    # case 1
    for i in range(len(constr_matr)):
        count = 0
        for j in range(len(constr_matr[i])):
            if constr_matr[i][j] == 0:
                count += 1
        if count == len(constr_matr[i]) and sol_vec[i] != 0:
            print("The method is not applicable!")
            exit(0)

    # case 2
    for i in sol_vec:
        if i < 0:
            print("The method is not applicable!")
            exit(0)

    # case 3
    if all([x for x in c]) <= 0:
        print("The method is not applicable!")
        exit(0)

    basic_vector = interior_point.create_basic_vector(3)
    var_vector = interior_point.create_var_vector(3, len(constr_matr))

    init_var = var_vector[0:3]

    while iteration_simplex.iteration(matrix, basic_vector, var_vector):
        continue


    print("Optimal Solution:")
    for i in init_var:
        # Bool variable for determining whether the decision variable is 0 or influences the optimal solution.
        flag = True
        for j in range(0, len(basic_vector)):
            if i == basic_vector[j]:
                flag = False
                print(i, matrix[j][-1])
        if flag:
            print(i, 0)
    print("Optimal Value:", math.floor(matrix[0][-1] * 10 ** epsilon) / 10 ** epsilon)


if __name__ == "__main__":
    main()
