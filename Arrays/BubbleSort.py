from io import BytesIO
from os import read, fstat
from sys import stdout

fast_input = BytesIO(read(0, fstat(0).st_size)).readline

n = int(fast_input().decode())

arr = []
for i in range(n):
    arr.append(int(fast_input()))

stdout.write(" ".join(map(str, arr)))
stdout.write("\n")

for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]

stdout.write(" ".join(map(str, arr)))
