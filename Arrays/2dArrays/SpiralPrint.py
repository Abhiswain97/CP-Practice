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


# row_start, row_end, col_start, col_end = 0, 0, 0, 0
# switch = 0

res = []
while matrix:
    print(*matrix)
    res += matrix.pop(0)
    # print(res)
    matrix = list(zip(*matrix))[::-1]
