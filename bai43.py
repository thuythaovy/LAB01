# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:36:33 2024

@author: nguyenthuythaovy 
"""

def sum_series(n):
  """Tính tổng dãy số S(n) = 1/2 + 2/3 + ... + n/(n+1)

  Args:
    n: Số hạng cuối cùng của dãy.

  Returns:
    Tổng của dãy số.
  """

  s = 0
  for i in range(1, n + 1):
    s += i / (i + 1)
  return s
n = int(input("Nhập số hạng cuối cùng n: "))
result = sum_series(n)
print("Tổng của dãy số là:", result)
