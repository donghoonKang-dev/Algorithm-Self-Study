# -*- coding: utf-8 -*-
# 빗물
# 백준14719

import sys

H, W = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))
result = 0

top = max(blocks)
topIndex = blocks.index(top)

leftIndex = 0
rightIndex = len(blocks) - 1

while leftIndex < topIndex - 1:
  if blocks[leftIndex] > blocks[leftIndex + 1]:
    diff = blocks[leftIndex] - blocks[leftIndex + 1]
    result += diff
    blocks[leftIndex + 1] += diff
  leftIndex += 1

while rightIndex > topIndex + 1:
  if blocks[rightIndex] > blocks[rightIndex - 1]:
    diff = blocks[rightIndex] - blocks[rightIndex - 1]
    result += diff
    blocks[rightIndex - 1] += diff
  rightIndex -= 1

print(result)

# 투포인터를 응용했지만 왼쪽에서 오른쪽으로 진행하는 스택형식으로도 풀 수 있다 -> solution