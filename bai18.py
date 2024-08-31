# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:01:07 2024

@author: nguyenthuythaovy 
"""

print("Nhập chính xác số giờ, phút, giây giúp bạn có kết quả đúng nhất.")
gio1 = int(input("Nhập giờ của khoảng thời gian thứ nhất: "))
phut1 = int(input("Nhập phút của khoảng thời gian thứ nhất: "))
giay1 = int(input("Nhập giây của khoảng thời gian thứ nhất: "))

gio2 = int(input("Nhập giờ của khoảng thời gian thứ hai: "))
phut2 = int(input("Nhập phút của khoảng thời gian thứ hai: "))
giay2 = int(input("Nhập giây của khoảng thời gian thứ hai: "))

tong_giay1 = gio1 * 3600 + phut1 * 60 + giay1 
tong_giay2 = gio2 * 3600 + phut2 * 60 + giay2  

tong = tong_giay1 + tong_giay2
if tong_giay1<tong_giay2:
    hieu= tong_giay2 - tong_giay1
else:
    hieu = tong_giay1 - tong_giay2

print("Tổng hai khoảng thời gian là:", tong)
print("Hiệu hai khoảng thời gian là:", hieu)
