# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:40:54 2024

@author: nguyenthuythaovy 
"""

def find_solutions(a, b, c, d):
  """Tìm tất cả các bộ nghiệm nguyên dương của phương trình ax + by + cz = d

  Args:
    a, b, c: Hệ số của x, y, z
    d: Hằng số tự do
  """

  for x in range(1, d // a + 1):
    for y in range(1, (d - a * x) // b + 1):
      z = (d - a * x - b * y) // c
      if z > 0:
        print(x, y, z)
find_solutions(2, 7, 9, 979)
