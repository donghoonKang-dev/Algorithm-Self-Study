# -*- coding: utf-8 -*-
# 문자열 뒤집기
# 리트코드344
# 입출력 임의 변경

import sys

def flipString(stringArr):
  mid = len(stringArr) // 2
  for i in range(0, mid):
    tmp = stringArr[i]
    stringArr[i] = stringArr[-(i+1)]
    stringArr[-(i+1)] = tmp

arr = []
s = sys.stdin.readline()

for i in s:
  arr.append(i)
arr.pop() #종료 character 제거

flipString(arr)
print(arr)