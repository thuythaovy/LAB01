# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:08:40 2024

@author: nguyenthuythaovy 
"""

def tong_chu_so(n):
  """Tính tổng các chữ số của một số nguyên dương.

  Args:
    n: Số nguyên dương.

  Returns:
    Tổng các chữ số của n.
  """

  tong = 0
  while n > 0:
    tong += n % 10
    n //= 10
  return tong
n = int(input("Nhập một số nguyên dương: "))
ket_qua = tong_chu_so(n)
print("Tổng các chữ số của", n, "là:", ket_qua)
