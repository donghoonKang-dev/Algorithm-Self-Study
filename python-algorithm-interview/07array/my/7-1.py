# -*- coding: utf-8 -*-
# 두 수의 합
# 백준3273

import sys

n = int(sys.stdin.readline())
aArray = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

aArray.sort()

count = 0
left = 0
right = len(aArray) - 1

while left < right:
  diff = x - aArray[left]
  if diff < aArray[right]:
    right -= 1
  elif diff > aArray[right]:
    left += 1
  else:
    count += 1
    left += 1
    right -= 1

print(count)
  