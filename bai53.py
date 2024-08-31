# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:12:42 2024

@author: nguyenthuythaovy 
"""

def tong_so_tu_nhien(n):
  """Tính tổng các số tự nhiên từ 1 đến n.

  Args:
    n: Số nguyên dương.

  Returns:
    Tổng các số từ 1 đến n.
  """

  return n * (n + 1) // 2

def tong_binh_phuong(n):
  """Tính tổng các bình phương từ 1^2 đến n^2.

  Args:
    n: Số nguyên dương.

  Returns:
    Tổng các bình phương từ 1^2 đến n^2.
  """

  return n * (n + 1) * (2*n + 1) // 6

def tong_phan_so(n):
  """Tính tổng các phân số từ 1/1 đến 1/n.

  Args:
    n: Số nguyên dương.

  Returns:
    Tổng các phân số từ 1/1 đến 1/n (dưới dạng số thực).
  """

  tong = 0
  for i in range(1, n+1):
    tong += 1/i
  return tong

def giai_thua(n):
  """Tính giai thừa của n.

  Args:
    n: Số nguyên dương.

  Returns:
    Giai thừa của n.
  """

  if n == 0:
    return 1
  else:
    return n * giai_thua(n-1)

def tich_tu_nhien(n):
  """Tính tích các số tự nhiên từ 1 đến n.

  Args:
    n: Số nguyên dương.

  Returns:
    Tích các số từ 1 đến n.
  """

  tich = 1
  for i in range(1, n+1):
    tich *= i
  return tich

n = int(input("Nhập một số nguyên dương n: "))

print("Tổng các số tự nhiên từ 1 đến", n, "là:", tong_so_tu_nhien(n))
print("Tổng các bình phương từ 1^2 đến", n**2, "là:", tong_binh_phuong(n))
print("Tổng các phân số từ 1/1 đến 1/", n, "là:", tong_phan_so(n))
print("Tổng các giai thừa từ 1! đến", n, "! là:", sum(giai_thua(i) for i in range(1, n+1)))
print("Tích các số tự nhiên từ 1 đến", n, "là:", tich_tu_nhien(n))