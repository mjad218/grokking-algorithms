def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, s, e):
    # first choose a pivot
    # make all elements greater than the pivot to the left of it
    # and the less to the right
    # use 3 pointers to achieve that
    # one beginning at start - 1 and is incremented to show the index of less elements

    pivot = e
    # Bad practice
    # I choose the pivot to be the last element
    start = s - 1
    # end = start

    # from start up to the end
    for j in range(s, e):
        if arr[j] < arr[pivot]:
            start += 1
            swap(arr, start, j)

    swap(arr, start + 1, pivot)
    return start + 1


def qSort(arr, start, end):
    # base case
    # one or two elements in the array - start = end
    if start >= end:
        return
    # else partition and qSort
    pivot = partition(arr, start, end)
    qSort(arr, start, pivot - 1)
    qSort(arr, pivot + 1, end)
