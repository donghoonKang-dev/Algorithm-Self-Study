# -*- coding: utf-8 -*-
# 유효한 괄호
# 백준9012

import sys

def check_bracket(bracket_string):
  stack = []
  length = len(bracket_string) - 1
  for i in range(length):
    if bracket_string[i] == '(':
      stack.append(bracket_string[i])
    else: # i == ')'
      if len(stack) == 0:
        return False
      else:
        out = stack.pop()
        if out != '(':
          return False
  if len(stack) != 0:
    return False
  else:
    return True

T = int(sys.stdin.readline())

for _ in range(T):
  input_string = sys.stdin.readline()
  if check_bracket(input_string):
    print('YES')
  else:
    print('NO')

