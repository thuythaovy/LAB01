# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:07:59 2024

@author: 
"""

def uoc_so(n):
  """Tìm tất cả ước số của một số nguyên dương.

  Args:
    n: Số nguyên dương cần tìm ước.

  Returns:
    Một danh sách chứa tất cả ước số của n.
  """

  uoc = []
  for i in range(1, n+1):
    if n % i == 0:
      uoc.append(i)
  return uoc
while True:
  try:
    n = int(input("Nhập một số nguyên dương: "))
    if n <= 0:
      print("Vui lòng nhập số nguyên dương.")
    else:
      break
  except ValueError:
    print("Vui lòng nhập số.")
ket_qua = uoc_so(n)
print("Các ước số của", n, "là:", ket_qua)

