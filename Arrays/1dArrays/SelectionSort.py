import os, io


def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input().decode())

arr = []
for i in range(n):
    arr.append(int(input()))

print(*arr)
selection_sort(arr)
print(*arr)
