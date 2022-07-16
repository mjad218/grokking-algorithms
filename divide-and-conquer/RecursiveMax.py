def maxWrap(list):
    return maxNum(list, 0, 0)


def maxNum(list, max, index):
    if index >= len(list) - 1:
        return max if list[index] < max else list[index]
    if max < list[index]:
        max = list[index]
    return maxNum(list, max, index + 1)
