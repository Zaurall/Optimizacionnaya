import math
import numpy as np
from numpy import linalg
from north_west import North_West
from vogel import Vogel
from input import S, C, D


def main():
    print("Matrix of coefficients of costs:")
    print(C)
    print("Vector of coefficients of supply:")
    print(S)
    print("Vector of coefficients of demand:")
    print(D)
    S1 = S.copy()
    C1 = C.copy()
    D1 = D.copy()
    North_West(S1, C1, D1)
    S2 = S.copy()
    C2 = C.copy()
    D2 = D.copy()
    Vogel(S2, C2, D2)
    S3 = S.copy()
    C3 = C.copy()
    D3 = D.copy()


if __name__ == "__main__":
    main()
