import numpy as np


def main():
    A = np.array([[3, -9], [2, 4]])
    b = np.array([-42, 2])

    z = np.linalg.solve(A, b)
    print(z)

    M = np.array([[1, -2, -1], [2, 2, -1], [-1, -1, 2]])
    c = np.array([6, 1, 1])

    y = np.linalg.solve(M, c)
    print(y)

    F = np.array([[30, 20], [50, 60]])
    e = np.array([6000, 12000])

    r = np.linalg.solve(F, e)
    print(r)


if __name__ == '__main__':
    main()
