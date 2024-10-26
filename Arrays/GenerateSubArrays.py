# Author: Abhishek Swain
# Mail: abhi08as.as@gmail.com
# Date: 26-10-2024

from io import BytesIO
from os import read, fstat
from sys import stdout

fast_input = BytesIO(read(0, fstat(0).st_size)).readline

n = int(fast_input().decode())

# Take input for newline separated integers
arr = [int(fast_input().decode()) for _ in range(n)]

# Take input for space separated integers
# arr = list(map(int, fast_input().split()))

for i in range(n):
    for j in range(i, n):
        for k in range(i, j):
            stdout.write(str(arr[k]) + " ")
        stdout.write("\n")
