# -*- coding: utf-8 -*-
# ��ȿ�� �Ӹ����
# ����10988
import sys

def checkPalindrome(inputString):
  stack = []

  stringLength = len(inputString) - 1
  mid = stringLength // 2

  for i in range(0, stringLength):
    # �߰� ������ stack�� ��´�
    if i < mid:
      stack.append(inputString[i])
    # �߰� ����
    else:
      # ���ڿ� ���̰� Ȧ���� �� �߰� ���� ����
      if (stringLength % 2 == 1) and (i == mid):
        continue
      # �߰� ���� ���� ���� - �Ӹ���� �˻�
      else:
        if stack.pop() == inputString[i]:
          continue
        else:
          return(0)
  return(1)

s = sys.stdin.readline()
result = checkPalindrome(s)
print(result)