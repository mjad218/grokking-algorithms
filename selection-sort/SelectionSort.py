def swap(item1, item2):
    temp = item1
    item1 = item2
    item2 = temp


def seleSort(list):
    for i, item in enumerate(list):
        for j, item2 in enumerate(list):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
