# First array has some elements and the second one has the same set of elements in a random order expect one element. Find the missing element.
def find(arr1,arr2):
  arr1.sort()
  arr2.sort()
  
  for num1,num2 in zip(arr1,arr2):
    if num1 != num2:
      return num1
  return arr1[-1]

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,4,2,5,6,7]

print(find(arr1,arr2))

# Alternate Solution
import collections 

def finder(arr1,arr2):
  d = collections.defaultdict(int)
  
  for num in arr2:
    d[num] += 1
  
  for num in arr1:
    if d[num] == 0:
      return num
    else:
      d[num] -= 1
      
print(finder(arr1,arr2))

