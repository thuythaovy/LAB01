# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:01:14 2024

@author: nguyenthuythaovy 
"""

def get_valid_input(min_value, max_value):
  """Nhập một số trong khoảng cho trước và kiểm tra tính hợp lệ.

  Args:
    min_value: Giá trị nhỏ nhất cho phép.
    max_value: Giá trị lớn nhất cho phép.

  Returns:
    Số nhập vào hợp lệ.
  """

  while True:
    try:
      number = int(input(f"Nhập một số trong khoảng [{min_value}, {max_value}]: "))
      if min_value <= number <= max_value:
        return number
      else:
        print("Số nhập vào không hợp lệ. Vui lòng nhập lại.")
    except ValueError:
      print("Vui lòng nhập một số nguyên.")
result = get_valid_input(-89, 90)
print("Số hợp lệ:", result)
