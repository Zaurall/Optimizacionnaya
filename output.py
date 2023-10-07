import math
import iteration as iteration_simplex
import input as input_simplex


def main():
    print('Please, enter the \'z\'-row:')
    c = input_simplex.read_vector()
    print('Please, enter the constraint matrix:')
    constr_matr = input_simplex.create_constraint_matrix(3)
    print('Please, enter the solution vector:')
    sol_vec = input_simplex.read_vector()

    matrix = input_simplex.create_main_matrix(c, constr_matr, sol_vec)

    # Check for all cases when the method is not applicable.

    # case 1
    for i in range(len(constr_matr)):
        count = 0
        for j in range(len(constr_matr[i])):
            if constr_matr[i][j] == 0:
                count += 1
        if count == len(constr_matr[i]) and sol_vec[i] != 0:
            print("The method is not applicable!1")
            exit(0)

    # case 2
    for i in sol_vec:
        if i < 0:
            print("The method is not applicable!2")
            exit(0)

    # case 3
    if all([x for x in c]) <= 0:
        print("The method is not applicable!3")
        exit(0)

    basic_vector = input_simplex.create_basic_vector(3)
    var_vector = input_simplex.create_var_vector(3, len(constr_matr))

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
    print("Optimal Value:", matrix[0][-1])


if __name__ == "__main__":
    main()
