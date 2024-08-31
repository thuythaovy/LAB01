# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:38:23 2024

@author: nguyenthuythaovy 
"""

def sum_series(n):
  """Tính tổng dãy số S(n) = 1/2 + 3/4 + ... + (2n+1)/(2n+2)

  Args:
    n: Số hạng cuối cùng của dãy.

  Returns:
    Tổng của dãy số.
  """

  s = 0
  for i in range(1, n + 1):
    s += (2 * i - 1) / (2 * i)
  return s
n = int(input("Nhập số hạng cuối cùng n: "))
result = sum_series(n)
print("Tổng của dãy số là:", result)
