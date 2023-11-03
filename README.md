# Optimizacionnaya

## Project Description
Optimizacionnaya is a computer program designed to solve a system of linear programming using the interior point method. The program focuses on solving maximization problems.

## Examples of problem

> The project aims to maximize the objective functions:
>
> Problem 1:
> F(x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>) = 9x<sub>1</sub> + 10x<sub>2</sub> + 16x<sub>3</sub>
> 
> subject to the following constraints:
> 1. 18x<sub>1</sub> + 15x<sub>2</sub> + 12x<sub>3</sub> ⩽ 360
> 2. 6x<sub>1</sub> + 4x<sub>2</sub> + 8x<sub>3</sub> ⩽ 192
> 3. 5x<sub>1</sub> + 3x<sub>2</sub> + 3x<sub>3</sub> ⩽ 180
> 4. x<sub>1</sub> ⩾ 0
> 5. x<sub>2</sub> ⩾ 0
> 6. x<sub>3</sub> ⩾ 0
> 
> Problem 2:
> F(x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>) = 4x<sub>1</sub> + 2x<sub>2</sub> - 3x<sub>3</sub>
> 
> subject to the following constraints:
> 1. 2x<sub>1</sub> - x<sub>2</sub> + 3x<sub>3</sub> ≤ 10
> 2. x<sub>1</sub> + 2x<sub>2</sub> + x<sub>3</sub> ≤ 12
> 3. 3x<sub>1</sub> + 4x<sub>2</sub> - 2x<sub>3</sub> ≤ 20
> 4. x<sub>1</sub> ≥ 0
> 5. x<sub>2</sub> ≥ 0
> 6. x<sub>3</sub> ≥ 0
>
> Problem 3:
> F(x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, x<sub>4</sub>) = 3x<sub>1</sub> + 2x<sub>2</sub> - x<sub>3</sub> + 4x<sub>4</sub>
> 
> subject to the following constraints:
> 1. 2x<sub>1</sub> + x<sub>2</sub> - 3x<sub>3</sub> + x<sub>4</sub> ≤ 8
> 2. x<sub>1</sub> + 3x<sub>2</sub> + 2x<sub>3</sub> - 2x<sub>4</sub> ≤ 10
> 3. 4x<sub>1</sub> - x<sub>2</sub> + 2x<sub>3</sub> + 3x<sub>4</sub> ≤ 12
> 4. x<sub>1</sub> + 2x<sub>2</sub> + x<sub>3</sub> + 2x<sub>4</sub> ≤ 6
> 5. x<sub>1</sub> ≥ 0
> 6. x<sub>2</sub> ≥ 0
> 7. x<sub>3</sub> ≥ 0
> 8. x<sub>4</sub> ≥ 0
>
> Problem 4:
> F(x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, x<sub>4</sub>, x<sub>5</sub>) = 2x<sub>1</sub> + 3x<sub>2</sub> - x<sub>3</sub> + 4x<sub>4</sub> - 2x<sub>5</sub>
> 
> subject to the following constraints:
> 1. x<sub>1</sub> - 2x<sub>2</sub> - 3x<sub>3</sub> ≤ 6
> 2. 2x<sub>1</sub> + x<sub>2</sub> + 2x<sub>4</sub> ≤ 8
> 3. 3x<sub>2</sub> - x<sub>4</sub> + x<sub>5</sub> ≤ 5
> 4. x<sub>1</sub> ≥ 0
> 5. x<sub>2</sub> ≥ 0
> 6. x<sub>3</sub> ≥ 0
> 7. x<sub>4</sub> ≥ 0
> 8. x<sub>5</sub> ≥ 0
>
> Problem 5:
> F(x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, x<sub>4</sub>, x<sub>5</sub>, x<sub>6</sub>) = 3x<sub>1</sub> + 2x<sub>2</sub> + 5x<sub>3</sub> - x<sub>4</sub> + 4x<sub>5</sub> + 2x<sub>6</sub>
> 
> subject to the following constraints:
> 1. 2x<sub>1</sub> - x<sub>2</sub> + 3x<sub>3</sub> + 4x<sub>4</sub> - x<sub>5</sub> + 2x<sub>6</sub> ≤ 10
> 2. 3x<sub>1</sub> + 3x<sub>2</sub> - 2x<sub>3</sub> + 2x<sub>4</sub> + 4x<sub>5</sub> - x<sub>6</sub> ≤ 12
> 3. x<sub>1</sub> + 2x<sub>2</sub> + 4x<sub>3</sub> - 3x<sub>4</sub> + 3x<sub>5</sub> + 2x<sub>6</sub> ≤ 15
> 4. 2x<sub>1</sub> - x<sub>2</sub> + 3x<sub>3</sub> + 2x<sub>4</sub> + x<sub>5</sub> - 4x<sub>6</sub> ≤ 8
> 5. x<sub>1</sub> ≥ 0
> 6. x<sub>2</sub> ≥ 0
> 7. x<sub>3</sub> ≥ 0
> 8. x<sub>4</sub> ≥ 0
> 9. x<sub>5</sub> ≥ 0
> 10. x<sub>6</sub> ≥ 0

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
- The maximum value of the objective function.

## Badges
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

## Usage
To use Optimizacionnaya for solving linear programming problems:
1. Clone this repository.
2. Set up your environment and install dependencies (if any).
3. Run the program with the necessary input parameters.
4. Review the output for the solution.
