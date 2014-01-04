#!/usr/bin/python
import random

def quicksort(array):
  if len(array) <= 1:
    return array
  lower = []
  upper = []
  pivot = array[len(array)-1]

  for x in array[:len(array)-1]:
    if x <= pivot:
      lower.append(x)
    else:
      upper.append(x)
  sortedArray = quicksort(lower)
  sortedArray.append(pivot)
  sortedArray.extend(quicksort(upper))
  return sortedArray
arr = []
for i in range(0, 100):
  arr.insert(i, random.randrange(0, 1000))
p = quicksort(arr)
print(p)
