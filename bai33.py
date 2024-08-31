# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:21:52 2024

@author: nguyenthuythaovy 
"""

def is_perfect_square(n):
  import math
  return math.sqrt(n) % 1 == 0
n = int(input("Nhập số nguyên dương: "))
if is_perfect_square(n):
  print(n, "là số chính phương")
else:
  print(n, "không phải là số chính phương")
  