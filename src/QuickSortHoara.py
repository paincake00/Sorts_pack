#EXE

array = [7, 1, 5, 2, 9, 9, 4, 0]

#LOGIC

def sortOfPart(arr, left, right):
    pivot = arr[(left + right) // 2]
    while left <= right:
        while arr[left] < pivot: left += 1
        while arr[right] > pivot: right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left

def quickSort(arr, start, end):
    if start >= end: return
    right = sortOfPart(arr, start, end)

    quickSort(arr, start, right - 1)
    quickSort(arr, right, end)

def quickSortHoara(arr):
    quickSort(arr, 0, len(arr) - 1)


quickSortHoara(array)
print(array)