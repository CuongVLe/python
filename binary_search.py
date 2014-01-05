#!/usr/bin/python

import random, time

def binarySearch(data, target):
  low = 0
  high = len(data)
  count = 0
  while(low +1 < high):
    count += 1
    time1 = time.time()
    test = (low + high)/2
    if(data[test] > target):
      high = test
    else:
      low = test
  if(data[low] == target):
    time2 = time.time()
    return low
  else:
    return

array = []
for i in range(0, 1000):
  array.insert(i, i)
t = random.randint(0,1000)
print("Finding: " + str(t))
f = binarySearch(array,t)
print(f)
