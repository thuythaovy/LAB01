# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 09:29:41 2024

@author: 
"""
    
so_xe = input("Nhập số xe của bạn: ")
if len(so_xe) == 4 and so_xe.isdigit():
    tong_nut = sum(int(chu_so) for chu_so in so_xe)
    print("Số xe của bạn có tổng số nút là:",tong_nut % 10)
else:
    print("Vui lòng nhập số xe gồm 4 chữ số.")
    
    