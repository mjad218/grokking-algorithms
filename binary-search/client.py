from BinarySearch import BinarySearch

nums = [1, 5, 2, 3, 10, 50]
binarySearch = BinarySearch(nums)
binarySearch.sort()

# nums is now [1 , 2 , 3 , 5 , 10 , 50]
# 5 has index of 3
indexOfFive = binarySearch.findIndex(6)

print(f'found 5 at index {indexOfFive}')
