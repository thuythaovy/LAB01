# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:09:21 2024

@author: nguyenthuythaovy 
"""

def so_ngay_trong_thang(thang, nam):
  """Tính số ngày trong một tháng.

  Args:
    thang: Số tháng (1-12).
    nam: Năm.

  Returns:
    Số ngày trong tháng.
  """

  thang_31_ngay = [1, 3, 5, 7, 8, 10, 12]
  if thang in thang_31_ngay:
    return 31
  elif thang == 2:
    if nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0):
      return 29
    else:
      return 28
  else:
    return 30
while True:
  try:
    thang = int(input("Nhập tháng (1-12): "))
    nam = int(input("Nhập năm: "))
    if 1 <= thang <= 12:
      break
    else:
      print("Tháng không hợp lệ.")
  except ValueError:
    print("Vui lòng nhập số.")
ket_qua = so_ngay_trong_thang(thang, nam)
print("Tháng", thang, "năm", nam, "có", ket_qua, "ngày.")
