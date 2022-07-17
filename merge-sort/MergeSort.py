
import math


def mSort(arr):
    # first divide the array into two halves
    # pass them to mergeSort func
    # call merge func to merge the two sorted halves
    mergeSort(arr, 0, len(arr) - 1)
    return


def mergeSort(arr, start, end):
    if start >= end:
        return
    mid = math.floor((start + end) / 2)
    mergeSort(arr, mid + 1, end)
    mergeSort(arr, start, mid)
    # this will keep dividing the array until we reach halves that have only one element on them
    # then merge func can merge them into sorted sub arrays
    merge(arr, start, end)


def merge(arr, start, end):
    # all the action is here
    mid = math.floor((start + end) / 2)
    rightStart = start
    rightEnd = mid
    leftStart = mid + 1
    leftEnd = end
    temp = []
    while rightStart <= rightEnd and leftStart <= leftEnd:
        if arr[rightStart] < arr[leftStart]:
            temp.append(arr[rightStart])
            rightStart = rightStart + 1
        else:
            temp.append(arr[leftStart])
            leftStart = leftStart + 1

    while rightStart <= rightEnd:
        temp.append(arr[rightStart])
        rightStart = rightStart + 1

    while leftStart <= leftEnd:
        temp.append(arr[leftStart])
        leftStart = leftStart + 1

    # copy the temp array back to arr
    s = start
    i = 0
    while s <= end:
        arr[s] = temp[i]
        i = i + 1
        s = s + 1

    return
