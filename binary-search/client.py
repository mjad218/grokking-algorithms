from BinarySearch import BinarySearch
from BinarySearchBookSol import BinarySearchBookSol


nums = [1, 5, 2, 3, 10, 50]
binarySearch = BinarySearch(nums)
binarySearch.sort()

# nums is now [1 , 2 , 3 , 5 , 10 , 50]
# 5 has index of 3
indexOfFive = binarySearch.findIndex(5)

print(f'found 5 at index {indexOfFive}')


# Book implementation
binarySearch = BinarySearchBookSol(nums)
binarySearch.sort()


indexOfTen = binarySearch.findIndex(10)

# 10 has index of 4
print(f'found 10 at index {indexOfTen}')
