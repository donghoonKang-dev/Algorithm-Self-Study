# -*- coding: utf-8 -*-
# 문자열 뒤집기
# 리트코드344
# 두 가지 풀이 방식

import sys

# 첫 번째 방식
def flipStringOne(stringArr):
  start, finish = 0, len(stringArr) - 1
  while start < finish:
    stringArr[start], stringArr[finish] = stringArr[finish], stringArr[start]
    start += 1
    finish -= 1

# 두 번째 방식
def flipStringTwo(stringArr):
  stringArr.reverse()

arr = []
s = sys.stdin.readline()

for i in s:
  arr.append(i)
arr.pop() #종료 character 제거

flipStringOne(arr)
print(arr)