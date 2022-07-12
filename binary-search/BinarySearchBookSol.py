import math


class BinarySearchBookSol:
    def __init__(self, list):
        self.list = list

    def binarySearch(self, element):
        start = 0
        end = len(self.list) - 1
        while start <= end:
            middle = math.floor((start + end) / 2)
            if (self.list[middle] == element):
                return middle
            if (end == start):
                return None
            if (self.list[middle] > element):
                end = middle - 1
            if (self.list[middle] < element):
                start = middle + 1
        return None

    def findIndex(self, element):
        end = len(self.list) - 1
        return self.binarySearch(element)

    def sort(self):
        self.list.sort()
