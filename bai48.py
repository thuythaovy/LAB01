# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:45:58 2024

@author: nguyenthuythaovy 
"""

def find_min_sum_solution(a, b, c, d):
  """Tìm bộ nghiệm (x, y, z) của phương trình ax + by + cz = d có tổng nhỏ nhất

  Args:
    a, b, c: Hệ số của x, y, z
    d: Hằng số tự do
  """

  min_sum = float('inf')
  min_solution = None
  for x in range(1, d // a + 1):
    for y in range(1, (d - a * x) // b + 1):
      z = (d - a * x - b * y) // c
      if z > 0:
        current_sum = x + y + z
        if current_sum < min_sum:
          min_sum = current_sum
          min_solution = (x, y, z)
  return min_solution
result = find_min_sum_solution(2, 7, 9, 979)
print("Bộ nghiệm có tổng nhỏ nhất:", result)
