# -*- coding: utf-8 -*-
# 유효한 팰린드롬
# 리트코드125
import sys

def checkPalindrome(inputString):
  stringArr = []

  for char in inputString:
    if char.isalnum():
      stringArr.append(char.lower())

  while len(stringArr) > 1:
    if stringArr.pop(0) != stringArr.pop():
      return False
  return True

s = sys.stdin.readline()
result = checkPalindrome(s)
print(result)