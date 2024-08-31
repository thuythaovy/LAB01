# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:17:43 2024

@author: nguyenthuythaovy 
"""

def kiem_tra_tam_giac(a, b, c):
  """Kiểm tra xem 3 số có tạo thành một tam giác không và xác định loại tam giác.

  Args:
    a, b, c: Độ dài ba cạnh của tam giác.

  Returns:
    Một chuỗi mô tả loại tam giác hoặc thông báo nếu không phải tam giác.
  """

  if a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and c + a > b:
    if a == b == c:
      return "Tam giác đều"
    elif a == b or b == c or c == a:
      if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        return "Tam giác vuông cân"
      else:
        return "Tam giác cân"
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        return "Tam giác vuông"
    else:
        return "Tam giác thường"
  else:
    return "Ba số không tạo thành một tam giác"
while True:
  try:
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))
    if a > 0 and b > 0 and c > 0:
      break
    else:
      print("Độ dài cạnh phải là số dương.")
  except ValueError:
    print("Vui lòng nhập số.")
ket_qua = kiem_tra_tam_giac(a, b, c)
print(ket_qua)
