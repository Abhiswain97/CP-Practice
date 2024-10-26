def BS_Recursive(arr, start, end, key):
    if start >= end:
        return -1

    mid = (start + end) // 2
    if key < arr[mid]:
        return BS_Recursive(arr, start, mid - 1, key)
    elif key > arr[mid]:
        return BS_Recursive(arr, mid + 1, end, key)
    else:
        return mid


def BS_Non_Recursive(arr):

    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            return mid
    return -1


n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

key = int(input())

res = BS_Recursive(arr, 0, len(arr) - 1, key)
res1 = BS_Non_Recursive(arr=arr)

(
    print(f"Element found at index: {res}")
    if res != -1
    else print(f"Element not found in the list")
)

(
    print(f"Element found at index: {res1}")
    if res1 != -1
    else print(f"Element not found in the list")
)
