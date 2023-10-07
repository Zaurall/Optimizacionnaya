# Optimizacionnaya

## Project Description
Optimizacionnaya is a computer program designed to solve a system of linear programming using the iterative Simplex method. The program focuses on solving maximization problems.

## Example of problem

> The project aims to maximize the objective function:
> F(x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>) = 9x<sub>1</sub> + 10x<sub>2</sub> + 16x<sub>3</sub>
> subject to the following constraints:
> 1. 18x<sub>1</sub> + 15x<sub>2</sub> + 12x<sub>3</sub> ⩽ 360 (Constraint 1)
> 2. 6x<sub>1</sub> + 4x<sub>2</sub> + 8x<sub>3</sub> ⩽ 192 (Constraint 2)
> 3. 5x<sub>1</sub> + 3x<sub>2</sub> + 3x<sub>3</sub> ⩽ 180 (Constraint 3)
> 4. x<sub>1</sub> ⩾ 0 (Constraint 4)
> 5. x<sub>2</sub> ⩾ 0 (Constraint 5)
> 6. x<sub>3</sub> ⩾ 0 (Constraint 6)


## Input Format
The input comprises:
- A vector of coefficients of the objective function C.
- A matrix of coefficients of constraint functions A.
- A vector of right-hand side numbers b.
- The desired approximation accuracy.

## Output Format
The output includes either:
- The string "The method is not applicable!"
or
- A vector of decision variables x<sup>*</sup>.
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

