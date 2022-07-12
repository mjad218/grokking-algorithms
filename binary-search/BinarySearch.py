import math


class BinarySearch:
    def __init__(self, list):
        self.list = list

    def binarySearch(self, element, start, end):
        middle = math.floor((start + end) / 2)
        if (self.list[middle] == element):
            return middle
        if (self.list[middle] >= element):
            return self.binarySearch(element, start, middle - 1)

        if (self.list[middle] <= element):
            return self.binarySearch(element, middle + 1, end)

    def findIndex(self, element):
        end = len(self.list) - 1
        return self.binarySearch(element, 0, end)

    def sort(self):
        self.list.sort()
