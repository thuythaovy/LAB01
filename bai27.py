# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:00:38 2024

@author: nguyenthuythaovy 
"""

import math
hinh = input("Nhập hình (v: vuông, n: chữ nhật, t: tròn):")
if hinh == 'v':
    canh = float(input("Nhập độ dài cạnh hình vuông: "))
    dien_tich = canh * canh
    chu_vi = 4 * canh
    print("Diện tích:", dien_tich)
    print("Chu vi:", chu_vi)
elif hinh == 'n':
    chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
    dien_tich = chieu_rong * chieu_dai
    chu_vi = 2 * (chieu_rong + chieu_dai)
    print("Diện tích:", dien_tich)
    print("Chu vi:", chu_vi)
elif hinh == 't':
    ban_kinh = float(input("Nhập bán kính hình tròn: "))
    dien_tich = math.pi * ban_kinh**2
    chu_vi = 2 * math.pi * ban_kinh
    print("Diện tích:", dien_tich)
    print("Chu vi:", chu_vi)
else:
    print("Hình không hợp lệ.")
