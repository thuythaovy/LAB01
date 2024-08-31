# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:02:46 2024

@author: nguuyenthuythaovy 
"""

import math

def tinh_can_bac_hai(n):
  """Tính căn bậc hai của một số.

  Args:
    n: Số cần tính căn bậc hai.

  Returns:
    Căn bậc hai của n.
  """

  return math.sqrt(n)

def dao_so(n):
  """Đảo ngược các chữ số của một số.

  Args:
    n: Số cần đảo ngược.

  Returns:
    Số đảo ngược.
  """

  dao_nguoc = 0
  while n > 0:
    chu_so = n % 10
    dao_nguoc = dao_nguoc * 10 + chu_so
    n //= 10
  return dao_nguoc

def la_so_chinh_phuong(n):
  """Kiểm tra xem một số có phải là số chính phương hay không.

  Args:
    n: Số cần kiểm tra.

  Returns:
    True nếu n là số chính phương, False nếu không.
  """

  can_bac_hai = int(math.sqrt(n))
  return can_bac_hai * can_bac_hai == n

def la_so_nguyen_to(n):
  """Kiểm tra xem một số có phải là số nguyên tố hay không.

  Args:
    n: Số cần kiểm tra.

  Returns:
    True nếu n là số nguyên tố, False nếu không.
  """

  if n <= 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def tich_cac_chu_so_le(n):
  """Tính tích các chữ số lẻ của một số.

  Args:
    n: Số cần tính tích.

  Returns:
    Tích các chữ số lẻ của n.
  """

  tich = 1
  while n > 0:
    chu_so = n % 10
    if chu_so % 2 != 0:
      tich *= chu_so
    n //= 10
  return tich

def tong_so_nguyen_to_nho_hon(n):
  """Tính tổng các số nguyên tố nhỏ hơn n.

  Args:
    n: Giới hạn trên.

  Returns:
    Tổng các số nguyên tố nhỏ hơn n.
  """

  tong = 0
  for i in range(2, n):
    if la_so_nguyen_to(i):
      tong += i
  return tong

def tong_so_chinh_phuong_nho_hon(n):
  """Tính tổng các số chính phương nhỏ hơn n.

  Args:
    n: Giới hạn trên.

  Returns:
    Tổng các số chính phương nhỏ hơn n.
  """

  tong = 0
  i = 1
  while i*i < n:
    tong += i*i
    i += 1
  return tong

def tong_uoc_so(n):
  """Tính tổng các ước số dương của một số.

  Args:
    n: Số cần tính tổng ước.

  Returns:
    Tổng các ước số dương của n.
  """

  tong = 0
  for i in range(1, n+1):
    if n % i == 0:
      tong += i
  return tong

n = int(input("Nhập một số nguyên dương: "))

print("Căn bậc hai của", n, "là:", tinh_can_bac_hai(n))
print("Số đảo ngược của", n, "là:", dao_so(n))
print(n, "là số chính phương:", la_so_chinh_phuong(n))
print(n, "là số nguyên tố:", la_so_nguyen_to(n))
print("Tích các chữ số lẻ của", n, "là:", tich_cac_chu_so_le(n))
print("Tổng các số nguyên tố nhỏ hơn", n, "là:", tong_so_nguyen_to_nho_hon(n))
print("Tổng các số chính phương nhỏ hơn", n, "là:", tong_so_chinh_phuong_nho_hon(n))
print("Tổng các ước số của", n, "là:", tong_uoc_so(n))