def swap(item1, item2):
    temp = item1
    item1 = item2
    item2 = temp


def seleSort(list):
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if list[i] < list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
