# Author: Abhishek Swain
# Mail: abhi08as.as@gmail.com
# Date: 27-10-2024

from io import BytesIO
from os import read, fstat
from sys import stdout

fast_input = BytesIO(read(0, fstat(0).st_size)).readline

mRows = int(fast_input().decode())
nCols = int(fast_input().decode())

# Take input for newline separated integers
# matrix = [[int(fast_input().decode()) for _ in range(mCols)] for _ in range(mRows)]

# Take input for space separated integers
matrix = []
for _ in range(mRows):
    row = list(map(int, fast_input().decode().split()))
    matrix.append(row)

switch = 0
for col_idx in range(nCols):
    if switch == 0:
        for row_idx in range(mRows):
            stdout.write(str(matrix[row_idx][col_idx]) + " ")
        switch = 1
    else:
        for row_idx in range(mRows - 1, -1, -1):
            stdout.write(str(matrix[row_idx][col_idx]) + " ")
        switch = 0
