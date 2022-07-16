def sum(list, index, total=0):
    if index >= len(list):
        return total
    return sum(list, index + 1, total + list[index])
