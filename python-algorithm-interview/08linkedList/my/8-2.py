# -*- coding: utf-8 -*-
# 두 정렬 리스트의 병합
# 리트코드21

import sys

fist_array_string, second_array_string = sys.stdin.readline().split(', ')
first_array = list(map(int, fist_array_string.split('->')))
second_array = list(map(int, second_array_string.split('->')))

result_list = []
first_index = 0
second_index = 0

while first_index < len(first_array) and second_index < len(second_array):
  if first_array[first_index] < second_array[second_index]:
    result_list.append(first_array[first_index])
    first_index += 1
  else:
    result_list.append(second_array[second_index])
    second_index += 1

if first_index == len(first_array):
  while second_index < len(second_array):
    result_list.append(second_array[second_index])
    second_index += 1
else:
  while first_index < len(first_array):
    result_list.append(first_array[first_index])
    first_index += 1

print('->'.join(list(map(str, result_list))))