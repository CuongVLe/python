#!/usr/bin/python
import random

def mergesort(array):
  if len(array) <= 1:
    return array
  midpoint = len(array)/2
  leftside = mergesort(array[:midpoint])
  rightside = mergesort(array[midpoint:])

  sortedArray = []
  while len(leftside) > 0 and len(rightside) > 0:
    if leftside[0] > rightside[0]:
      sortedArray.append(rightside.pop(0))
    else:
      sortedArray.append(leftside.pop(0))
  if len(leftside) > 0:
    sortedArray.extend(mergesort(leftside))
  else:
    sortedArray.extend(mergesort(rightside))
  return sortedArray

arr = []
for i in range(0, 10):
  arr.insert(i, random.randrange(0, 1000))

p = mergesort(arr)
print(p)
