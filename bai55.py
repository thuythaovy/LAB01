# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:45:55 2024

@author: ASUS
"""

def tinh_chu_vi(chieu_dai, chieu_rong):
  """Tính chu vi hình chữ nhật.

  Args:
    chieu_dai: Độ dài chiều dài.
    chieu_rong: Độ dài chiều rộng.

  Returns:
    Chu vi hình chữ nhật.
  """

  return 2 * (chieu_dai + chieu_rong)

def tinh_dien_tich(chieu_dai, chieu_rong):
  """Tính diện tích hình chữ nhật.

  Args:
    chieu_dai: Độ dài chiều dài.
    chieu_rong: Độ dài chiều rộng.

  Returns:
    Diện tích hình chữ nhật.
  """

  return chieu_dai * chieu_rong

def ve_hinh_chu_nhat(chieu_dai, chieu_rong):
  """Vẽ hình chữ nhật bằng các dấu *.

  Args:
    chieu_dai: Số lượng dấu * theo chiều ngang.
    chieu_rong: Số lượng dấu * theo chiều dọc.
  """

  for _ in range(chieu_rong):
    print("*" * chieu_dai)

chieu_dai = int(input("Nhập chiều dài: "))
chieu_rong = int(input("Nhập chiều rộng: "))

chu_vi = tinh_chu_vi(chieu_dai, chieu_rong)
dien_tich = tinh_dien_tich(chieu_dai, chieu_rong)
print("Chu vi hình chữ nhật:", chu_vi)
print("Diện tích hình chữ nhật:", dien_tich)
print("Hình chữ nhật:")
ve_hinh_chu_nhat(chieu_dai, chieu_rong)