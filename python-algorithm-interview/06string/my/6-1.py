# -*- coding: utf-8 -*-
# 유효한 팰린드롬
# 백준10988
import sys

def checkPalindrome(inputString):
  stack = []

  stringLength = len(inputString) - 1
  mid = stringLength // 2

  for i in range(0, stringLength):
    # 중간 전까진 stack에 담는다
    if i < mid:
      stack.append(inputString[i])
    # 중간 이후
    else:
      # 문자열 길이가 홀수일 때 중간 문자 동작
      if (stringLength % 2 == 1) and (i == mid):
        continue
      # 중간 문자 이후 동작 - 팰린드롬 검사
      else:
        if stack.pop() == inputString[i]:
          continue
        else:
          return(0)
  return(1)

s = sys.stdin.readline()
result = checkPalindrome(s)
print(result)