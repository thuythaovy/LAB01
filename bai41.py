# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:33:24 2024

@author: nguyenthuythaovy 
"""

def harmonic_sum_odd(n):
  """Tính tổng dãy số hài hòa các số lẻ đến số hạng thứ n.

  Args:
    n: Số hạng cuối cùng của dãy.

  Returns:
    Tổng của dãy số.
  """

  s = 0
  for i in range(1, n + 1):
    s += 1 / (2 * i - 1)  # Số lẻ thứ i là 2*i - 1
  return s
n = int(input("Nhập số hạng cuối cùng n: "))
result = harmonic_sum_odd(n)
print("Tổng của dãy số là:", result)
