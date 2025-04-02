def print_sol():
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print()
    print()

def is_safe(row, col):
    for i in range(row):
        if a[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if a[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if a[i][j] == 1:
            return False

    return True

def nqueen(row):
    if row == n:
        print_sol()
    else:
        for col in range(n):
            if is_safe(row, col):
                a[row][col] = 1
                nqueen(row + 1)
                a[row][col] = 0

n = int(input("Enter the value of N: "))
a = [[0] * n for _ in range(n)]
nqueen(0)