# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:56:24 2024

@author: nguyenthuythaovy 
"""

def check_number(number):
  """Kiểm tra một số và trả về giá trị tương ứng.

  Args:
    number: Số cần kiểm tra.

  Returns:
    -1 nếu số âm và lẻ, 1 nếu số dương và chẵn, 0 trong các trường hợp khác.
  """

  if number < 0 and number % 2 != 0:
    return -1
  elif number > 0 and number % 2 == 0:
    return 1
  else:
    return 0
number = int(input("Nhập một số nguyên:"))
result = check_number(number)
print("Kết quả:", result)
