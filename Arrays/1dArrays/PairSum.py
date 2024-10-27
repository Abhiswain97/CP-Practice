# Author: Abhishek Swain
# Mail: abhi08as.as@gmail.com
# Date: 27-10-2024

# Find all pairs matching the target sum

from io import BytesIO
from os import read, fstat
from sys import stdout

fast_input = BytesIO(read(0, fstat(0).st_size)).readline

n = int(fast_input().decode())

# Take input for newline separated integers
# arr = [int(fast_input().decode()) for _ in range(n)]

# Take input for space separated integers
arr = list(map(int, fast_input().split()))

target_sum = int(fast_input().decode())

start = 0
end = len(arr) - 1

while start < end:
    curr_sum = arr[start] + arr[end]
    if curr_sum < target_sum:
        start += 1
    elif curr_sum > target_sum:
        end -= 1
    else:
        stdout.write(f"{str(arr[start])}, {str(arr[end])}\n")
        start += 1
        end -= 1
