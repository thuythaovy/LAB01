# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:48:36 2024

@author: nguyenthuythaovy 
"""

def is_negative_even_number(number):
  """Kiểm tra xem một số có phải là số chẵn âm hay không.

  Args:
    number: Số cần kiểm tra.

  Returns:
    True nếu số là chẵn âm, False nếu không.
  """

  return number % 2 == 0 and number < 0
number = int(input("Nhập một số nguyên: "))
result = is_negative_even_number(number)

if result:
  print("Số đã nhập là số chẵn âm.")
else:
  print("Số đã nhập không phải là số chẵn âm.")
  