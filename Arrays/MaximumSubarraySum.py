# Author: Abhishek Swain
# Mail: abhi08as.as@gmail.com
# Date: 26-10-2024

from io import BytesIO
from os import read, fstat
from sys import stdout

fast_input = BytesIO(read(0, fstat(0).st_size)).readline

n = int(fast_input().decode())

# Take input for space separated integers
arr = list(map(int, fast_input().split()))
max_sum, left, right = 0, 0, 0

for i in range(n):
    for j in range(i, n):
        curr_sum = 0
        for k in range(i, j):
            curr_sum += arr[k]
        # stdout.write(f"{str(curr_sum)}\n")
        if curr_sum > max_sum:
            max_sum = curr_sum
            left = i
            right = j

stdout.write(f"Max sum is: {str(max_sum)}\n")
stdout.write(" ".join([str(arr[l]) for l in range(left, right)]))
