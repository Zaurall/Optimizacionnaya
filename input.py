import numpy as np


# Function that reads a vector of coefficients.
def read_vector():
    return np.array([float(x) for x in input().split(' ')])


# Function that transforms a few vectors into a single matrix.
def create_main_matrix(z_row, vectors, sol_vector):
    # Create an array in which we will store all the vectors.
    matrix = []
    complete_matrix = []

    # Add basic coefficients to z-row.
    z_row = np.append(z_row, [0 for _ in range(len(vectors))]) * -1

    # Put the z-row inside the matrix.
    matrix.append(z_row)

    # Put vectors inside an array.
    for vector in vectors:
        matrix.append(vector)

    # Add the solution variable to each vector in the matrix.
    sol_vector = np.append([0], sol_vector)
    for i in range(len(matrix)):
        complete_matrix.append(np.append(matrix[i], sol_vector[i]))

    # Transform array into single matrix.
    return np.array(complete_matrix)


# Function that creates a vector of variables.
def create_var_vector(length_of_coef, number_of_basic_var):
    # Create an array in which we will store all the variables.
    vector_of_variables = []

    # Add main variables to the array.
    for i in range(1, length_of_coef + 1):
        vector_of_variables.append('x' + str(i))

    # Add basic variables to the array.
    for i in range(1, number_of_basic_var + 1):
        vector_of_variables.append('s' + str(i))

    # Transform an array into vector.
    return np.array(vector_of_variables)


# Function that creates a vector of basic variables.
def create_basic_vector(number_of_basic_var):
    # Create an array in which we will store all the basic variables.
    vector_of_basic_var = []

    # Add the 'z' variable to the array.
    vector_of_basic_var.append('z')

    # Add basic variables to the array.
    for i in range(1, number_of_basic_var + 1):
        vector_of_basic_var.append('s' + str(i))

    # Transform an array into vector.
    return np.array(vector_of_basic_var)


# Function that adds additional basic coefficients to the matrix of vectors.
def add_basic_coef(vectors):
    # Create Identity matrix.
    identity_matrix = np.identity(len(vectors))
    # Add additional coefficients to the 2-D array via cycles.
    for i in range(len(vectors)):
        vectors[i] = np.append(vectors[i], identity_matrix[i])

    # Transform vectors into matrix.
    return vectors


# Function that creates constraint matrix.
def create_constraint_matrix(length):
    # Create a list of constraint vectors.
    constr_vec = []

    # Add vectrots to the list:
    for i in range(length):
        constr_vec.append(read_vector())

    # Add basic coefficients to the list.
    constr_vec = add_basic_coef(constr_vec)

    # Return the result (array of ndarrays).
    return constr_vec
