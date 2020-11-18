import numpy as np

def is_dominant_matrix(mat):
    for i, row in enumerate(mat):
        s = sum(abs(v) for j, v in enumerate(row) if i != j)
        if s > abs(row[i]):
            return False
    return True


def calc_gauss_zeidl():
    # Initial setup
    x0 = 0
    y0 = 0
    z0 = 0
    count = 1
    error = 0.001
    print('The Relative Error is 0.00001 \n')
    state = True
    while state:
        x1 = funcX(x0, y0, z0)
        y1 = funcY(x1, y0, z0)
        z1 = funcZ(x1, y1, z0)
        print('%d\t%0.3f\t%0.3f\t%0.3f\n' % (count, x1, y1, z1))
        e1 = abs(x0 - x1)
        e2 = abs(y0 - y1)
        e3 = abs(z0 - z1)

        count += 1
        x0 = x1
        y0 = y1
        z0 = z1

        state = e1 > error and e2 > error and e3 > error
    print('\nSolution: x=%0.2f, y=%0.2f and z = %0.2f\n' % (x1, y1, z1))


def calc_Jacobi():
    # Initial setup
    x0 = 0
    y0 = 0
    z0 = 0
    count = 1
    error = 0.001
    print('The Relative Error is 0.00001 \n')
    state = True
    while state:
        x1 = funcX(x0, y0, z0)
        y1 = funcY(x0, y0, z0)
        z1 = funcZ(x0, y0, z0)
        print('%d\t%0.3f\t%0.3f\t%0.3f\n' % (count, x1, y1, z1))
        e1 = abs(x0 - x1)
        e2 = abs(y0 - y1)
        e3 = abs(z0 - z1)

        count += 1
        x0 = x1
        y0 = y1
        z0 = z1

        state = e1 > error and e2 > error and e3 > error
    print('\nSolution: x=%0.2f, y=%0.2f and z = %0.2f\n' % (x1, y1, z1))


if __name__ == "__main__":
    mat = np.zeros((3, 3), dtype=float)
    answer = np.zeros(3, dtype=float)

    # Input data
    for i in range(3):
        for j in range(3):
           mat_number = int(input(f"Please Enter Elements ({i},{j}) in Matrix : "))
           if j == 2:
               ans_number = int(input(f"Please Enter Elements {i} answer : "))
               answer[i] = ans_number
           mat[i][j] = mat_number


    if not is_dominant_matrix(mat):
        print("The matrix does not have a dominant diagonal")
        exit(0)

    # Input data by the dominate slant
    funcX = lambda x, y, z:  (answer[0] + (-mat[0][1]) * y + (-mat[0][2]) * z) / mat[0][0]
    funcY = lambda x, y, z:  (answer[1] + (-mat[1][0]) * x + (-mat[1][2]) * z) / mat[1][1]
    funcZ = lambda x, y, z: (answer[2] + (-mat[2][0]) * x + (-mat[2][1]) * y) / mat[2][2]

    print("gauss-zeidl:")
    calc_gauss_zeidl()
    print("Jacobi:")
    calc_Jacobi()
