# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:43:55 2024

@author: nguyenthuythaovy 
"""

def find_max_sum_solution(a, b, c, d):
  """Tìm bộ nghiệm (x, y, z) của phương trình ax + by + cz = d có tổng lớn nhất

  Args:
    a, b, c: Hệ số của x, y, z
    d: Hằng số tự do
  """

  max_sum = 0
  max_solution = None
  for x in range(1, d // a + 1):
    for y in range(1, (d - a * x) // b + 1):
      z = (d - a * x - b * y) // c
      if z > 0:
        current_sum = x + y + z
        if current_sum > max_sum:
          max_sum = current_sum
          max_solution = (x, y, z)
  return max_solution
result = find_max_sum_solution(2, 7, 9, 979)
print("Bộ nghiệm có tổng lớn nhất:", result)
