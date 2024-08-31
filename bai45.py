# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:39:56 2024

@author: nguyenthuythaovy 
"""

def sum_series(x, n):
  """Tính tổng dãy số S(n)

  Args:
    x: Cơ số của lũy thừa
    n: Số hạng cuối cùng của dãy

  Returns:
    Tổng của dãy số.
  """

  s = 0
  for i in range(1, n + 1):
    denominator = i * (i + 1) // 2  # Tính tổng các số từ 1 đến i
    s += (x ** i) / denominator
  return s
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập số hạng cuối cùng n: "))
result = sum_series(x, n)
print("Tổng của dãy số là:", result)
