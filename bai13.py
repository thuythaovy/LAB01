# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:08:54 2024

@author: nguyenthuythaovy 
"""

ngay = int(input("Nhập ngày sinh: "))
thang = int(input("Nhập tháng sinh: "))
nam = int(input("Nhập năm sinh: "))
dinh_dang_a = f"{ngay}/{thang}/{nam}"
print(f"a) {dinh_dang_a}")
dinh_dang_b = f"{ngay}/{thang}/{nam:02d}"
print(f"b) {dinh_dang_b}")
dinh_dang_c = f"{nam}/{thang}/{ngay}"
print(f"c) {dinh_dang_c}")
