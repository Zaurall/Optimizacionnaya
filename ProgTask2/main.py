import math
import iteration as iteration_interior_point
import numpy as np
from numpy import linalg
from input_v2 import C, A, b, epsilon, alpha_1, alpha_2, number_of_var
from trial import make_trial


def main():
    # Check for all cases when the method is not applicable.
    # case 1
    for i in b:
        if i < 0:
            print("The method is not applicable!")
            exit(0)

    # case 2

    is_already_optimized = True
    for x in C:
        if(x > 0):
            is_already_optimized = False
    if(is_already_optimized == True):
        print("The method is not applicable!")

    x = make_trial(A, b)
    x_old_alpha1 = np.asarray(x)
    is_solved_alpha1 = False
    x_old_alpha2 = np.asarray(x)
    is_solved_alpha2 = False
    # Iterations Counter
    iter_counter = 0
    # Iterate until convergence
    while True:

        # Set up matrices D and I for the current iteration
        zero_matrix_alpha1 = np.zeros((x_old_alpha1.size, x_old_alpha1.size))
        D_alpha1 = np.diag(x_old_alpha1) + zero_matrix_alpha1
        I_alpha1 = np.identity(x_old_alpha1.size)

        # Set up matrices D and I for the current iteration
        zero_matrix_alpha2 = np.zeros((x_old_alpha2.size, x_old_alpha2.size))
        D_alpha2 = np.diag(x_old_alpha2) + zero_matrix_alpha2
        I_alpha2 = np.identity(x_old_alpha2.size)

        # Perform iterations using different alpha values
        if(is_solved_alpha1 == False):
            x_new_alpha1 = iteration_interior_point.count_iteration(D_alpha1, I_alpha1, alpha_1, x_old_alpha1)
        if(is_solved_alpha2 == False):
            x_new_alpha2 = iteration_interior_point.count_iteration(D_alpha2, I_alpha2, alpha_2, x_old_alpha2)

        # Check for convergence
        if linalg.norm(np.subtract(x_new_alpha1, x_old_alpha1), ord=2) < epsilon:
            is_solved_alpha1 = True
        else:
            x_old_alpha1 = x_new_alpha1

        if linalg.norm(np.subtract(x_new_alpha2, x_old_alpha2), ord=2) < epsilon:
            is_solved_alpha2 = True
        else:
            x_old_alpha2 = x_new_alpha2
        
        if(iter_counter >= 10000): # If the number of iterations is tense to infinity, problem have no solution 
            print("The problem does not have solution!\n")
            break
        else:
            iter_counter += 1
    # Calculating maximum value of z 
    z_alpha1 = np.dot(x_new_alpha1, C)
    z_alpha2 = np.dot(x_new_alpha2, C)
    # Print the solution
    print("Maximum value of z if alpha = 0.5: ", z_alpha1)
    print("A vector of decision variables - X*, using alpha = 0.5: ", x_new_alpha1[:number_of_var])
    print("Maximum value of z if alpha = 0.9: ", z_alpha2)
    print("A vector of decision variables - X*, using alpha = 0.9: ", x_new_alpha2[:number_of_var])

if __name__ == "__main__":
    main()
