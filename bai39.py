# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:30:57 2024

@author: nguyenthuythaovy 
"""

def harmonic_sum(n):
  """Tính tổng dãy số hài hòa đến số hạng thứ n.

  Args:
    n: Số hạng cuối cùng của dãy.

  Returns:
    Tổng của dãy số.
  """

  s = 0
  for i in range(1, n + 1):
    s += 1 / i
  return s
n = int(input("Nhập số hạng cuối cùng n: "))
result = harmonic_sum(n)
print("Tổng của dãy số hài hòa đến số hạng thứ", n, "là:", result)
