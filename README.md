# Optimizacionnaya

## Project Description
Optimizacionnaya is a computer program designed to solve a system of linear programming using the iterative Simplex method. The program focuses on solving maximization problems.

## Problem Statement
> The project aims to maximize the objective function:
> $$ F(x_1, x_2, x_3) = 9x_1 + 10x_2 + 16x_3 $$
> subject to the following constraints:
> 1. $$ 18x_1 + 15x_2 + 12x_3 \leq 360 <= 4 (Constraint 1) $$
> 2. $$ 6x_1 + 4x_2 + 8x_3 \leq 192 (Constraint 2) $$
> 3. $$ 5x_1 + 3x_2 + 3x_3 \leq 180 (Constraint 3) $$
> 4. $$ x_1 \leq 0 (Constraint 4) $$
> 5. $$ x_2 \leq 0 (Constraint 5) $$
> 6. $$ x_3 \leq 0 (Constraint 6) $$
> The fitted degree of a polynomal can be and must be assigned by the user in the window when the program is running. For example,
> When $degree=2$, $$y = a_0+a_1x+a_2x^2$$
> When $degree=3$, $$y = a_0+a_1x+a_2x^2+a_3x^3$$
> When $degree=4$, $$y = a_0+a_1x+a_2x^2+a_3x^3+a_4x^4$$
> Be attention that the assigned term cannot be bigger than the amount ot data you give.


## Input Format
The input comprises:
- A vector of coefficients of the objective function (\(C\)).
- A matrix of coefficients of constraint functions (\(A\)).
- A vector of right-hand side numbers (\(b\)).
- The desired approximation accuracy.

## Output Format
The output includes either:
- The string "The method is not applicable!"
or
- A vector of decision variables (\(x^*\)).
- The maximum (minimum) value of the objective function.

## Badges
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

## Usage
To use Optimizacionnaya for solving linear programming problems:
1. Clone this repository.
2. Set up your environment and install dependencies (if any).
3. Run the program with the necessary input parameters.
4. Review the output for the solution.

## License
This project is licensed under the [MIT License](LICENSE).
