# Author: Abhishek Swain
# Mail: abhi08as.as@gmail.com
# Date: 26-10-2024

from io import BytesIO
from os import read, fstat
from sys import stdout

fast_input = BytesIO(read(0, fstat(0).st_size)).readline

n = int(fast_input().decode())
arr = []
for i in range(n):
    arr.append(int(fast_input().decode()))


stdout.write(" ".join(map(str, arr)))
stdout.write("\n")

i = 1
while i < len(arr):
    e = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > e:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = e
    i += 1

stdout.write(" ".join(map(str, arr)))
