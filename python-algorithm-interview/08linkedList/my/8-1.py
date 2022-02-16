# -*- coding: utf-8 -*-
# 팰린드롬 연결 리스트
# 리트코드234

import sys

numbers = list(map(int, sys.stdin.readline().split('->')))
result = 'true'

for i in range(len(numbers)//2):
  if numbers[i] != numbers[-1-i]:
    result = 'false'
    break

print(result)