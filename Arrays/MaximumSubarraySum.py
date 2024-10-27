# Author: Abhishek Swain
# Mail: abhi08as.as@gmail.com
# Date: 26-10-2024

from io import BytesIO
from os import read, fstat
from sys import stdout, maxsize

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
        max_sum = max(max_sum, curr_sum)
        left = i
        right = j

stdout.write(f"Max sum (brute-force) is: {str(max_sum)}\n")
stdout.write(" ".join([str(arr[l]) for l in range(left, right)]))

# Using cumulative sum

max_sum = -maxsize - 1
cum_sum = [0] * (n + 1)

# Compute the cumulative sum
for i in range(1, n + 1):
    cum_sum[i] = cum_sum[i - 1] + arr[i - 1]

# Find the maximum subarray sum
for i in range(n):
    for j in range(i, n):
        max_sum = max(max_sum, cum_sum[j + 1] - cum_sum[i])

stdout.write(f"Max sum (cumulative-sum) is: {str(max_sum)}\n")

# Kadane's Algorithm
max_sum, curr_sum = -maxsize - 1, 0
for e in arr:
    curr_sum += e
    if curr_sum < 0:
        curr_sum = 0
    max_sum = max(curr_sum, max_sum)

stdout.write(f"Max sum (Kadane's Algo) is: {str(max_sum)}\n")
