from RecursiveSum import sum
from RecursiveMax import maxWrap as max
from RecursiveCount import count
list = [1, 2, 5, 10, 80]

mySum = sum(list, 0)
myMax = max(list)
myCount = count(list)

print(f'the sum is {mySum}')
print(f'the max is {myMax}')
print(f'the count is {myCount}')
